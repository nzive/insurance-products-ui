from flask import Flask, request, jsonify, render_template, redirect, url_for, session
import json
import os

app = Flask(__name__, 
            template_folder='../frontend/templates', 
            static_folder='../frontend/static')
app.secret_key = 'super_secret_key'

# Hardcoded credentials for testing [cite: 27, 39]
VALID_CLIENT_ID = "test_client"
VALID_CLIENT_SECRET = "test_secret"
VALID_USER = {"username": "user1", "password": "pass1"}

# Load mock data [cite: 29]
def load_products():
    with open('products.json', 'r') as f:
        return json.load(f)

# --- OAuth 2.0 Token Endpoint [cite: 27] ---
@app.route('/oauth/token', methods=['POST'])
def token():
    # Simple Resource Owner Password Credentials Grant [cite: 26]
    client_id = request.form.get('client_id')
    username = request.form.get('username')
    password = request.form.get('password')

    if client_id == VALID_CLIENT_ID and username == VALID_USER['username'] and password == VALID_USER['password']:
        # Issue a mock access token [cite: 27]
        access_token = "mock_access_token_abc123"
        session['access_token'] = access_token
        return jsonify({"access_token": access_token, "token_type": "Bearer"})
    
    return jsonify({"error": "invalid_grant"}), 401

# --- Secured API Endpoint [cite: 15, 28] ---
@app.route('/api/products', methods=['GET'])
def get_products():
    auth_header = request.headers.get('Authorization')
    # Require valid access_token in header [cite: 28]
    if auth_header == "Bearer mock_access_token_abc123":
        return jsonify(load_products())
    return jsonify({"error": "unauthorized"}), 401

# --- Frontend Routes (Server-Side Rendering) ---
@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def handle_login():
    # This simulates the frontend call to /oauth/token [cite: 34]
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username == VALID_USER['username'] and password == VALID_USER['password']:
        session['access_token'] = "mock_access_token_abc123"
        return redirect(url_for('display_products'))
    return "Invalid Credentials", 401

@app.route('/products_ui')
def display_products():
    # Secure UI route [cite: 12]
    if 'access_token' not in session:
        return redirect(url_for('login_page'))
    
    products_data = load_products()
    return render_template('products.html', products=products_data)

if __name__ == '__main__':
    app.run(port=5000, debug=True)

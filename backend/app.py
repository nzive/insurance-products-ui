from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import requests

app = Flask(__name__)
app.secret_key = 'super_secret_key'  # Required for session storage

# Mock Data
VALID_USER = {"username": "user1", "password": "pass1"}
VALID_CLIENT = {"id": "test_client", "secret": "test_secret"} [cite: 39]

# --- API SECTION ---
@app.route('/oauth/token', methods=['POST'])
def oauth_token():
    # Simplistic implementation of Resource Owner Password Credentials Grant [cite: 26]
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username == VALID_USER['username'] and password == VALID_USER['password']:
        return jsonify({"access_token": "mock_token_123", "token_type": "Bearer"})
    return jsonify({"error": "invalid_grant"}), 401

@app.route('/api/products')
def get_products_api():
    token = request.headers.get('Authorization')
    if token != "Bearer mock_token_123":
        return jsonify({"error": "unauthorized"}), 401
    
    products = [
        {"id": "prod_001", "name": "Premium Health Plan", "type": "HEALTH", "coverage": "Full medical + dental", "price": 200.00},
        {"id": "prod_002", "name": "Basic Life Insurance", "type": "LIFE", "coverage": "Standard payout", "price": 50.00}
    ] [cite: 16, 20, 21, 22, 23, 24]
    return jsonify(products)

# --- UI SECTION (No JavaScript needed) ---
@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def handle_login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Internal call to the token endpoint [cite: 34]
    if username == VALID_USER['username'] and password == VALID_USER['password']:
        session['token'] = "mock_token_123"
        return redirect(url_for('products_page'))
    return "Login Failed", 401

@app.route('/products')
def products_page():
    token = session.get('token')
    if not token:
        return redirect(url_for('login_page'))
    
    # Render UI using Python data
    products_list = [
        {"id": "prod_001", "name": "Premium Health Plan", "type": "HEALTH", "coverage": "Full medical + dental", "price": 200.00}
    ]
    return render_template('products.html', products=products_list)

if __name__ == '__main__':
    app.run(debug=True)

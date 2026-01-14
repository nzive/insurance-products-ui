from flask import Flask, jsonify, request, abort
from flask_cors import CORS
import uuid

app = Flask(__name__)
CORS(app) # Allows frontend to communicate with backend

# Mock Data 
VALID_CLIENT_ID = "test_client"
VALID_CLIENT_SECRET = "test_secret"
VALID_USER = {"username": "user1", "password": "pass1"}
tokens = {} # In-memory token store [cite: 29]

products = [
    {
        "id": "prod_001",
        "name": "Premium Health Plan",
        "type": "HEALTH",
        "coverage": "Full medical + dental",
        "price": 200.00
    }
]

# 1. OAuth Token Endpoint [cite: 27, 34]
@app.route('/oauth/token', methods=['POST'])
def get_token():
    auth = request.authorization or request.form
    grant_type = request.form.get('grant_type')
    
    # Check Client Credentials and User Credentials [cite: 34, 39]
    if (request.form.get('client_id') == VALID_CLIENT_ID and 
        request.form.get('username') == VALID_USER['username'] and 
        request.form.get('password') == VALID_USER['password']):
        
        access_token = str(uuid.uuid4())
        tokens[access_token] = VALID_USER['username']
        return jsonify({"access_token": access_token, "token_type": "Bearer"})
    
    return jsonify({"error": "invalid_grant"}), 401

# 2. Secured Products Endpoint [cite: 15, 28]
@app.route('/api/products', methods=['GET'])
def get_products():
    auth_header = request.headers.get('Authorization')
    if not auth_header or "Bearer " not in auth_header:
        abort(401)
    
    token = auth_header.split(" ")[1]
    if token not in tokens:
        abort(401)
        
    return jsonify(products)

if __name__ == '__main__':
    app.run(port=5000, debug=True)

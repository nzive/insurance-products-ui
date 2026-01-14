from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Hardcoded credentials
CLIENT_ID = "test_client"
CLIENT_SECRET = "test_secret"
USERNAME = "user1"
PASSWORD = "pass1"
ACCESS_TOKEN = "mock_access_token_123"

@app.route("/oauth/token", methods=["POST"])
def token():
    data = request.json

    if (
        data.get("client_id") == CLIENT_ID and
        data.get("client_secret") == CLIENT_SECRET and
        data.get("username") == USERNAME and
        data.get("password") == PASSWORD
    ):
        return jsonify({
            "access_token": ACCESS_TOKEN,
            "token_type": "Bearer"
        }), 200

    return jsonify({"error": "invalid_credentials"}), 401


@app.route("/api/products", methods=["GET"])
def products():
    auth_header = request.headers.get("Authorization")

    if auth_header != f"Bearer {ACCESS_TOKEN}":
        return jsonify({"error": "unauthorized"}), 401

    with open("products.json") as f:
        return jsonify(json.load(f)), 200


if __name__ == "__main__":
    app.run(debug=True)

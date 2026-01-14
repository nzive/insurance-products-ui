# Insurance Products UI - Technical Assessment

This project is a full-stack insurance product display application featuring a secured Flask backend and a responsive Jinja2-rendered frontend.

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Flask
- Pytest

### Installation
1. Clone the repository:
   `git clone https://github.com/nzive/insurance-products-ui.git`
2. Install dependencies:
   `pip install flask pytest`

## 🛠 Running the Application
1. Start the Flask server from the root directory:
   `python backend/app.py`
2. Access the UI in your browser at:
   `http://127.0.0.1:5000`

## 🧪 Testing
This project uses **Pytest** for backend logic and security verification. You can run all tests with a single command:
`python -m pytest backend/tests_backend.py`

## 🔑 Credentials
Use the following hardcoded credentials to access the products page:
- **Username:** user1
- **Password:** pass1
- **OAuth Client ID:** test_client
- **OAuth Client Secret:** test_secret

## ✨ Features
- **API Security:** All product data is protected via Bearer token authorization.
- **Responsive Design:** Optimized for Mobile, Tablet, and Desktop using CSS Media Queries.
- **Automated CI:** GitHub Actions configured for continuous testing on every push.

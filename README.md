# Insurance Products UI – OAuth 2.0 Demo

## Overview
This project demonstrates a simple insurance products application secured using OAuth 2.0 authentication.  
It focuses on system design, authentication flow, API security, and responsive UI rather than complex programming.

---

## Features
- Login screen simulating OAuth 2.0 authentication
- Secured access to insurance products
- Responsive user interface (mobile, tablet, desktop)
- Mock insurance product data
- Clear separation of frontend and backend

---

## OAuth 2.0 Configuration
The application uses a simplified OAuth 2.0 Password Grant flow.

Credentials used for demonstration:
- Client ID: test_client
- Client Secret: test_secret
- Username: user1
- Password: pass1

---

## API Endpoints (Conceptual)
- POST /oauth/token  
  Issues an access token after successful authentication.

- GET /api/products  
  Returns insurance products.  
  Access is restricted and requires a valid OAuth 2.0 access token.

---

## Project Structure
frontend/ – User interface (HTML/CSS)  
backend/ – OAuth explanation and mock data  

---

## Notes
This repository is intended to demonstrate understanding of secure system design, OAuth 2.0 authentication, and API protection in the simplest possible form.

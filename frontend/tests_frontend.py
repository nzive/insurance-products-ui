import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_api_security(client):
    # Unauthenticated requests must fail [cite: 55]
    response = client.get('/api/products')
    assert response.status_code == 401

def test_oauth_token(client):
    # Test valid credentials [cite: 34]
    response = client.post('/oauth/token', data={
        'client_id': 'test_client',
        'username': 'user1',
        'password': 'pass1'
    })
    assert response.status_code == 200
    assert 'access_token' in response.json

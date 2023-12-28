import pytest
from pytest_factoryboy import register
import httpx

@pytest.fixture
def authenticated_client():
    client = httpx.Client(base_url='http://testserver')

    # Substitua com os detalhes da sua API de login
    login_data = {
        "username": "your_username",
        "password": "your_password"
    }
    response = client.post('/api/login/', data=login_data)

    token = response.json().get('token')
    client.headers['Authorization'] = f'Token {token}'

    return client
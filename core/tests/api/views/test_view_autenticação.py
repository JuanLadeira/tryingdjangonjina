import pytest

@pytest.mark.django_db
def test_some_authenticated_action(authenticated_client):
    response = authenticated_client.get('/api/')
    assert response.status_code == 200
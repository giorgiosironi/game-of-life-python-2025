import pytest
from bs4 import BeautifulSoup
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

@pytest.fixture
def page(client):
    def _get_page(url):
        response = client.get(url)
        return BeautifulSoup(response.data, 'html.parser')
    return _get_page 

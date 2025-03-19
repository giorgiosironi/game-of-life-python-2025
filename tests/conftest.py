from flask.testing import FlaskClient
import pytest
from bs4 import BeautifulSoup
from app import app
from fixtures_types import LoadPage

@pytest.fixture
def client() -> FlaskClient:
    app.config['TESTING'] = True
    return app.test_client()

@pytest.fixture
def page(client: FlaskClient) -> LoadPage:
    def _load_page(url: str) -> BeautifulSoup:
        response = client.get(url)
        return BeautifulSoup(response.data, 'html.parser')
    return _load_page 

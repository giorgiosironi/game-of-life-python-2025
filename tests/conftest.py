from flask.testing import FlaskClient
import pytest
from typing import TypeAlias, Callable
from bs4 import BeautifulSoup
from app import app

@pytest.fixture
def client() -> FlaskClient:
    app.config['TESTING'] = True
    return app.test_client()

LoadPage: TypeAlias = Callable[[str], BeautifulSoup]

@pytest.fixture
def page(client: FlaskClient) -> LoadPage:
    def _load_page(url: str) -> BeautifulSoup:
        response = client.get(url)
        return BeautifulSoup(response.data, 'html.parser')
    return _load_page 

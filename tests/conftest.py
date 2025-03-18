from flask.testing import FlaskClient
import pytest
from typing import TypeAlias, Callable
from bs4 import BeautifulSoup
from app import app

@pytest.fixture
def client() -> FlaskClient:
    app.config['TESTING'] = True
    return app.test_client()

PageGetter: TypeAlias = Callable[[str], BeautifulSoup]

@pytest.fixture
def page(client: FlaskClient) -> PageGetter:
    def _get_page(url: str) -> BeautifulSoup:
        response = client.get(url)
        return BeautifulSoup(response.data, 'html.parser')
    return _get_page 

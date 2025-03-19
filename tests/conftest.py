from flask.testing import FlaskClient
import pytest
from bs4 import BeautifulSoup
from fixtures_types import LoadPage
from app import app


@pytest.fixture(name='client')
def fixture_client() -> FlaskClient:
    app.config['TESTING'] = True
    return app.test_client()


@pytest.fixture(name='page')
def fixture_page(client: FlaskClient) -> LoadPage:
    def _load_page(url: str) -> BeautifulSoup:
        response = client.get(url)
        return BeautifulSoup(response.data, 'html.parser')
    return _load_page

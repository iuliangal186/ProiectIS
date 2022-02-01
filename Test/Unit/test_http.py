import pytest
import json
from server_http import get_app



@pytest.fixture
def client():

    local_app = get_app()
    client = local_app.test_client()

    yield client

def test_root_endpoint(client):
    landing = client.get("/")
    html = landing.data.decode()

    assert "Welcome to the smart GreenHouse !" in html
    assert landing.status_code == 200

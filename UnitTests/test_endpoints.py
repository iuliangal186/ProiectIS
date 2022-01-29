from grpc import server
import pytest
import server_http

@pytest.fixture
def client():
    server_http.init_http()
    server_http.run_http_server()

    local_app = server_http.get_app()
    client = local_app.test_client()

    yield client

def test_root_endpoint(client):
    landing = client.get("/")
    html = landing.data.decode()

    assert 'Hello World!' in html
    assert landing.status_code == 200
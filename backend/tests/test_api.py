from fastapi.testclient import TestClient

from main import app


def test_client_app_can_start():
    TestClient(app)

"""Tests for the backend API."""

from fastapi.testclient import TestClient

from main import app


def test_client_app_can_start():
    """Test that the app can start."""
    TestClient(app)

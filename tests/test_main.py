"""
Initialisation de l'objet app
"""

from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_read_root():
    """
    Vérifie que l'endpoint racine renvoie le message de bienvenue et un code 200.
    Cela assure que l'API est en ligne et accessible.
    """

    expected_json = {"message": "Hello World"}

    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == expected_json


def test_read_quote():
    """
    Vérifié que l'endpoint renvoie le bon message et le bon code.
    """

    response = client.get("/quote")
    assert response.status_code == 200
    assert "citation" in response.json()

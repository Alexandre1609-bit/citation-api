"""
Initialisation de l'objet app
"""

from fastapi.testclient import TestClient
from sqlmodel import SQLModel
import pytest
from app.main import app
from app.database import ENGINE


def test_read_root(client):
    """
    Vérifie que l'endpoint racine renvoie le message de bienvenue et un code 200.
    Cela assure que l'API est en ligne et accessible.
    """
    expected_json = {"message": "Hello World"}
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == expected_json


def test_create_quote(client):
    """
    Vérifie la création d'une citation.
    envoie une donnée.
    vérifie qu'on reçoit un 200 OK.
    vérifie que la réponse contient bien la citation envoyée.
    vérifie qu'un ID a été généré (et n'est pas null).
    """
    # envoie le JSON
    response = client.post("/quote", json={"citation": "Omelette du fromage"})

    # Vérification du statut
    assert response.status_code == 200

    # Extraction des données
    data = response.json()

    # Vérifications du contenu
    assert data["citation"] == "Omelette du fromage"
    assert "id" in data
    assert data["id"] is not None


def test_read_quote_empty(client):
    response = client.get("/quote")

    print(f"DEBUG RESPONSE: {response.json()}")
    assert response.status_code == 404

    data = response.json()
    assert "detail" in data
    assert data["detail"] == "No quote found"

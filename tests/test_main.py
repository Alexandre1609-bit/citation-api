"""
Initialisation de l'objet app
"""

from fastapi.testclient import TestClient
from app.main import app
import pytest
from app.database import engine
from sqlmodel import SQLModel


# Fixture : Une Fixture est une fonction de préparation qui s'exécute avant chaque test
# pour "mettre la table" (créer la BDD, préparer le client).
@pytest.fixture(name="client")
def client_fixture():
    # Force la création des tables pour le test
    SQLModel.metadata.create_all(engine)
    return TestClient(app)


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

from fastapi.testclient import TestClient
from app.main import app #On lancera le test depuis la racine avec Pytest, pour éviter me modifier le code avec "os". C'est plus propre ainsi.


client = TestClient(app)

def test_read_root():
    expected_json = {"message": "Hello World"}

    response = client.get("/") #On simule la reqête sur "/". 

    assert response.status_code == 200 #Si code 200, OK.
    assert response.json() == expected_json #Compare les json pour vérifier.

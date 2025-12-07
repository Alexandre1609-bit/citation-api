# Citation API

## Description
Une API REST moderne et robuste, développée selon les principes du **Clean Code**, **TDD**, et **DevSecOps**. Elle fournit des citations inspirantes de manière aléatoire via une architecture micro-service conteneurisée.

## Stack Technique
* **Langage :** Python 3.13
* **Framework :** FastAPI (Performance & Async)
* **Validation :** Pip-audit, Pydantic (Strong Typing)
* **Qualité :** Black, Pylint
* **CI/CD :** GitHub Actions (Quality Gate, Security Audit, Delivery)
* **Conteneurisation :** Docker & GHCR

## Installation & Démarrage

### Via Docker (Recommandé)
Le moyen le plus simple de lancer l'application : 
```bash
docker compose up
```
Via Python (Développement)

1. Créer l'environnement virtuel : ```python -m venv venv```
2. Activer l'environnement : ```source venv/bin/activate``` (Mac/Linux) ou ```venv\Scripts\Activate``` (Windows)
3. Installer les dépendances : ```pip install -r requirements.txt```
4. Lancer le serveur : ```fastapi dev app/main.py```


## Tests & Qualité
Le projet suit une approche TDD stricte. Pour lancer les tests unitaires :
```bash
pytest
```

## Architecture
* app/ : Code source de l'API
* tests/ : Test unitaires (isolés du code)
* .github/ : Pipeline CI/CD
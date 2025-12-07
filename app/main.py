"""Import"""

from fastapi import FastAPI
import random

app = FastAPI()

fake_db = [
    {"citation": "La vie est un mystère qu'il faut vivre, et non un problème à résoudre."}, 
    {"citation": "Le plus grand risque est de ne prendre aucun risque."},
    {"citation": "L'important n'est pas la chute, mais l'atterrissage."}
    ]


@app.get("/")
async def root() -> dict:
    """
    Renvoie un message de bienvenue simple au format JSON.
    """
    return {"message": "Hello World"}

@app.get("/quote")
async def quote() -> dict:
    """
    Retourne une citation aléatoire depuis la base de données.

    Returns:
        dict: un dictionnaire contenant la citation.
    """
    return random.choice(fake_db)
    #TDD (Test Driven Development) ?

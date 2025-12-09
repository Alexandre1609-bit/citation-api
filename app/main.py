"""Import"""

from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select

from app.database import get_session, create_db_and_tables
from app.schemas import Quote


# Lifespan (démarrage auto)
# S'exécute une seule fois quand je lance l'API
@asynccontextmanager
async def lifespan(_application: FastAPI):
    """Lance la DB avant que l'application ne se lance"""
    create_db_and_tables()  # Crée la table si elle n'existe pas
    yield  # Laisse l'appli tourner


# On initialise avec le lifespan
# Crée les tables si elles n'existent pas encore
app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root() -> dict:
    """
    Renvoie un message de bienvenue simple au format JSON.
    """
    return {"message": "Hello World"}


@app.post("/quote")
async def create_quote(quote: Quote, session: Session = Depends(get_session)) -> Quote:
    """On crée et commit quote"""
    session.add(quote)
    session.commit()
    session.refresh(quote)
    return quote


@app.get("/quote")
async def get_quote(session: Session = Depends(get_session)) -> Quote | None:
    """
    Retourne la première citation trouvée dans la base de données.
    """
    # Prépare la requête: "SELECT * FROM quote"
    statement = select(Quote)

    # Execute le statement et on prend le premier résultat
    result = session.exec(statement).first()
    if not result:
        raise HTTPException(status_code=404, detail="No quote found")

    return result
    # TDD (Test Driven Development) ?

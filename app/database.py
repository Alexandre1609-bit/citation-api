"""import des modules"""
from sqlmodel import Session, SQLModel, create_engine


SQLITE_URL = "sqlite:///database.db"
connect_args = {"check_same_thread": False}
ENGINE = create_engine(SQLITE_URL, connect_args=connect_args)


def get_session():
    """
    Création de la dépendance à FastAPI
    """
    with Session(ENGINE) as session:
        yield session


def create_db_and_tables():
    """Crée la DB"""
    SQLModel.metadata.create_all(ENGINE)

from sqlmodel import Field, SQLModel

class Quote(SQLModel, table=True):
    """
    Modèle représentant une citation
    """
    citation: str
    id: int | None = Field(default=None, primary_key=True)

from pydantic import BaseModel


class Quote(BaseModel):
    """
    Modèle représentant une citation
    """

    citation: str

"""Import"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root() -> (
    dict
):  # On essaie d'être le plus rigoureux possible, on documente le tout !!
    """
    Définie le contenue (simple) de ma page en format json
    """
    return {"message": "Hello World"}

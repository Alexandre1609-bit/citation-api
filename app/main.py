from fastapi import FastAPI
from typing import Dict

app = FastAPI()

@app.get("/")
async def root() -> dict: #On essaie d'être le plus rigoureux possible, on documente le tout !!
    return {"message": "Hello World"}
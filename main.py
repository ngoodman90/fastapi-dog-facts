import fastapi

import models

import service

app = fastapi.FastAPI(docs_url="/api/docs")

DOG_FACTS_URL = "https://dog-api.kinduff.com/api/facts"


@app.get("/api/v1/facts", response_model=models.DogFactResponse)
async def get_fact() -> models.DogFactResponse:
    fact = await service.get_fact()
    return models.DogFactResponse(fact=fact)

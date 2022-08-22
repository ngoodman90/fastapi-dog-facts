import fastapi


from cats import service, models

router = fastapi.APIRouter(prefix="/api/v1/cats", tags=["Cats"])


@router.get("/facts", response_model=models.CatFactResponse)
async def get_fact() -> models.CatFactResponse:
    fact = await service.get_fact()
    return models.CatFactResponse(fact=fact)

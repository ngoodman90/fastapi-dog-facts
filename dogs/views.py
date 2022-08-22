import fastapi


from dogs import service, models

router = fastapi.APIRouter(prefix="/api/v1/dogs", tags=["Dogs"])

DOG_FACTS_URL = "https://dog-api.kinduff.com/api/facts"


@router.get("/facts", response_model=models.DogFactResponse)
async def get_fact() -> models.DogFactResponse:
    fact = await service.get_fact()
    return models.DogFactResponse(fact=fact)

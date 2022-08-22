import aiohttp
import fastapi

from cats import models

CAT_FACTS_URL = "https://dog-api.kinduff.com/api/facts"


async def get_fact() -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(CAT_FACTS_URL) as response:
            if not response.ok:
                raise fastapi.HTTPException(status_code=response.status)

            response_json = await response.json()
            parsed_response = models.CatFactApiResponse.parse_obj(response_json)
            if not parsed_response.facts:
                raise fastapi.HTTPException(
                    status_code=fastapi.status.HTTP_404_NOT_FOUND,
                    detail="No cat facts found",
                )

            return parsed_response.facts[0]

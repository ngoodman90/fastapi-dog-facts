from typing import List

import pydantic


class CatFactResponse(pydantic.BaseModel):
    fact: str


class CatFactApiResponse(pydantic.BaseModel):
    facts: List[str]
    success: bool

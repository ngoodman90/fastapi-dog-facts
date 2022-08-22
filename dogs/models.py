from typing import List

import pydantic


class DogFactResponse(pydantic.BaseModel):
    fact: str


class DogFactApiResponse(pydantic.BaseModel):
    facts: List[str]
    success: bool

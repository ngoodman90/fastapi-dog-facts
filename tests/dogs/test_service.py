import pytest

from dogs import service


@pytest.mark.asyncio
async def test_get_fact():
    fact = await service.get_fact()
    assert fact


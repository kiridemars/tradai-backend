from fastapi import HTTPException

from app.schemas import ScreenerResponse


def _not_impl(market: str) -> ScreenerResponse:
    raise HTTPException(status_code=501, detail=f"provider '{market}' not implemented")


def us_losers() -> ScreenerResponse:
    return _not_impl("us")


def kr_losers() -> ScreenerResponse:
    return _not_impl("kr")


def eu_losers() -> ScreenerResponse:
    return _not_impl("eu")

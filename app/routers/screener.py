from fastapi import APIRouter, Query

from app import providers
from app.schemas import ScreenerResponse

router = APIRouter(prefix="/screener", tags=["screener"])


@router.get("/losers", response_model=ScreenerResponse)
def losers(market: str = Query(..., pattern="^(us|kr|eu)$")):
    fn = {
        "us": providers.us_losers,
        "kr": providers.kr_losers,
        "eu": providers.eu_losers,
    }[market]
    return fn()

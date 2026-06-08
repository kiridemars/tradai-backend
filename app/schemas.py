from pydantic import BaseModel


class Loser(BaseModel):
    symbol: str
    name: str
    price: float
    change_pct: float


class ScreenerResponse(BaseModel):
    market: str
    losers: list[Loser]

from fastapi import FastAPI

from app.routers import screener

app = FastAPI(title="TradAI Backend")


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(screener.router)

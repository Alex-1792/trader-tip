"""
Entrypoint for FastAPI.
"""

from fastapi import FastAPI
from trader_tip.api import news

app = FastAPI(title="Stock News API")

app.include_router(news.router, prefix="/news", tags=["news"])

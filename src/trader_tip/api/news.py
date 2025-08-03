"""
/news endpoint to fetch articles based on the query word provided.
"""

from fastapi import APIRouter, Query
from typing import List
from trader_tip.models.news import Article
from trader_tip.services.news_service import fetch_news_articles

router = APIRouter()

@router.get("/", response_model=List[Article])
async def get_news(query: str = Query(..., description="Keyword to search for")):
    """
    Fetch latest news articles for a given query word.
    """
    return fetch_news_articles(query)

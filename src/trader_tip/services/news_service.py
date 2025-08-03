"""
Logic for fetching and parsing news articles.
"""


import feedparser
from datetime import datetime
from trader_tip.models.news import Article

def fetch_news_articles(query: str):
    """
    Fetch articles from Google News RSS for a given query.
    """
    feed_url = f"https://news.google.com/rss/search?q={query}"
    feed = feedparser.parse(feed_url)

    articles = []
    for entry in feed.entries:
        published = None
        try:
            published = datetime(*entry.published_parsed[:6])
        except:
            published = datetime.now()

        articles.append(Article(
            title=entry.title,
            link=entry.link,
            published=published
        ))

    return articles

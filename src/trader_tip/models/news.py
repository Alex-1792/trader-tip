"""
Models for the news endpoint.
"""

from pydantic import BaseModel
from datetime import datetime

class Article(BaseModel):
    title: str
    link: str
    published: datetime

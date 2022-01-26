from typing import Optional
from pydantic import BaseModel


class Article(BaseModel):
    id: Optional[str]
    title: str
    url: str
    imageUrl: str
    newsSite: str
    summary: str
    publishedAt: str
    updatedAt: str
    featured: bool
    launches: Optional[list]
    events: Optional[list]



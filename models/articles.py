from typing import Optional
from pydantic import BaseModel, Field


class ArticleIn(BaseModel):
    title: str
    url: str
    imageUrl: str
    newsSite: str
    summary: str
    publishedAt: str
    updatedAt: str
    featured: bool
    launches: Optional[list] = Field([{'id': "string", 'provider': "string"}])
    events: Optional[list] = Field([{'id': "string", 'provider': "string"}])


class ArticleOut(BaseModel):
    mongo_id: Optional[str] = Field(alias='_id')
    id: Optional[int] = Field(alias='id')
    title: str
    url: str
    imageUrl: str
    newsSite: str
    summary: str
    publishedAt: str
    updatedAt: str
    featured: bool
    launches: Optional[list] = Field([{'id': "string", 'provider': "string"}])
    events: Optional[list] = Field([{'id': "string", 'provider': "string"}])


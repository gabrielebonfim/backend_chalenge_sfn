from typing import List

from fastapi import APIRouter, Response, status
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

from models.articles import ArticleIn, ArticleOut
from settings.db import COLLECTIONS
from schemas.articles import articles_entity, article_entity

ARTICLE = APIRouter()
COLLECTION = COLLECTIONS["articles"]


@ARTICLE.get('/articles', response_model=List[ArticleOut], tags=["articles"])
def get_all_articles():
    return articles_entity(COLLECTION.find())


@ARTICLE.get('/articles/{_id}', response_model=ArticleOut, tags=["articles"])
def get_article_by_id(id: str):
    article = COLLECTION.find_one({"_id": ObjectId(id)})
    return article_entity(article)


@ARTICLE.post('/articles', response_model=ArticleOut, tags=["articles"])
def add_new_article(article: ArticleIn):
    new_article = dict(article)
    new_article["id"] = None
    article_in = COLLECTION.insert_one(new_article).inserted_id
    article_out = COLLECTION.find_one({"_id": article_in})
    return article_entity(article_out)


@ARTICLE.put('/articles/{_id}', response_model=ArticleOut, tags=["articles"])
def update_article(id: str, article: ArticleIn):
    COLLECTION.find_one_and_update({
        "_id": ObjectId(id)
    }, {
        "$set": dict(article)
    })
    return article_entity(COLLECTION.find_one({"_id": ObjectId(id)}))


@ARTICLE.delete('/articles/{_id}', status_code=status.HTTP_204_NO_CONTENT, tags=["articles"])
def delete_article(id: str):
    COLLECTION.find_one_and_delete({
        "_id": ObjectId(id)
    })
    return Response(status_code=HTTP_204_NO_CONTENT)

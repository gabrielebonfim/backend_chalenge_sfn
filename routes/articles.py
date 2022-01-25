from fastapi import APIRouter

article = APIRouter()


@article.get('/articles')
def get_all_articles():
    return 'hello_world'


@article.get('/articles/{id}')
def get_article_by_id():
    return 'hello_world'


@article.post('/articles')
def add_new_article():
    return 'hello_world'


@article.put('/articles/{id}')
def update_article():
    return 'hello_world'


@article.delete('/articles/{id}')
def delete_article():
    return 'hello_world'



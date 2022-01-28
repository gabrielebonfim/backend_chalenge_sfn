from cron.scheduler import start
from restore_data.restore_data import RestoreData
from schemas.articles import articles_entity
from settings.db import COLLECTIONS


def update_articles(hour: int):
    collection = COLLECTIONS['articles']
    url = 'https://api.spaceflightnewsapi.net/v3/articles'
    job = RestoreData(collection, url).restore_last
    return start(job, hour)

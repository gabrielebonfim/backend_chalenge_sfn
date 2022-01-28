from fastapi import FastAPI

from restore_data.restore_data import RestoreData
from routes.root import ROOT
from routes.articles import ARTICLE
from settings.db import COLLECTIONS

APP = FastAPI()


API_ROUTES = [
    APP.include_router(ROOT),
    APP.include_router(ARTICLE)
]


"""
Restoring the data from Space Flight News API for the first time.
Restaurando os dados do Space Flight News API pela primeira vez.
"""
ARTICLES = RestoreData(COLLECTIONS["articles"], 'https://api.spaceflightnewsapi.net/v3/articles').restore()


"""
CRON
Initizalized at 9:00AM (UTC-3) every day to update data.
Inicializado às 9:00AM (UTC-3) todos os dias para atualizar os dados.
"""

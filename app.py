from fastapi import FastAPI

from cron.tasks import update_articles
from restore_data.restore_data import RestoreData
from routes.root import ROOT
from routes.articles import ARTICLE
from settings.db import COLLECTIONS

APP = FastAPI(
    title='Back-end Challenge 🏅 2021 - Space Flight News 🇧🇷',
    description='A Rest API created using data from Space Flight News API. | '
                'Uma API Rest criada usando dados da API Space Flight News. '
                'Created by Gabriele Alves.',
    version='0.0.1',
    contact={
        "name": "Repository",
        "url":  "https://github.com/gabrielebonfim/backend_chalenge_sfn",
    }
)

API_ROUTES = [
    APP.include_router(ROOT),
    APP.include_router(ARTICLE)
]

"""
Restoring the data from Space Flight News API for the first time.
Restaurando os dados do Space Flight News API pela primeira vez.
"""

ARTICLES = RestoreData(COLLECTIONS["articles"], 'https://api.spaceflightnewsapi.net/v3/articles').restore_all()

"""
CRON
Initizalized at 9:00AM (UTC-3) every day to update data.
Inicializado às 9:00AM (UTC-3) todos os dias para atualizar os dados.
"""

CRON_JOBS = [
    update_articles(9)
]

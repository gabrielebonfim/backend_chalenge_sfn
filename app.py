from fastapi import FastAPI
from routes.articles import article
from restore_data.utils import restore_data_from_api

app = FastAPI()

"""
API ROUTES
"""

app.include_router(article)


"""
Restoring the data from Space Flight News API for the first time.
Restaurando os dados do Space Flight News API pela primeira vez.
"""
url = 'https://api.spaceflightnewsapi.net/v3/articles'
restore_data_from_api(url)


"""
CRON
Initizalized at every 9 hours to update data.
Inicializado a cada 9 horas para atualizar os dados.
"""
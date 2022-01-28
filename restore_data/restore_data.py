import requests

from schemas.articles import articles_entity
from settings import db


def __validate_first_import():
    count_docs = db.collection.count_documents({})
    return count_docs == 0


def __change_id_field():
    """
    This function change the field 'id' to 'id_original'. This field is the reference
    for the cron to get new documents from the original API.

    Esta função altera o campo 'id' para 'id_original'. Este campo é a referência para
    que o cron atualize a coleção com novos documentos contidos na API original.
    """
    data = articles_entity(db.collection.find())
    for i in range(len(data)):
        data[i]["id"] = data[i]["id_original"]


def restore_data_from_api(api_url):
    if __validate_first_import():
        data = requests.get(api_url).json()
        return db.collection.insert_many(data)


if __name__ == "__main__":
    __change_id_field()
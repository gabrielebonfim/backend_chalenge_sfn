import requests
from settings import db


def __validate_first_import():
    count_docs = db.collection.count_documents({})
    return count_docs == 0


def restore_data_from_api(api_url):
    if __validate_first_import():
        data = requests.get(api_url).json()
        return db.collection.insert_many(data)


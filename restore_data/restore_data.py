import requests


class RestoreData:
    def __init__(self, collection, api_url):
        self.collection = collection
        self.api_url = api_url

    def __validate_first_import(self):
        count_docs = self.collection.count_documents({})
        return count_docs == 0

    def restore(self):
        if self.__validate_first_import():
            data = requests.get(self.api_url).json()
            return self.collection.insert_many(data)

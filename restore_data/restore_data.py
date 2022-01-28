from operator import itemgetter
import requests


class RestoreData:
    def __init__(self, collection, api_url, schema=None):
        self.collection = collection
        self.json = requests.get(api_url).json()
        self.schema = schema

    def __validate_first_import(self):
        count_docs = self.collection.count_documents({})
        return count_docs == 0

    def restore_all(self):
        if self.__validate_first_import():
            return self.collection.insert_many(self.json)

    def restore_last(self):
        json_sorted = sorted(self.json, key=itemgetter('id'))

        def get_json_position():
            last_original_id = self.schema(self.collection.find().sort("id", -1).limit(1))[0]["id"]
            for i in range(0, len(json_sorted)):
                if json_sorted[i]["id"] == last_original_id:
                    position = i + 1
                    return position

        new_documents = [json_sorted[i] for i in range(get_json_position(), len(json_sorted))]
        if new_documents:
            return self.collection.insert_many(new_documents)

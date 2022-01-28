import pymongo

"""
THIS PROJECT ONLY SUPORTS MONGODB CONNECTION | ESTE PROJETO SUPORTA APENAS CONEXÃO COM MONGODB
"""

"""
CONN
Example:
'mongodb+srv://<USER>:<PASSWORD>@<CLUSTER>.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
"""

CONN = None

CLIENT = pymongo.MongoClient(CONN, serverSelectionTimeoutMS=5000)

""" 
DATABASE
Example:
DATABASE = CLIENT.<database_name>
"""

DATABASE = None

COLLECTIONS = {
    """
    COLLECTIONS
    Example:
    "<collection_name>": DATABASE.<collection_name>,
    """
    
    "articles": None
}

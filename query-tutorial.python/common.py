DB_HOST='localhost'
DB_NAME='nn'

from pymongo import MongoClient
client = MongoClient('mongodb://{}:27017/'.format(DB_HOST), connect=False)
db = client[DB_NAME]


def mongo_print(query_cursor, pretty=True):
    r = query_cursor; r=list(r)
    if pretty:
        from pprint import pprint
        pprint(r)
    else:
        print(r)

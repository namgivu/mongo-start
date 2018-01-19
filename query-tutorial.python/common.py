DB_HOST='localhost'
DB_NAME='nn'

from pymongo import MongoClient
client = MongoClient('mongodb://{}:27017/'.format(DB_HOST), connect=False)
db = client[DB_NAME]


def mongo_print(query_cursor, count=False, pretty=False):
    r = query_cursor; r=list(r)
    if pretty:
        from pprint import pprint
        pprint(r)
    else:
        docs=r
        for d in docs: print(d)

    #print found count
    if count:
        print('Found {}'.format(len(r)) )

    #a blank line at the end as ending separator
    print()


def exit():
    print('Exited on purpose')
    import sys; sys.exit()

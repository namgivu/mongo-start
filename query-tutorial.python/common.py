DB_HOST='localhost'
DB_NAME='nn'

from pymongo import MongoClient
client = MongoClient('mongodb://{}:27017/'.format(DB_HOST), connect=False)
db = client[DB_NAME]


#region printing

def mongo_print(query_cursor, count=False, pretty=False):

    #region print query result
    from pymongo.cursor import Cursor
    from pymongo.command_cursor import CommandCursor

    is_cursor = type(query_cursor) is Cursor or \
                type(query_cursor) is CommandCursor
    is_dict   = type(query_cursor) is dict

    if False: pass

    elif is_cursor:
        _mongo_print_cursor(query_cursor, count, pretty)
    elif is_dict:
        _mongo_print_dict(query_cursor, count, pretty)

    else: raise Exception('Unsupported query_cursor type {}'.format(type(query_cursor)))
    #endregion print query result

    #print found count
    if is_cursor: #only print count when NOT a list/cursor
        if count:
            print('Found {}'.format(len(list(query_cursor))) )

    #a blank line at the end as ending separator
    print()


def _mongo_print_cursor(query_cursor, count=False, pretty=False):
    docs = list(query_cursor)
    for d in docs: _mongo_print_dict(d, count, pretty)
    if len(docs)<=0: print('(nothing found)')


from pprint import pprint
def _mongo_print_dict(query_cursor, count=False, pretty=False):
    d = query_cursor #d i.e. a dict
    if pretty: pprint(d)
    else:      print(d)

#endregion printing


def halt():
    print('Exited on purpose')
    import sys; sys.exit()

from datetime import datetime

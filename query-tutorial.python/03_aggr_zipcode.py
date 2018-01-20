from common import *

db.zipcodes.delete_many({}) #clear all first

##do seeding
db.zipcodes.insert_many([
  {
    "_id": "10280", "state": "NY", "city": "NEW YORK",
    "loc": [-74.016323,40.710537], "pop":   5574,
  },

  {
    "_id": "122333", "state": "AA", "city": "CCC DEE",
    "loc": [-11.016323,33.710537], "pop":   122333,
  },

])

#output
mongo_print(query_cursor=db.users.find())


##start query ref. https://docs.mongodb.com/manual/tutorial/aggregation-zip-code-data-set/

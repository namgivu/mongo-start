from common import *

db.users.delete_many({}) #clear all first

##do seeding
db.users.insert_many([
    {
      "_id"    : "ruby han",
      "joined" : datetime.strptime("2016-04-04", "%Y-%d-%M"),
      "likes"  : ["youtube for kids"],
    },

    {
      "_id"    : "jane",
      "joined" : datetime.strptime("2011-03-02", "%Y-%d-%M"),
      "likes"  : ["golf", "racquetball"],
    },

    {
      "_id"    : "joe",
      "joined" : datetime.strptime("2012-07-02", "%Y-%d-%M"),
      "likes"  : ["tennis", "golf", "swimming"],
    },

])

#output
mongo_print(query_cursor=db.users.find())


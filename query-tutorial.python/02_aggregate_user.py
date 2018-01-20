from common import *

db.users.delete_many({}) #clear all first

##do seeding
db.users.insert_many([
    {
      "_id"    : "ruby han",
      "joined" : datetime.strptime("2016-04-04", "%Y-%m-%d"),
      "likes"  : ["youtube for kids"],
    },

    {
      "_id"    : "jane",
      "joined" : datetime.strptime("2011-01-02", "%Y-%m-%d"),
      "likes"  : ["golf", "racquetball"],
    },

    {
      "_id"    : "joe",
      "joined" : datetime.strptime("2012-06-08", "%Y-%m-%d"),
      "likes"  : ["tennis", "golf", "swimming"],
    },

    {
      "_id"    : "jill",
      "joined" : datetime.strptime("2012-06-02", "%Y-%m-%d"),
      "likes"  : ["tennis", "golf", "swimming"],
    },
    {
      "_id"    : "jack",
      "joined" : datetime.strptime("2012-06-02", "%Y-%m-%d"),
      "likes"  : ["tennis", "golf", "swimming"],
    },

])

#output
mongo_print(query_cursor=db.users.find())


##start query ref. https://docs.mongodb.com/manual/tutorial/aggregation-with-user-preference-data/

qc=qc=db.users.find(); mongo_print(qc)

p=[{ "$project": { "_id":0                              }}  ]; qc=db.users.aggregate(p); mongo_print(qc)
p=[{ "$project": { "_id":0, "name":{"$toUpper":"$_id"}  }}  ]; qc=db.users.aggregate(p); mongo_print(qc)
p=[{ "$project": { "_id":0, "name":{"$toUpper":"$_id"}  }},
   { "$sort" :   { "name":1                             }},
]; qc=db.users.aggregate(p); mongo_print(qc)

#ordered by join month
p=[{ "$project": { "_id":0, "name":"$_id", "month_joined":{"$month" : "$joined"}  }},
   { "$sort" :   { "month_joined":1  }},
]; qc=db.users.aggregate(p); mongo_print(qc)

#total number of joins per month/year
p=[{ "$project": { "month_joined": {"$month": "$joined"}  }},
   { "$group":   { "_id": {"month_joined": "$month_joined"}, "qty": {"$sum": 1}  }},
   { "$sort":    { "_id.month_joined": 1  }},
   ]; qc=db.users.aggregate(p); mongo_print(qc)

p=[{ "$project": { "yyyy": {"$year": "$joined"}  }},
   { "$group":   { "_id": {"yyyy": "$yyyy"}, "qty": {"$sum": 1}  }},
   { "$sort":    { "_id.yyyy": 1  }},
   ]; qc=db.users.aggregate(p); mongo_print(qc)

#top 2 common likes
p=[{ "$unwind": "$likes" },
   { "$group":  { "_id": "$likes", "qty": {"$sum": 1}  }},
   { "$sort":   { "qty": -1  }},
   { "$limit":  2 },
   ]; qc=db.users.aggregate(p); mongo_print(qc)

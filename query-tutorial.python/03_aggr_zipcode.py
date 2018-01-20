from common import *

db.zipcodes.delete_many({}) #clear all first

##do seeding
db.zipcodes.insert_many([
  {
    "_id":   "10280",
    "state": "NY",
    "city":  "NEW YORK",
    "loc":   [-74.016323,40.710537],
    "pop":   5574,
  },

  {
    "_id":   "1801201024",
    "state": "AA",
    "city":  "CCC DEE",
    "loc":   [-11.016323,33.710537],
    "pop":   122000,
  },

  {
    "_id":   "1801201025",
    "state": "AA",
    "city":  "B CCC",
    "loc":   [-11.016323,33.710537],
    "pop":   333,
  },

])

#output
mongo_print(query_cursor=db.zipcodes.find())


##start query ref. https://docs.mongodb.com/manual/tutorial/aggregation-zip-code-data-set/
qc=db.zipcodes.find(); mongo_print(qc)

#states that have population more than 10000
p=[{"$group":{ "_id":      {"state":"$state"},
               "totalPop": {"$sum": "$pop"},
             }},
]; qc=db.zipcodes.aggregate(p); mongo_print(qc)

p=[{"$group": { "_id":     {"state":"$state"},
                "totalPop": {"$sum": "$pop"},
              }},
   {"$match": {"totalPop": {"$gte": 10000}  }},
]; qc=db.zipcodes.aggregate(p); mongo_print(qc)

p=[{"$group": { "_id": "$state", "totalPop": {"$sum": "$pop"} }},
   {"$match": {"totalPop": {"$gte": 10000}  }},
]; qc=db.zipcodes.aggregate(p); mongo_print(qc)

#average city population by state
p=[{"$group": { "_id": {"state":"$state"}, "totalPop": {"$sum": "$pop"} }},
]; qc=db.zipcodes.aggregate(p); mongo_print(qc)

p=[{"$group": { "_id": {"state":"$state"}, "totalPop": {"$sum": "$pop"} }},
   {"$group": { "_id": "$_id.state",        "avgPop":  {"$avg": "$totalPop"} }},
]; qc=db.zipcodes.aggregate(p); mongo_print(qc)

p=[{"$group": { "_id": {"state":"$state"}, "totalPop": {"$sum": "$pop"} }},
   {"$group": { "_id": "$_id.state",        "avgPop":  {"$avg": "$totalPop"} }},
   {"$sort":  { "_id": 1 }},
]; qc=db.zipcodes.aggregate(p); mongo_print(qc)



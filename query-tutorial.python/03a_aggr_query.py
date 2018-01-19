from common import *

##start here ref. https://docs.mongodb.com/manual/tutorial/aggregation-with-user-preference-data/

qc=qc=db.users.find(); mongo_print(qc)

p=[{ "$project": { "_id":0                              }}  ]; qc=db.users.aggregate(p); mongo_print(qc)
p=[{ "$project": { "_id":0, "name":{"$toUpper":"$_id"}  }}  ]; qc=db.users.aggregate(p); mongo_print(qc)
p=[{ "$project": { "_id":0, "name":{"$toUpper":"$_id"}  }},
   { "$sort" :   { "name":1                             }},
]; qc=db.users.aggregate(p); mongo_print(qc)

from common import *

##start here ref. https://docs.mongodb.com/manual/tutorial/aggregation-with-user-preference-data/

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


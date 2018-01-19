from common import *

##start here ref. https://docs.mongodb.com/manual/tutorial/query-documents/

#all
qc=db.inventory.find()          ; mongo_print(qc)
qc=db.inventory.find_one()      ; mongo_print(qc)
qc=db.inventory.find().limit(1) ; mongo_print(qc)

#in
qc=db.inventory.find({"status": "some invalid status"}); mongo_print(qc)
qc=db.inventory.find({"status": "D"                  }); mongo_print(qc)
qc=db.inventory.find({"status": {"$in": ["A", "D"]}  }); mongo_print(qc)

#compare
qc=db.inventory.find({"qty": 50           }); mongo_print(qc)
qc=db.inventory.find({"qty": {"$lt": 50}  }); mongo_print(qc)
qc=db.inventory.find({"qty": {"$lte": 50} }); mongo_print(qc)
qc=db.inventory.find({"qty": {"$lte": 50, "$gte": 40} }); mongo_print(qc)

print('query180119-1200') #a timestamp marker when we have reached many enough queries

#and, or
qc=db.inventory.find({         "status": "A"                         }); mongo_print(qc)
qc=db.inventory.find({         "status": "A",   "qty": {"$lt": 50}   }); mongo_print(qc)
qc=db.inventory.find({"$or": [{"status": "A"}, {"qty": {"$lt": 50}}] }); mongo_print(qc)
qc=db.inventory.find({"$or": [{"status": "A"},
                              {"qty": {"$lt": 50}},
                              ]                                      }); mongo_print(qc)

#regex
qc=db.inventory.find({"status": "A"}); mongo_print(qc)
qc=db.inventory.find({"status": "A", "item": {"$regex": "^p"} }); mongo_print(qc)

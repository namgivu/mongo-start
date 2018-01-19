from common import *

##start here ref. https://docs.mongodb.com/manual/tutorial/query-documents/

#all
qc=db.inventory.find(); mongo_print(qc)

#in
qc=db.inventory.find({"status": "D"                 }); mongo_print(qc)
qc=db.inventory.find({"status": {"$in": ["A", "D"]} }); mongo_print(qc)

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


##further read point ref. https://docs.mongodb.com/manual/tutorial/query-documents/#additional-query-tutorials

#field.nested_field
qc=db.inventory.find({"size.uom": "cm"}); mongo_print(qc)
qc=db.inventory.find({"size.uom": "cm", "size.h": {"$lte": 10} }); mongo_print(qc)

#data as array
print('query180119-1400') #a timestamp marker when we have reached many enough queries
qc = db.inventory.find({"tags":          ["red", "blank"]   }); mongo_print(qc) #an array with exactly two elements, "red" and "blank" in the specific order
qc = db.inventory.find({"tags": {"$all": ["red", "blank"]}  }); mongo_print(qc) #an array with exactly two elements, "red" and "blank" regardless to the order
qc = db.inventory.find({"tags": {"$all": ["red"]}           }); mongo_print(qc) #an array with exactly two elements, "red" and "blank" regardless to the order
qc = db.inventory.find({"tags":           "red"             }); mongo_print(qc) #an array with exactly two elements, "red" and "blank" regardless to the order

#further on array data ref. https://docs.mongodb.com/manual/tutorial/query-arrays/#query-for-an-array-element-that-meets-multiple-criteria


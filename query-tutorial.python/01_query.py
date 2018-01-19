from common import *

##start here ref. https://docs.mongodb.com/manual/tutorial/query-documents/

#all
qc=db.inventory.find(); mongo_print(qc)

#in
qc=db.inventory.find({"status": "D"                 }); mongo_print(qc)
qc=db.inventory.find({"status": {"$in": ["A", "D"]} }); mongo_print(qc)

#compare
qc=db.inventory.find({"qty": 50          }); mongo_print(qc)
qc=db.inventory.find({"qty": {"$lt": 50} }); mongo_print(qc)
qc=db.inventory.find({"qty": {"$lte": 50} }); mongo_print(qc)

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

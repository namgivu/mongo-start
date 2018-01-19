from common import *

#ref. https://docs.mongodb.com/manual/tutorial/query-documents/#additional-query-tutorials
pass

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
pass

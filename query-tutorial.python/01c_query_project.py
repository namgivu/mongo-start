from common import *

#ref. https://docs.mongodb.com/manual/tutorial/project-fields-from-query-results/
"""use **project** to specify or restrict fields to return"""

qc=db.inventory.find({"status": "A"}                                                ); mongo_print(qc, count=True)
qc=db.inventory.find({"status": "A"}, {"_id":0}                                     ); mongo_print(qc) #all but _id
qc=db.inventory.find({"status": "A"}, {"item":1, "status":1}                        ); mongo_print(qc) #item, status only
qc=db.inventory.find({"status": "A"}, {"item":1, "status":1, "_id":0}               ); mongo_print(qc) #item, status only, excluding _id
qc=db.inventory.find({"status": "A"}, {"item":1, "status":1, "_id":0, "size.uom":1} ); mongo_print(qc)

from common import *

qc=db.inventory.find(); mongo_print(query_cursor=qc)
qc=db.inventory.find({"status": "D"                 }); mongo_print(query_cursor=qc)
qc=db.inventory.find({"status": {"$in": ["A", "D"]} }); mongo_print(query_cursor=qc)

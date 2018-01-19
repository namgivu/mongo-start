from common import *

qc=db.inventory.find(); mongo_print(query_cursor=qc, pretty=False)
print()
qc=db.inventory.find({"status": "D"}); mongo_print(query_cursor=qc, pretty=False)

from common import *

db.sandbox.delete_many({}) #clear all first

##do seeding
ts=datetime.strptime('2018-01-01 00:00:00','%Y-%m-%d %H:%M:%S')
tsAll=[
  {'ts': ts},
]
db.sandbox.insert_many(tsAll)

#output
p=[
  {'$project': {
    #'result': {'$divide': ['$ts', 1]},
    'result' : {'$divide': [{'$millisecond':'$ts'},1] },
  }},
  {'$project': {'_id' : 0,'ts' : 0} },
]; qc=db.sandbox.aggregate(p); mongo_print(qc, pretty=False)

# 'xx': {'$divide': ['$ts', SAMPLING_THRESHOLD]},

from common import *

db.sandbox.delete_many({}) #clear all first

##do seeding
tsAll=[
  {'group':'g1','value':'2'},
  {'group':'g1','value':'1'},
  {'group':'g1','value':'3'},

  {'group':'g2','value':'b'},
  {'group':'g2','value':'a'},
  {'group':'g2','value':'c'},
]
db.sandbox.insert_many(tsAll)

#output
p=[
  {'$sort':{'value':1} },
  {'$group': {
    '_id':{'g':'$group'},
    '1st_value':{'$first' :'$value'},
    '2nd_value':{'$second':'$value'}, #TODO get n-th doc ref. https://stackoverflow.com/q/39079496/248616
  }},
  # {'$project': {'_id' : 0} },
]; qc=db.sandbox.aggregate(p); mongo_print(qc, pretty=False)

# 'xx': {'$divide': ['$ts', SAMPLING_THRESHOLD]},

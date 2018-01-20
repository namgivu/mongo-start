from common import *

db.zipcodes.delete_many({}) #clear all first

##do seeding
db.zipcodes.insert_many([
  {
    '_id':   '1801201100',
    'state': 'NY',
    'city':  'NEW YORK',
    'loc':   [-74.016323,40.710537],
    'pop':   5574,
  },

  {
    '_id':   '1801201101',
    'state': 'NY',
    'city':  'MIN CITY',
    'loc':   [-74.016323,40.710537],
    'pop':   1111,
  },

  {
    '_id':   '1801201102',
    'state': 'NY',
    'city':  'MAX CITY',
    'loc':   [-74.016323,40.710537],
    'pop':   9999,
  },

  {
    '_id':   '1801201024',
    'state': 'AA',
    'city':  'CCC DEE',
    'loc':   [-11.016323,33.710537],
    'pop':   122000,
  },

  {
    '_id':   '1801201025',
    'state': 'AA',
    'city':  'B CCC',
    'loc':   [-11.016323,33.710537],
    'pop':   333,
  },

  {
    '_id':   '1801201026',
    'state': 'AA',
    'city':  'B CCC',
    'loc':   [-11.01,33.03],
    'pop':   22,
  },

])

#output
mongo_print(query_cursor=db.zipcodes.find())


##start query ref. https://docs.mongodb.com/manual/tutorial/aggregation-zip-code-data-set/
qc=db.zipcodes.find(); mongo_print(qc)

#states that have population more than 10000
p=[{'$group':{ '_id':      {'state':'$state'},
               'totalPop': {'$sum': '$pop'},
             }},
]; qc=db.zipcodes.aggregate(p); mongo_print(qc)

p=[{'$group': { '_id':     {'state':'$state'},
                'totalPop': {'$sum': '$pop'},
              }},
   {'$match': {'totalPop': {'$gte': 10000}  }},
]; qc=db.zipcodes.aggregate(p); mongo_print(qc)

p=[{'$group': { '_id': '$state', 'totalPop': {'$sum': '$pop'} }},
   {'$match': {'totalPop': {'$gte': 10000}  }},
]; qc=db.zipcodes.aggregate(p); mongo_print(qc)

#average city population by state
p=[{'$group': { '_id': {'state':'$state'}, 'totalPop': {'$sum': '$pop'} }},
]; qc=db.zipcodes.aggregate(p); mongo_print(qc)

p=[{'$group': { '_id': {'state':'$state'}, 'totalPop': {'$sum': '$pop'} }},
   {'$group': { '_id': '$_id.state',        'avgPop':  {'$avg': '$totalPop'} }},
]; qc=db.zipcodes.aggregate(p); mongo_print(qc)

p=[{'$group': { '_id': {'state':'$state'}, 'totalPop': {'$sum': '$pop'} }},
   {'$group': { '_id': '$_id.state',        'avgPop':  {'$avg': '$totalPop'} }},
   {'$sort':  { '_id': 1 }},
]; qc=db.zipcodes.aggregate(p); mongo_print(qc)

#largest and smallest (in population) cities of each state
p=[{'$group': { '_id':     {'state':'$state', 'city':'$city'},
                'cityPop': {'$sum': '$pop'},
              }},
]; qc=db.zipcodes.aggregate(p); mongo_print(qc)
p=[{'$group': { '_id':     {'state':'$state', 'city':'$city'},
                'cityPop': {'$sum': '$pop'},
              }},
   {'$sort': { 'cityPop': 1} },
 ]; qc=db.zipcodes.aggregate(p); mongo_print(qc)

p=[{'$group': { '_id':     {'state':'$state', 'city':'$city'},
                'cityPop': {'$sum': '$pop'},
              }},
   {'$sort': { 'cityPop': 1} },
   {'$group': { '_id':  {'state':'$_id.state'},
                'minCity': {'$first': '$_id.city'}, 'minCityPop': {'$first': '$cityPop'},
                'maxCity': {'$last':  '$_id.city'}, 'maxCityPop': {'$last':  '$cityPop'},
              }},
]; qc=db.zipcodes.aggregate(p); mongo_print(qc)

p=[{'$group': { '_id':     {'state':'$state', 'city':'$city'},
                'cityPop': {'$sum': '$pop'},
              }},
   {'$sort': { 'cityPop': 1} },
   {'$group': { '_id':  {'state':'$_id.state'},
                'minCity': {'$first': '$_id.city'}, 'minCityPop': {'$first': '$cityPop'},
                'maxCity': {'$last':  '$_id.city'}, 'maxCityPop': {'$last':  '$cityPop'},
              }},
   {'$project': { 'state':        '$_id.state',
                  'largestCity':  {'name':'$maxCity', 'pop':'$maxCityPop'},
                  'smallestCity': {'name':'$minCity', 'pop':'$minCityPop'},
                }},
]; qc=db.zipcodes.aggregate(p); mongo_print(qc)


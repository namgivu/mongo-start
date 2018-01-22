from common import *

db.sandbox.delete_many({}) #clear all first

##do seeding
ts=datetime.strptime('2018-01-01 00:00:00','%Y-%m-%d %H:%M:%S')
tsAll=[
  {'ts': ts},

  {'ts': ts + relativedelta(seconds=10)},
  {'ts': ts + relativedelta(seconds=11)},
  {'ts': ts + relativedelta(seconds=12)},

  {'ts': ts + relativedelta(seconds=20)},
  {'ts': ts + relativedelta(seconds=21)},
  {'ts': ts + relativedelta(seconds=22)},

  {'ts': ts + relativedelta(seconds=30)},
  {'ts': ts + relativedelta(seconds=40)},
  {'ts': ts + relativedelta(seconds=50)},
  {'ts': ts + relativedelta(seconds=60)},

  {'ts': ts + relativedelta(days=1)},
  {'ts': ts + relativedelta(days=1,seconds=10)},
  {'ts': ts + relativedelta(days=1,seconds=20)},
  {'ts': ts + relativedelta(days=1,seconds=30)},
  {'ts': ts + relativedelta(days=1,seconds=40)},
  {'ts': ts + relativedelta(days=1,seconds=50)},
  {'ts': ts + relativedelta(days=1,seconds=60)},

  {'ts': ts + relativedelta(days=364)},
  {'ts': ts + relativedelta(days=364,seconds=10)},
  {'ts': ts + relativedelta(days=364,seconds=20)},
  {'ts': ts + relativedelta(days=364,seconds=30)},
  {'ts': ts + relativedelta(days=364,seconds=40)},
  {'ts': ts + relativedelta(days=364,seconds=50)},
  {'ts': ts + relativedelta(days=364,seconds=60)},
]
i=0
for t in tsAll:
  t.update(id=i); i+=1
db.sandbox.insert_many(tsAll)

#output
ONE_SECOND = 1
ONE_MINUTE = 60*ONE_SECOND
ONE_HOUR   = 60*ONE_MINUTE
SAMPLING_THRESHOLD = 20*ONE_SECOND
p=[
  {'$project': {
    'ts': '$ts',
    'id': '$id',
    'parts': {
      'year'   : {'$year': '$ts'},
      'doy'    : {'$dayOfYear': '$ts'},
      'hour'   : {'$hour': '$ts'},
      'minute' : {'$minute': '$ts'},
      'second' : {'$second': '$ts'},
    },
  }},

  {'$project': {
    'ts': '$ts',
    'id': '$id',

    'year_doy': {
      '$concat':[
        {'$substrBytes': ['$parts.year',0,-1] },
        '_',
        {'$substrBytes': ['$parts.doy',0,-1] },
      ]
    },

    'sod': {  # seconds of day
      '$add': [
        {'$multiply': ['$parts.hour', ONE_HOUR]},
        {'$multiply': ['$parts.minute', ONE_MINUTE]},
        '$parts.second',
      ]
    },

  }},

  {'$project': {
    'ts'      : '$ts',
    'id'      : '$id',
    'year_doy': '$year_doy',
    'sod'     : {'$floor':{'$divide': ['$sod', 10]}} },
  },

  {'$sort': {'year_doy':1, 'sod':1}},
  {'$project': {'_id' : 0, 'ts' : 0 }},

  {'$group':{
    '_id': {'year_doy':'$year_doy', 'sod':'$sod'},
    'doc': {'$first':'$$ROOT'},
  }},
  {'$sort': {'_id.year_doy': 1, '_id.sod': 1}},
]; qc=db.sandbox.aggregate(p); mongo_print(qc, pretty=False)

# 'xx': {'$divide': ['$ts', SAMPLING_THRESHOLD]},

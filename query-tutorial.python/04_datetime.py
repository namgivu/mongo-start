from common import *

db.sandbox.delete_many({}) #clear all first

##do seeding
ts=datetime.strptime('2018-01-01 00:00:00','%Y-%m-%d %H:%M:%S')
tsAll=[
  {'ts': ts},
  {'ts': ts + relativedelta(seconds=10)},
  {'ts': ts + relativedelta(seconds=20)},
  {'ts': ts + relativedelta(seconds=30)},
  {'ts': ts + relativedelta(seconds=40)},
  {'ts': ts + relativedelta(seconds=50)},
  {'ts': ts + relativedelta(seconds=60)},
]
db.sandbox.insert_many(tsAll)

#output
ONE_SECOND = 1
ONE_MINUTE = 60*ONE_SECOND
ONE_HOUR   = 60*ONE_MINUTE
SAMPLING_THRESHOLD = 20*ONE_SECOND
p=[
  {'$project': {
    'ts': '$ts',
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

    'year-doy': {
      '$concat':[
        {'$substrBytes': ['$parts.year',0,-1] },
        '-',
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
    '_id' : 0,
  }},
]; qc=db.sandbox.aggregate(p); mongo_print(qc, pretty=True)

# 'ts01': {'$add': ['$ts', SAMPLING_THRESHOLD]},
# 'ts02': {'$divide': ['$ts', SAMPLING_THRESHOLD]},

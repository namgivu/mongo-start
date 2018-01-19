from common import *

db.inventory.delete_many({}) #clear all first

##do seeding

print('BEGIN insert item qty size status')
"""simple data ref. https://docs.mongodb.com/manual/tutorial/query-documents/#additional-query-tutorials"""
db.inventory.insert_many([
    {"item":     "journal",
     "qty":       25,
     "size":   {"h":   14, "w":   21, "uom":   "cm"},
     "status": "A",
     },

    {"item":     "notebook",
     "qty":       50,
     "size":   {"h":   8.5, "w":   11, "uom":   "in"},
     "status": "A",
     },

    {"item":     "paper",
     "qty":       100,
     "size":   {"h":   8.5, "w":   11, "uom":   "in"},
     "status": "D",
     },

    {"item":     "planner",
     "qty":       75, "size":   {"h":   22.85, "w":   30, "uom":   "cm"},
     "status": "D",
     },

    {"item":     "postcard",
     "qty":       45,
     "size":   {"h":   10, "w":   15.25, "uom":   "cm"},
     "status": "A",
     },
])
print('END   insert item qty size status')

print('BEGIN insert item qty tags dim_cm') #dim_cm == dimension in centimetter
"""data has array ref. https://docs.mongodb.com/manual/tutorial/query-array-of-documents/"""
db.inventory.insert_many([
    {"item":   "journal",
     "qty":    25,
     "tags":   ["blank", "red"],
     "dim_cm": [14, 21],
     },

    {"item":   "notebook",
     "qty":    50,
     "tags":   ["red", "blank"],
     "dim_cm": [14, 21],
     },

    {"item":   "paper",
     "qty":    100,
     "tags":   ["red", "blank", "plain"],
     "dim_cm": [14, 21],
     },

    {"item":   "planner",
     "qty":    75,
     "tags":   ["blank", "red"],
     "dim_cm": [22.85, 30],
     },

    {"item":   "postcard",
     "qty":    45,
     "tags":   ["blue"],
     "dim_cm": [10, 15.25],
     },
])
print('END   insert item qty tags dim_cm')

print('BEGIN insert item status size instock')
db.inventory.insert_many([
    {"item":    "journal",
     "status":  "A",
     "size":    {"h": 14, "w": 21, "uom": "cm"},
     "instock": [{"warehouse": "A", "qty": 5}]
     },

    {"item":    "notebook",
     "status":  "A",
     "size":    {"h": 8.5, "w": 11, "uom": "in"},
     "instock": [{"warehouse": "C", "qty": 5}]
     },

    {"item":    "paper",
     "status":  "D",
     "size":    {"h": 8.5, "w": 11, "uom": "in"},
     "instock": [{"warehouse": "A", "qty": 60}]
     },

    {"item":    "planner",
     "status":  "D",
     "size":    {"h": 22.85, "w": 30, "uom": "cm"},
     "instock": [{"warehouse": "A", "qty": 40}]
     },

    {"item":    "postcard",
     "status":  "A",
     "size":    {"h": 10, "w": 15.25, "uom": "cm"},
     "instock": [
         {"warehouse": "B", "qty": 15},
         {"warehouse": "C", "qty": 35},
     ]},
])
print('END   insert item status size instock')

#output
mongo_print(query_cursor=db.inventory.find(), pretty=True)
mongo_print(query_cursor=db.inventory.find())


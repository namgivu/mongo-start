#!/usr/bin/env bash

mongo #enter mongo prompt

echo "
#list db
db.getMongo().getDBNames()

#drop test db
use test
  db.dropDatabase()
use test_restored
  db.dropDatabase()
db.getMongo().getDBNames()

#list collections
db.getCollectionNames()

#note, we don't have rename command for db
"

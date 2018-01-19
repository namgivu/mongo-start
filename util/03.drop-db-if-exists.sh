#!/usr/bin/env bash

DB_HOST='localhost'
DB_NAME='test_dropdb'

#create db to drop later ref. https://www.mkyong.com/mongodb/how-to-create-database-or-collection-in-mongodb/
q="db.any.save({anyKey:122})"   && mongo --eval "$q" ${DB_HOST}/${DB_NAME}

#drop it
q="db.dropDatabase()" && mongo --eval "$q" ${DB_HOST}/${DB_NAME}

#list db
q="db.getMongo().getDBNames()"  && mongo --eval "$q" ${DB_HOST}/${DB_NAME}

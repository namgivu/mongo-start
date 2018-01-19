#!/usr/bin/env bash

: #ref. https://docs.mongodb.com/getting-started/shell/

s=$BASH_SOURCE ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ; export SCRIPT_HOME=$s
IMPORT_FILE="$SCRIPT_HOME/00c.primer-dataset.json"

DB_HOST='localhost'
DB_NAME='test'
DB_COLLECTION='restaurants'

#import db
mongoimport --db ${DB_NAME} --collection ${DB_COLLECTION} --drop --file ${IMPORT_FILE}

#query via cli / aftermath check ref. https://docs.mongodb.com/getting-started/shell/query/#query-by-a-top-level-field
q="db.$DB_COLLECTION.find()"                            && mongo --eval "$q" ${DB_HOST}/${DB_NAME}
q="db.$DB_COLLECTION.find( {'borough': 'Manhattan'} )"  && mongo --eval "$q" ${DB_HOST}/${DB_NAME}

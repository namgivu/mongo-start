#!/usr/bin/env bash

: #ref. https://docs.mongodb.com/getting-started/shell/

TEST_DATASET='https://raw.githubusercontent.com/mongodb/docs-assets/primer-dataset/primer-dataset.json'
IMPORT_FILE='/tmp/nn-mongodb/primer-dataset.json'

DB_HOST='localhost'
DB_NAME='test'
DB_COLLECTION='restaurants'

#import db
mkdir -p $(dirname ${IMPORT_FILE}) && \
  curl ${TEST_DATASET} -o ${IMPORT_FILE} && \
  mongoimport --db ${DB_NAME} --collection ${DB_COLLECTION} --drop --file ${IMPORT_FILE}

#query via cli / aftermath check ref. https://docs.mongodb.com/getting-started/shell/query/#query-by-a-top-level-field
q="db.$DB_COLLECTION.find()"                            && mongo --eval "$q" ${DB_HOST}/${DB_NAME}
q="db.$DB_COLLECTION.find( {'borough': 'Manhattan'} )"  && mongo --eval "$q" ${DB_HOST}/${DB_NAME}

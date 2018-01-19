#!/usr/bin/env bash
set -e

: #ref. https://dba.stackexchange.com/a/189938/52550

DB_NAME='test'
TODAY=`date +%Y%m%d-%H%M`
BACKUP_FOLDER='/tmp/nn-mongodb/backup'
BACKUP_FILE_GZ="$BACKUP_FOLDER/$TODAY-mongodb.tar.gz"

#backup for v3.2
mkdir -p ${BACKUP_FOLDER} && \
  mongodump --db ${DB_NAME} --gzip -o ${BACKUP_FILE_GZ}


#do restore ref. https://docs.mongodb.com/manual/reference/program/mongorestore/#restore-from-compressed-data
DB_NAME_RESTORE="${DB_NAME}_restored"
DB_COLLECTION='restaurants'
  #drop target db before restore
  q="db.dropDatabase()"  && mongo --eval "$q" ${DB_NAME_RESTORE}

  #do restore v3_2_09
  mongorestore --gzip --db "${DB_NAME_RESTORE}" "${BACKUP_FILE_GZ}/${DB_NAME}"

  : #restore aftermath check
  #check database
  q="db.getMongo().getDBNames()"  && mongo --eval "$q" | grep ${DB_NAME_RESTORE} || echo "Database $DB_NAME_RESTORE not found"
  #check data
  q="db.$DB_COLLECTION.find( {'borough': 'Manhattan'} )"  && mongo --eval "$q" ${DB_NAME_RESTORE}

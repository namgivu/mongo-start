#!/usr/bin/env bash
set -e

: #backup to .tar.gz file ref. https://github.com/controlz/Mongo-db-shell-backup/blob/master/mongodb-backup.sh

DB_NAME='test'
TODAY=`date +%Y%m%d-%H%M`
BACKUP_FOLDER='/tmp/nn-mongodb/backup'
BACKUP_FILE_GZ="$BACKUP_FOLDER/$TODAY-mongodb.tar.gz"

#do backup ref. https://docs.mongodb.com/manual/reference/program/mongodump/#compress-the-output
mkdir -p ${BACKUP_FOLDER} && \
  mongodump --db ${DB_NAME} --gzip --archive=${BACKUP_FILE_GZ} && \
  ls -lh ${BACKUP_FILE_GZ}

#do restore ref. https://docs.mongodb.com/manual/reference/program/mongorestore/#restore-from-compressed-data
DB_NAME_RESTORE="${DB_NAME}_restored"
DB_COLLECTION='restaurants'
  #v3_4_10
  mongorestore --gzip --archive=${BACKUP_FILE_GZ} --nsFrom "${DB_NAME}.*" --nsTo "${DB_NAME_RESTORE}.*"

  #v3_2_09
  mongorestore --gzip --archive=${BACKUP_FILE_GZ} --db "${DB_NAME_RESTORE}" "${DB_NAME}.*"

  #restore aftermath check
  q="db.$DB_COLLECTION.find( {'borough': 'Manhattan'} )"  && mongo --eval "$q" ${DB_NAME_RESTORE}

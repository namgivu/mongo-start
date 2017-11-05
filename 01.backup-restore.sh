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
  #drop target db before restore
  q="db.dropDatabase()"  && mongo --eval "$q" ${DB_NAME_RESTORE}

  #v3_4_10
  mongorestore --gzip --archive=${BACKUP_FILE_GZ} --nsFrom "${DB_NAME}.*" --nsTo "${DB_NAME_RESTORE}.*"

  #v3_2_09 TODO still failing ref. https://dba.stackexchange.com/questions/189928/how-restore-from-gz-backup-with-new-database-name-using-mongorestore-r3-2-9/189938?noredirect=1#comment368934_189938
  mongorestore --gzip --archive=${BACKUP_FILE_GZ} --db "${DB_NAME_RESTORE}" "${BACKUP_FILE_GZ}.*"

  : #v3_2_09 with extraction? Nope, the backup file created with --archive, so cannot ungzip it ref. https://dba.stackexchange.com/a/149276/52550

  : #restore aftermath check
  #check database
  q="db.getMongo().getDBNames()"  && mongo --eval "$q" | grep ${DB_NAME_RESTORE} || echo "Database $DB_NAME_RESTORE not found"
  #check data
  q="db.$DB_COLLECTION.find( {'borough': 'Manhattan'} )"  && mongo --eval "$q" ${DB_NAME_RESTORE}

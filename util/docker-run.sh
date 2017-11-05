#!/usr/bin/env bash

: #https://github.com/namgivu/deploy-util/blob/master/util/bash_util/docker-run/mongodb-docker-run.sh

#load param
if [ -z "$1" ]; then
  VERSION='latest'
else
  VERSION=$1
fi


SERVICE='mongod' #ref. https://stackoverflow.com/a/11776728/248616
REGISTRY='mongo'
IMAGE="${REGISTRY}:${VERSION}"
PORT=27017
CONTAINER_NAME="mongo_$VERSION"
DATA_FILE="$HOME/mongodb-data-${VERSION}"

sudo echo 'sudo initiated'
sudo service ${SERVICE} stop #stop any local $SERVICE so that our docker $SERVICE will override its port
docker rm -f ${CONTAINER_NAME}
docker run \
  -p ${PORT}:${PORT} \
  -v ${DATA_FILE}:/data/db \
  --name ${CONTAINER_NAME} ${IMAGE}

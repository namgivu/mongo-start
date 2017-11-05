#!/usr/bin/env bash

s=$BASH_SOURCE ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ; export SCRIPT_HOME=$s
version='3.2'
version='3.4'
${SCRIPT_HOME}/util/docker-run.sh $version
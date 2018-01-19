#!/usr/bin/env bash

s=$BASH_SOURCE ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ; export SCRIPT_HOME=$s
${SCRIPT_HOME}/docker-run.sh '3.2'
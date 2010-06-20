#!/bin/bash
#Skrypt linuksowy automatyzujacy pewne rzeczy

export PYTHONPATH=`pwd`

RELPATH=`pwd`
SERVER=$RELPATH/serwer/server.py
CONSERVER=$RELPATH/serwer/config.txt
WORKER=$RELPATH/worker/client.py

if [ "$1" = "run-server" ]; then
    if [ "$#" != 3 ]; then
        echo "Usage: run-server repo_name task_name"
    else
        cd serwer
        python $SERVER $2 $3
    fi
elif [ "$1" = "run-worker" ]; then
    cd worker
    while [ 1 ]; do
        python $WORKER
    done
elif [ "$1" = "config-server" ]; then
    vim $CONSERVER
elif [ "$1" = "compile-proto" ]; then
    protoc -I$RELPATH/common $RELPATH/common/datapakiet.proto --python_out=$RELPATH/common
elif [ "$1" = "create-database" ]; then
    python createDB.py
else
    echo "Dostepne komendy: run-server, run-worker, config-server, compile-proto, create-database"
fi


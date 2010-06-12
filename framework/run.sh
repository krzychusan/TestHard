#!/bin/bash
#Skrypt linuksowy automatyzujacy pewne rzeczy

export PYTHONPATH=`pwd`

RELPATH=`pwd`
SERVER=$RELPATH/serwer/main.py
CONSERVER=$RELPATH/serwer/config.txt
WORKER=$RELPATH/worker/client.py

if [ "$1" = "run-server" ]; then
	cd serwer
	python $SERVER
elif [ "$1" = "run-worker" ]; then
	cd worker
	python $WORKER
elif [ "$1" = "config-server" ]; then
	vim $CONSERVER
elif [ "$1" = "compile-proto" ]; then
	protoc -I$RELPATH/common $RELPATH/common/datapakiet.proto --python_out=$RELPATH/common
else
	echo "Dostepne komendy: run-server, run-worker, config-server, compile-proto"
fi


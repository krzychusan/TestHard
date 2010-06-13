#!/bin/bash
#Skrypt linuksowy automatyzujacy pewne rzeczy

export PYTHONPATH=`pwd`/framework

if [ "$1" = "run-web" ]; then
    source mydevenv/bin/activate
    paster serve --reload development.ini
fi


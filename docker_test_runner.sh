#!/bin/bash

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"

pip install -r ${SCRIPTPATH}/requirements.txt
cd ${SCRIPTPATH} && nosetests

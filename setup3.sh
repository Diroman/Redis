#!/bin/bash

mkdir "env"
python3 -m venv ./env
pip3 install -r requirements.txt

python3 run.py
rm -rf "env"
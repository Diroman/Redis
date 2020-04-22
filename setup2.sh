#!/bin/bash

mkdir "env"
python -m venv ./env
source env/bin/activate
pip install -r requirements.txt

python run.py
deactivate
rm -rf "env"
#!/bin/bash


echo "El nombre del proyecto es ParcialIDS"


mkdir API
cd API
touch app.py
mkdir .venv
python3 -m venv .venv 
souce .venv/bin/activate

pipenv install flask
export FLASK_DEBUG=1
pip install flask_sqlalchemy
pip install mysql-connector-python

mkdir templates
mkdir static
cd static
mkdir css
mkdir images
cd ..


echo 'Se ha creado tu entrono virtual'


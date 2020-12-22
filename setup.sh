#!/bin/bash

python3 -m venv venv
source venv/bin/activate
pip install -r matcher/requirements.txt

cd matcher-ui
npm install
npm run build

cd ../matcher
python manage.py runserver



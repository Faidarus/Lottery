#! /bin/bash 
sudo apt-get install python3-venv -y
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

pytest
pytest --cov=app
pytest --cov-config=.coveragec --cov=.
pytest --cov=app --cov-report=term-missing
pytest --cov . --cov-report html
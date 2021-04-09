#! /bin/bash 
sudo apt-get install python3-venv -y
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
pip3 install pytest
pip3 install pytest-cov

pytest service_one --cov --cov-report=term-missing 
pytest service_two --cov --cov-report=term-missing 
pytest service_three --cov --cov-report=term-missing 
pytest service_four --cov --cov-report=term-missing 

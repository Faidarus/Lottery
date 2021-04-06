sudo pytest
sudo pytest --cov=app
sudo pytest --cov-config=.coveragec --cov=.
sudo pytest --cov=app --cov-report=term-missing
sudo pytest --cov . --cov-report html
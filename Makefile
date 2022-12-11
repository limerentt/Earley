SHEll := /bin/bash


TEST = python -m pytest --verbosity=2 --showlocals --log-level=DEBUG

build:
	pip install poetry && poetry install

test:
	$(TEST)

test-cov:
	$(TEST) --cov=src --cov-report html --cov-fail-under=90

clean: 
	rm -fr __pycache__ .pytest_cache .coverage htmlcov 

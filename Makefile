install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff

lint:
	poetry run flake8 gendiff

build:
	poetry build

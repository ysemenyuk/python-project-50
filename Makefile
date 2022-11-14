install:
	poetry install

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff

lint:
	poetry run flake8 gendiff

build:
	poetry build
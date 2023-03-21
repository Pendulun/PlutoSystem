install:
	python -m pip install poetry poetry-core
	python -m poetry config virtualenvs.in-project true
	python -m poetry install

test:
	python -m poetry run pytest

ci/check: install test

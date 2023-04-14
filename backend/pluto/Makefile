install:
	pip install poetry poetry-core
	poetry config virtualenvs.in-project true
	poetry install

lint:
	poetry run black pluto
	poetry run isort pluto

lint-check:
	poetry run flake8 pluto
	poetry run isort --check-only pluto
	poetry run mypy pluto

unittest:
	poetry run pytest
test: unittest

ci/check: install lint-check test

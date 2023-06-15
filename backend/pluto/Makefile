PYTEST_FLAGS ?=

install:
	pip install poetry poetry-core
	poetry config virtualenvs.in-project true
	poetry install

lint:
	poetry run black pluto
	poetry run isort pluto

lint-check:
	poetry run flake8 --ignore=E501,W503 pluto
	poetry run isort --check-only pluto
	poetry run mypy pluto

unittest:
	poetry run pytest -vv --log-cli-level=DEBUG --capture=tee-sys --cov-report=html --cov=pluto $(PYTEST_FLAGS)
test: unittest

check: lint-check test
ci/check: install check

PYTEST_FLAGS ?=

build:
	pip3 install poetry==1.3.2 poetry-core==1.4.0
	poetry config experimental.new-installer false
	rm -rf package && mkdir package
	poetry export -f requirements.txt --output package/requirements.txt  --without-hashes
	pip3 install -r package/requirements.txt -t package
	docker build . -t server

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
	poetry run pytest $(PYTEST_FLAGS)
test: unittest

check: lint-check test
ci/check: install check

SHELL := bash

HELPERS ?= ./helpers
DB_HOST ?= localhost
DB_USER ?= postgres
DB_PASSWORD ?= changeme
DB_NAME ?= pluto
SETENV = DB_USER=$(DB_USER) DB_PASSWORD=$(DB_PASSWORD)

_build_bootstrap_image:
	$(SETENV) docker build \
	  -f $(HELPERS)/bootstrap/Dockerfile $(HELPERS)/bootstrap/ \
	  -t db-bootstrap

start: _build_bootstrap_image
	$(SETENV) docker-compose -f $(HELPERS)/docker-compose.yaml \
	  up -d

stop:
	$(SETENV) docker-compose -f $(HELPERS)/docker-compose.yaml \
	  down --remove-orphans

restart: stop start

db/connect:
	PGPASSWORD="$(DB_PASSWORD)" psql -h "$(DB_HOST)" --user "$(DB_USER)" -d "$(DB_NAME)"

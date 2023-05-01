SHELL := bash

HELPERS ?= ./helpers
DBHOST ?= localhost
DBUSER ?= postgres
DBPASSWORD ?= changeme
DBNAME ?= pluto
DBPORT ?= 123
HOST ?= localhost
PORT ?= 5000
BASE_SETENV = DBUSER=$(DB_USER) DBPASSWORD=$(DB_PASSWORD)
BOOTSTRAP_SETENV = $(BASE_SETENV)
COMPLETE_SETENV = $(BASE_SETENV) HOST=$(HOST) PORT=$(PORT) DBNAME=$(DB_NAME) DBPORT=$(DB_PORT) DBHOST=$(DB_HOST)
SERVER_SETENV = $(COMPLETE_SETENV)

_build_bootstrap_image:
	$(BOOTSTRAP_SETENV) docker build \
	  -f $(HELPERS)/bootstrap/Dockerfile $(HELPERS)/bootstrap/ \
	  -t db-bootstrap

_build_server_image:
	$(SERVER_SETENV) docker build \
	-f $(HELPERS)/server/Dockerfile $(HELPERS)/server/ \
	-t server

start: _build_bootstrap_image _build_server_image
	$(COMPLETE_SETENV) docker-compose -f $(HELPERS)/docker-compose.yaml \
	  up -d

stop:
	$(SETENV) docker-compose -f $(HELPERS)/docker-compose.yaml \
	  down --remove-orphans

restart: stop start

db/connect:
	PGPASSWORD="$(DB_PASSWORD)" psql -h "$(DB_HOST)" --user "$(DB_USER)" -d "$(DB_NAME)"

SHELL := bash

HELPERS ?= ./helpers
SERVER_DIR_PATH ?= ./backend/pluto/pluto/
DB_HOST ?= localhost
DB_USER ?= postgres
DB_PASSWORD ?= changeme
DB_NAME ?= pluto
DB_PORT ?= 5432
HOST ?= localhost
PORT ?= 5000
BASE_SETENV = DB_USER=$(DB_USER) DB_PASSWORD=$(DB_PASSWORD)
BOOTSTRAP_SETENV = $(BASE_SETENV)
COMPLETE_SETENV = $(BASE_SETENV) HOST=$(HOST) PORT=$(PORT) DB_NAME=$(DB_NAME) DB_PORT=$(DB_PORT) DB_HOST=$(DB_HOST)
TEMP_LOGS_DIR ?= logs

_build_bootstrap_image:
	$(BOOTSTRAP_SETENV) docker build \
	  -f $(HELPERS)/bootstrap/Dockerfile $(HELPERS)/bootstrap/ \
	  -t db-bootstrap

start/backend: _build_bootstrap_image
	$(COMPLETE_SETENV) docker-compose -f $(HELPERS)/docker-compose.yaml \
	  up -d
	$(COMPLETE_SETENV) python $(SERVER_DIR_PATH)/main.py > $(TEMP_LOGS_DIR)/backend.log 2>&1 &

start/frontend:
	cd frontend && \
		yarn run start > ../$(TEMP_LOGS_DIR)/frontend.log 2>&1 &
	cd frontend && \
	  yarn run bff > ../$(TEMP_LOGS_DIR)/bff.log 2>&1 &

_start:
	mkdir -p $(TEMP_LOGS_DIR)

start: _start start/backend start/frontend

stop:
	$(BASE_SETENV) docker-compose -f $(HELPERS)/docker-compose.yaml \
	  down --remove-orphans
	killall node

restart: stop start

db/connect:
	PGPASSWORD="$(DB_PASSWORD)" psql -h "$(DB_HOST)" --user "$(DB_USER)" -d "$(DB_NAME)"

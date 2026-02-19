.PHONY: help run test runserver build-local start-local stop-local xbuild xpublish run-prod

IMAGE ?= leohakim.dev
DOCKER_REPO ?= leohakim
TAG ?= $(shell git describe --tags `git rev-list --tags --max-count=1` 2>/dev/null || git rev-parse --short HEAD)
VENV ?= .venv

run: runserver

test:
	. $(VENV)/bin/activate && python manage.py test

runserver:
	. $(VENV)/bin/activate && python manage.py runserver 0.0.0.0:8000

build-local:
	docker compose -f docker-compose.local.yml up --build

start-local:
	docker compose -f docker-compose.local.yml up

stop-local:
	docker compose -f docker-compose.local.yml down

xbuild:
	docker buildx build --platform linux/amd64,linux/arm64 -t ${DOCKER_REPO}/${IMAGE}:${TAG} -o type=image .

xpublish:
	docker buildx build --platform linux/amd64,linux/arm64 -t ${DOCKER_REPO}/${IMAGE}:${TAG} --push -f Dockerfile .

run-prod:
	docker compose -f production.yml up -d --build

help:
	@echo "Available targets:"
	@echo "  run              Activate $(VENV) and run Django server"
	@echo "  test             Activate $(VENV) and run Django tests"
	@echo "  runserver        Run local server on 0.0.0.0:8000"
	@echo "  build-local      Build and start local Docker stack"
	@echo "  start-local      Start local Docker stack"
	@echo "  stop-local       Stop local Docker stack"
	@echo "  xbuild           Multi-arch build (no push)"
	@echo "  xpublish         Multi-arch build and push"
	@echo "  run-prod         Build and start production.yml stack"

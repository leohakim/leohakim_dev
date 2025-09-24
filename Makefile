PHONY: build-local
build-local:
	docker-compose -f docker-compose.local.yml up --build

PHONY: start-local
start-local:
	docker-compose -f docker-compose.local.yml up

PHONY: stop-local
stop-local:
	docker-compose -f docker-compose.local.yml down

help:
	@echo "Available targets:"
	@echo "  help			Show this help message"
	@echo "  build-local		Build the development environment"
	@echo "  start-local		Start the development environment"
	@echo "  stop-local		Stop the development environment"

COMPOSE_FILE = docker/docker-compose.yml
PERSISTENT_PATH = docker/persistent

run: create-persistent
	docker compose -f $(COMPOSE_FILE) up -d
build: create-persistent
	docker compose -f $(COMPOSE_FILE) up --build -d
restart: create-persistent
	docker compose -f $(COMPOSE_FILE) down
	docker compose -f $(COMPOSE_FILE) up --build -d
stop:
	docker compose -f $(COMPOSE_FILE) down
create-persistent:
	mkdir -p $(PERSISTENT_PATH)
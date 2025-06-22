#!/bin/bash
FOLDER=$1
BRANCH=$2
YML=$3
COMMONS_ACCESS_TOKEN=$4
CHATBOT_ACCESS_TOKEN=$5
FCM_ACCESS_TOKEN=$6

git pull origin $BRANCH
docker compose -f ~/$FOLDER/.docker/$YML build --build-arg COMMONS_ACCESS_TOKEN=$COMMONS_ACCESS_TOKEN --build-arg CHATBOT_ACCESS_TOKEN=$CHATBOT_ACCESS_TOKEN --build-arg FCM_ACCESS_TOKEN=$FCM_ACCESS_TOKEN
docker compose -f ~/$FOLDER/.docker/$YML stop
docker compose -f ~/$FOLDER/.docker/$YML rm -f
docker compose -f ~/$FOLDER/.docker/$YML up -d --remove-orphans
docker system prune --force
docker exec -it web python manage.py migrate

# seed db with mandatory handlers
docker exec -it web python manage.py seed_handlers

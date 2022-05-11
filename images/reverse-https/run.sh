#!/bin/bash

set -e

source .env

BACKEND_IP=$(docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $TARGET_BACKEND_CONTAINER)

docker build -t towl/dev-haproxy .

echo "Running reverse proxy with backend container $TARGET_BACKEND_CONTAINER  holding ip : $BACKEND_IP"

docker run -d --rm --name reverse-local-ssl -v $PWD/haproxy.cfg:/etc/haproxy/haproxy.cfg -p 443:443 -e BACKEND_IP=$BACKEND_IP --network=wordpress_default towl/dev-haproxy

echo "OK"

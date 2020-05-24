#!/bin/bash
#set -x
cd /home/pi/Desktop/ampnado && \
docker-compose down && \
docker rmi ampnado && \
docker image prune -f && \
docker volume rm ampnado_ampnadovol && \
docker volume prune -f && \
docker-compose up && \
docker image prune -f

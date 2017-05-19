#!/bin/bash

docker pull mongo:3.2
docker rm -f mongo
docker run --name mongo -v mongo:/data/db -d -p 27017:27017 mongo --noauth  

docker build -t pull .
docker rm -f pull
docker run --name pull -t --link mongo -d pull

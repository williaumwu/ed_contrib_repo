#!/bin/bash

# remove exited containers:
docker ps --filter status=dead --filter status=exited -aq | xargs -r docker rm -v
docker rm -v $(docker ps -a -q -f status=exited)
 
# remove unused images:
docker images --no-trunc | grep '<none>' | awk '{ print $3 }' | xargs -r docker rmi
docker rmi $(docker images -f "dangling=true" -q)
 
# remove unused volumes:
docker volume rm $(docker volume ls -qf dangling=true)
find '/var/lib/docker/volumes/' -mindepth 1 -maxdepth 1 -type d | grep -vFf <(
  docker ps -aq | xargs docker inspect | jq -r '.[] | .Mounts | .[] | .Name | select(.)'
) | xargs -r rm -fr





















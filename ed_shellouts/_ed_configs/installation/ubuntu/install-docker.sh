#!/bin/bash

apt-get update -y 
service lxcfs stop
apt-get remove -y -q lxc-common lxcfs lxd lxd-client
apt-get update -y 

apt-cache policy docker-engine
apt-get install -y --allow-unauthenticated docker.io

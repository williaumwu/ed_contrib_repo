#!/bin/bash

apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \
echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list && \
apt-get update && \
apt-get install -y mongodb-org-server=2.6.9 mongodb-org-shell

#apt-get install -y mongodb-org=2.6.9 mongodb-org-server=2.6.9 mongodb-org-shell=2.6.9 mongodb-org-mongos=2.6.9 mongodb-org-tools=2.6.9 
#
#apt-get install -y pwgen wget curl git-core build-essential scons devscripts lintian dh-make \
#libpcre3 libpcre3-dev libboost-dev libboost-date-time-dev libboost-filesystem-dev \
#libboost-program-options-dev libboost-system-dev libboost-thread-dev \
#libpcap-dev libreadline-dev libssl-dev rng-tools haveged && \
#wget https://s3.amazonaws.com/jiffy-mongodb/mongodb-ssl_2.6.7_amd64.deb && \
#dpkg -i mongodb-ssl_2.6.7_amd64.deb

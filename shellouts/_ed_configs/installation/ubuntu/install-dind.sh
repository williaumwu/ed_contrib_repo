#!/bin/bash

apt-get update && \
DEBIAN_FRONTEND=noninteractive apt-get -y dist-upgrade && \
apt-get install -yq apt-transport-https && \
apt-get clean

apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9 && \
echo deb https://get.docker.io/ubuntu docker main > /etc/apt/sources.list.d/docker.list && \
apt-get update && \
apt-get install -yq lxc-docker-1.4.1

# Install docker-compose
bash -c "curl -L https://github.com/docker/compose/releases/download/1.4.2/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose" &&
chmod +x /usr/local/bin/docker-compose &&
bash -c "curl -L https://raw.githubusercontent.com/docker/compose/1.4.2/contrib/completion/bash/docker-compose > /etc/bash_completion.d/docker-compose" &&
#
# Install docker-cleanup command
cd /tmp &&
git clone https://gist.github.com/76b450a0c986e576e98b.git &&
cd 76b450a0c986e576e98b &&
mv docker-cleanup /usr/local/bin/docker-cleanup &&
chmod +x /usr/local/bin/docker-cleanup 

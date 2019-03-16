#!/bin/bash

apt-get update -y &&
apt-get install linux-image-extra-$(uname -r) linux-image-extra-virtual -y &&
#use apt for https
apt-get install apt-transport-https ca-certificates curl software-properties-common -y &&
#Install key for docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
#
apt-key fingerprint 0EBFCD88
#Install docker
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" 

apt-get update -y &&
apt-get install docker-ce -y
#apt-get install docker-ce=<VERSION>

#############################
###Old method
#############################
## Install kernel extra's to enable docker aufs support
## Did not require this below to complete because it will NOT work with 
## docker in docker
#echo "#######################################"
#echo "#######Installing kernel extras########"
#echo "#######################################"
#apt-get -y install linux-image-extra-$(uname -r) &&
## Add Docker PPA and install latest version
#apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9 &&
#bash -c "echo deb https://get.docker.io/ubuntu docker main > /etc/apt/sources.list.d/docker.list" &&
#apt-get update &&
#echo "#######################################"
#echo "#######Installing lxc-docker###########"
#echo "#######################################"
#apt-get install lxc-docker -y &&
## Install docker-compose
#bash -c "curl -L https://github.com/docker/compose/releases/download/1.4.2/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose" &&
#chmod +x /usr/local/bin/docker-compose &&
#bash -c "curl -L https://raw.githubusercontent.com/docker/compose/1.4.2/contrib/completion/bash/docker-compose > /etc/bash_completion.d/docker-compose" &&
##wget -qO- https://get.docker.com/ | sh
### Install docker-compose
##bash -c "curl -L https://github.com/docker/compose/releases/download/1.4.2/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose" &&
##chmod +x /usr/local/bin/docker-compose &&
##bash -c "curl -L https://raw.githubusercontent.com/docker/compose/1.4.2/contrib/completion/bash/docker-compose > /etc/bash_completion.d/docker-compose" &&
##
## Install docker-cleanup command
#rm -rf /tmp/76b450a0c986e576e98b
#cd /tmp &&
#git clone https://gist.github.com/76b450a0c986e576e98b.git &&
#cd 76b450a0c986e576e98b &&
#mv docker-cleanup /usr/local/bin/docker-cleanup &&
#chmod +x /usr/local/bin/docker-cleanup 

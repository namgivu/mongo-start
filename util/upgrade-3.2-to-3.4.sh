#!/usr/bin/env bash

#ensure the right linux distro
cat /etc/os-release #should see Ubuntu 16.04

#ensure mongodb 3.2 installed
mongo --version #should see MongoDB 3.2.x

#ensure 'apt package' mongodb-org installed ref. https://stackoverflow.com/a/1298103/248616
dpkg -S `which mongo` `which mongorestore` #should see mongodb-org-xxx
dpkg -s mongodb-org

#upgrade for mongodb-org package ref. https://askubuntu.com/a/44124/22308
sudo apt install --only-upgrade mongodb-org

#TODO continue steps here ref. https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/#install-mongodb-community-edition

#! /bin/bash

if [ -e ./alertmanager.tar.gz ]
then
	echo -e "File exists"
else
	echo -e "File doesnt exists"
	wget https://github.com/prometheus/alertmanager/releases/download/v0.7.1/alertmanager-0.7.1.linux-amd64.tar.gz -O alertmanager.tar.gz
fi

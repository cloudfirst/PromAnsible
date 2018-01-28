#! /bin/bash

if [ -e ./prometheus.tar.gz ]
then
	echo -e "File exists"
else
	echo -e "File doesnt exists"
	wget https://github.com/prometheus/prometheus/releases/download/v1.7.1/prometheus-1.7.1.linux-amd64.tar.gz -O prometheus.tar.gz
fi

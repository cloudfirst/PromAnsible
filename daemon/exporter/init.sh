#! /bin/bash

if [ -e ./node_exporter.tar.gz ]
then
	echo -e "File exists"
else
	echo -e "File doesnt exists"
	wget https://github.com/prometheus/node_exporter/releases/download/v0.14.0/node_exporter-0.14.0.linux-amd64.tar.gz  -O node_exporter.tar.gz
        wget https://github.com/prometheus/mysqld_exporter/releases/download/v0.10.0/mysqld_exporter-0.10.0.linux-amd64.tar.gz -O mysqld_exporter.tar.gz
fi

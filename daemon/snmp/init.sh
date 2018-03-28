#! /bin/bash

if [ -e ./snmp.tar.gz ]
then
	echo -e "File exists"
else
	echo -e "File doesnt exists"
	wget https://github.com/prometheus/snmp_exporter/releases/download/v0.8.0/snmp_exporter-0.8.0.linux-amd64.tar.gz -O snmp.tar.gz
fi

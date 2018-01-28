#! /bin/bash

if [ -e ./grafana.tar.gz ]
then
	echo -e "File exists"
else
	echo -e "File doesnt exists"
	wget https://s3-us-west-2.amazonaws.com/grafana-releases/release/grafana-4.4.1.linux-x64.tar.gz -O grafana.tar.gz
fi
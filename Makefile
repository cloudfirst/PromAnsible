# Makefile
#
#

.PHONY: build clean

EDU_MONITOR     =debian/educloud-monitor
EDU_GRAFANA     =debian/grafana-server
EDU_PROMETHEUS  =debian/prometheus-server
EDU_ALERTMAN    =debian/alertman-server
EDU_SNMP	    =debian/snmp-exporter
EDU_WTEE        =debian/educloud-wtee
EDU_DAEMON      =debian/educloud-daemon

#### exporter
NODE_EXPORTER   =debian/node-exporter


build:
	echo "now is building educloud-monitor debian packages ... ... "
clean:
	echo "now is cleaning educloud-monitor debian packages ... ... "
	rm debian/*.debhelper* debian/*substvars debian/stamp* debian/compat debian/files || true
	rm ../*.tar* ../*.deb ../*.dsc ../*.changes || true
	rm -fr $(EDU_MONITOR)    || true
	rm -fr $(EDU_PROMETHEUS) || true
	rm -fr $(EDU_ALERTMAN)   || true
	rm -fr $(EDU_GRAFANA)    || true
	rm -fr $(EDU_SNMP)       || true
	rm -fr $(EDU_WTEE)       || true
	rm -fr $(EDU_DAEMON)     || true
	rm -fr $(NODE_EXPORTER)  || true
	rm -fr daemon/monitord/build || true 
	rm -fr daemon/monitord/dist || true
install:
	#####################
	#     EDU_MONITOR   #
	#####################
	install -d $(EDU_MONITOR)/usr/local/www/monitor
	cp $(CURDIR)/monitor/*.py                               $(EDU_MONITOR)/usr/local/www/

	python -m compileall $(CURDIR)/monitor/monitor/
	mv $(CURDIR)/monitor/monitor/*.pyc                      $(EDU_MONITOR)/usr/local/www/monitor/
	cp $(CURDIR)/monitor/monitor/wsgi.py                    $(EDU_MONITOR)/usr/local/www/monitor/
	rm $(EDU_MONITOR)/usr/local/www/monitor/wsgi.pyc

	install -d $(EDU_MONITOR)/usr/local/webconfig/
	cp -r $(CURDIR)/webconfig/apache2                       $(EDU_MONITOR)/usr/local/webconfig/
	cp -r $(CURDIR)/webconfig/prometheus                    $(EDU_MONITOR)/usr/local/webconfig/
	cp -r $(CURDIR)/webconfig/alertman                      $(EDU_MONITOR)/usr/local/webconfig/
	cp -r $(CURDIR)/webconfig/grafana                       $(EDU_MONITOR)/usr/local/webconfig/
	cp -r $(CURDIR)/webconfig/pip                           $(EDU_MONITOR)/usr/local/webconfig/
	cp -r $(CURDIR)/webconfig/snmp                          $(EDU_MONITOR)/usr/local/webconfig/
	cp    $(CURDIR)/debian/sudoers                          $(EDU_MONITOR)/usr/local/webconfig/
	cp    $(CURDIR)/debian/ssh-config                       $(EDU_MONITOR)/usr/local/webconfig/

	install -d $(EDU_MONITOR)/usr/local/www/portal
	python -m compileall $(CURDIR)/monitor/portal/
	mv $(CURDIR)/monitor/portal/*.pyc                       $(EDU_MONITOR)/usr/local/www/portal/
	cp -r $(CURDIR)/monitor/portal/static                   $(EDU_MONITOR)/usr/local/www/portal/
	cp -r $(CURDIR)/monitor/portal/templates                $(EDU_MONITOR)/usr/local/www/portal/
	cp -r $(CURDIR)/monitor/portal/sql                      $(EDU_MONITOR)/usr/local/www/portal/

	install -d $(EDU_MONITOR)/usr/local/www/django_apscheduler
	python -m compileall $(CURDIR)/monitor/django_apscheduler/
	mv $(CURDIR)/monitor/django_apscheduler/*.pyc           $(EDU_MONITOR)/usr/local/www/django_apscheduler/
	cp -r $(CURDIR)/monitor/django_apscheduler/cron         $(EDU_MONITOR)/usr/local/www/django_apscheduler/

	install -d $(EDU_MONITOR)/storage/config/template
	install -d $(EDU_MONITOR)/storage/data/prometheus
	install -d $(EDU_MONITOR)/storage/data/alertman
	install -d $(EDU_MONITOR)/storage/static/wechat
	install -d $(EDU_MONITOR)/storage/ansible
	install -d $(EDU_MONITOR)/storage/log

	#########################
	#     EDU_PROMETHEUS    #
	#########################
	install -d $(EDU_PROMETHEUS)/usr/local/daemon/prometheus
	cd $(CURDIR)/daemon/prometheus/ && ./init.sh
	tar vxf $(CURDIR)/daemon/prometheus/prometheus.tar.gz --strip 1 -C $(EDU_PROMETHEUS)/usr/local/daemon/prometheus/

	install -d $(EDU_PROMETHEUS)/etc/supervisor/conf.d
	cp $(CURDIR)/daemon/prometheus/supervisor/prometheus.conf   $(EDU_PROMETHEUS)/etc/supervisor/conf.d/

	#########################
	#     EDU_ALERTMAN      #
	#########################
	install -d $(EDU_ALERTMAN)/usr/local/daemon/alertman
	cd $(CURDIR)/daemon/alertman/ && ./init.sh
	tar vxf $(CURDIR)/daemon/alertman/alertmanager.tar.gz --strip 1 -C $(EDU_ALERTMAN)/usr/local/daemon/alertman/

	install -d $(EDU_ALERTMAN)/etc/supervisor/conf.d
	cp $(CURDIR)/daemon/alertman/supervisor/alertman.conf   $(EDU_ALERTMAN)/etc/supervisor/conf.d/

	######################
	#     EDU_GRAFANA    #
	######################
	install -d $(EDU_GRAFANA)/usr/local/daemon/grafana
	cd $(CURDIR)/daemon/grafana/ && ./init.sh
	tar vxf $(CURDIR)/daemon/grafana/grafana.tar.gz --strip 1 -C $(EDU_GRAFANA)/usr/local/daemon/grafana/

	install -d $(EDU_GRAFANA)/etc/supervisor/conf.d
	cp $(CURDIR)/daemon/grafana/supervisor/grafana.conf   $(EDU_GRAFANA)/etc/supervisor/conf.d/

	######################
	#     EDU_SNMP       # 
	###################### 
	install -d $(EDU_SNMP)/usr/local/daemon/snmp
	cd $(CURDIR)/daemon/snmp/ && ./init.sh
	tar vxf $(CURDIR)/daemon/snmp/snmp_exporter.tar.gz --strip 1 -C $(EDU_SNMP)/usr/local/daemon/snmp/

	install -d $(EDU_SNMP)/etc/supervisor/conf.d
	cp $(CURDIR)/daemon/snmp/supervisor/snmp-exporter.conf   $(EDU_SNMP)/etc/supervisor/conf.d/

	######################
	#     EDU_WTEE       #
	######################
	install -d $(EDU_WTEE)/usr/bin/
	cp $(CURDIR)/daemon/wtee/wtee-server            $(EDU_WTEE)/usr/bin/

	install -d $(EDU_WTEE)/etc/supervisor/conf.d
	cp $(CURDIR)/daemon/wtee/supervisor/wtee.conf   $(EDU_WTEE)/etc/supervisor/conf.d/


	########################
	#     EDU_DAEMON       #
	########################
	install -d $(EDU_DAEMON)/usr/local/daemon/monitord
	cd $(CURDIR)/daemon/monitord && sudo -u luhya pyinstaller monitord_cmd_consumer.py -F -s
	cp $(CURDIR)/daemon/monitord/dist/monitord_cmd_consumer  $(EDU_DAEMON)/usr/local/daemon/monitord/

	install -d $(EDU_DAEMON)/etc/supervisor/conf.d
	cp $(CURDIR)/daemon/monitord/supervisor/monitord.conf   $(EDU_DAEMON)/etc/supervisor/conf.d/

	########################
	#     NODE_EXPORTER    #
	########################
	install -d $(NODE_EXPORTER)/usr/local/exporter/node-exporter
	cd $(CURDIR)/daemon/exporter/ && ./init.sh
	tar vxf $(CURDIR)/daemon/exporter/node_exporter.tar.gz --strip 1 -C  $(NODE_EXPORTER)/usr/local/exporter/node-exporter

	install -d $(NODE_EXPORTER)/etc/supervisor/conf.d
	cp $(CURDIR)/daemon/exporter/supervisor/node-exporter.conf   $(NODE_EXPORTER)/etc/supervisor/conf.d/

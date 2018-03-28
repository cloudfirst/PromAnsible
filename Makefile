# Makefile
#
#

.PHONY: build clean

PROMANSIBLE_MONITOR     =debian/promansible-monitor
PROMANSIBLE_GRAFANA     =debian/grafana-server
PROMANSIBLE_PROMETHEUS  =debian/prometheus-server
PROMANSIBLE_ALERTMAN    =debian/alertman-server
PROMANSIBLE_SNMP	=debian/snmp-exporter
PROMANSIBLE_WTEE        =debian/promansible-wtee
PROMANSIBLE_DAEMON      =debian/promansible-daemon

#### exporter
NODE_EXPORTER   =debian/node-exporter


build:
	echo "now is building promansible-monitor debian packages ... ... "
clean:
	echo "now is cleaning promansible-monitor debian packages ... ... "
	rm debian/*.debhelper* debian/*substvars debian/stamp* debian/compat debian/files || true
	rm ../*.tar* ../*.deb ../*.dsc ../*.changes || true
	rm -fr $(PROMANSIBLE_MONITOR)    || true
	rm -fr $(PROMANSIBLE_PROMETHEUS) || true
	rm -fr $(PROMANSIBLE_ALERTMAN)   || true
	rm -fr $(PROMANSIBLE_GRAFANA)    || true
	rm -fr $(PROMANSIBLE_SNMP)       || true
	rm -fr $(PROMANSIBLE_WTEE)       || true
	rm -fr $(PROMANSIBLE_DAEMON)     || true
	rm -fr $(NODE_EXPORTER)  || true
	rm -fr daemon/monitord/build || true
	rm -fr daemon/monitord/dist || true
publish:
	rm $(CURDIR)/../promansible-Install/playbook/roles/monitor/files/*.deb  || true
	cp $(CURDIR)/../*.deb 	$(CURDIR)/../promansible-Install/playbook/roles/monitor/files   || true
	cp $(CURDIR)/../node-exporter*.deb   $(CURDIR)/../sample-ansible-script-for-promansible/playbook/routine/roles/install-node-exporter/files/ || true
install:
	#############################
	#     PROMANSIBLE_MONITOR   #
	#############################
	install -d $(PROMANSIBLE_MONITOR)/usr/local/www/monitor
	cp $(CURDIR)/monitor/*.py                               $(PROMANSIBLE_MONITOR)/usr/local/www/

	python -m compileall $(CURDIR)/monitor/monitor/
	mv $(CURDIR)/monitor/monitor/*.pyc                      $(PROMANSIBLE_MONITOR)/usr/local/www/monitor/
	cp $(CURDIR)/monitor/monitor/wsgi.py                    $(PROMANSIBLE_MONITOR)/usr/local/www/monitor/
	rm $(PROMANSIBLE_MONITOR)/usr/local/www/monitor/wsgi.pyc

	install -d $(PROMANSIBLE_MONITOR)/usr/local/webconfig/
	cp -r $(CURDIR)/webconfig/apache2                       $(PROMANSIBLE_MONITOR)/usr/local/webconfig/
	cp -r $(CURDIR)/webconfig/prometheus                    $(PROMANSIBLE_MONITOR)/usr/local/webconfig/
	cp -r $(CURDIR)/webconfig/alertman                      $(PROMANSIBLE_MONITOR)/usr/local/webconfig/
	cp -r $(CURDIR)/webconfig/grafana                       $(PROMANSIBLE_MONITOR)/usr/local/webconfig/
	cp -r $(CURDIR)/webconfig/pip                           $(PROMANSIBLE_MONITOR)/usr/local/webconfig/
	cp -r $(CURDIR)/webconfig/snmp                          $(PROMANSIBLE_MONITOR)/usr/local/webconfig/
	cp    $(CURDIR)/debian/sudoers                          $(PROMANSIBLE_MONITOR)/usr/local/webconfig/
	cp    $(CURDIR)/debian/ssh-config                       $(PROMANSIBLE_MONITOR)/usr/local/webconfig/

	install -d $(PROMANSIBLE_MONITOR)/usr/local/www/portal
	python -m compileall $(CURDIR)/monitor/portal/
	mv $(CURDIR)/monitor/portal/*.pyc                       $(PROMANSIBLE_MONITOR)/usr/local/www/portal/
	cp -r $(CURDIR)/monitor/portal/static                   $(PROMANSIBLE_MONITOR)/usr/local/www/portal/
	cp -r $(CURDIR)/monitor/portal/templates                $(PROMANSIBLE_MONITOR)/usr/local/www/portal/
	cp -r $(CURDIR)/monitor/portal/sql                      $(PROMANSIBLE_MONITOR)/usr/local/www/portal/

	install -d $(PROMANSIBLE_MONITOR)/usr/local/www/django_apscheduler
	python -m compileall $(CURDIR)/monitor/django_apscheduler/
	mv $(CURDIR)/monitor/django_apscheduler/*.pyc           $(PROMANSIBLE_MONITOR)/usr/local/www/django_apscheduler/
	cp -r $(CURDIR)/monitor/django_apscheduler/cron         $(PROMANSIBLE_MONITOR)/usr/local/www/django_apscheduler/

	install -d $(PROMANSIBLE_MONITOR)/storage/config/template
	install -d $(PROMANSIBLE_MONITOR)/storage/data/prometheus
	install -d $(PROMANSIBLE_MONITOR)/storage/data/alertman
	install -d $(PROMANSIBLE_MONITOR)/storage/static/wechat
	install -d $(PROMANSIBLE_MONITOR)/storage/ansible
	install -d $(PROMANSIBLE_MONITOR)/storage/log

	#################################
	#     PROMANSIBLE_PROMETHEUS    #
	#################################
	install -d $(PROMANSIBLE_PROMETHEUS)/usr/local/daemon/prometheus
	cd $(CURDIR)/daemon/prometheus/ && ./init.sh
	tar vxf $(CURDIR)/daemon/prometheus/prometheus.tar.gz --strip 1 -C $(PROMANSIBLE_PROMETHEUS)/usr/local/daemon/prometheus/

	install -d $(PROMANSIBLE_PROMETHEUS)/etc/supervisor/conf.d
	cp $(CURDIR)/daemon/prometheus/supervisor/prometheus.conf   $(PROMANSIBLE_PROMETHEUS)/etc/supervisor/conf.d/

	#################################
	#     PROMANSIBLE_ALERTMAN      #
	#################################
	install -d $(PROMANSIBLE_ALERTMAN)/usr/local/daemon/alertman
	cd $(CURDIR)/daemon/alertman/ && ./init.sh
	tar vxf $(CURDIR)/daemon/alertman/alertmanager.tar.gz --strip 1 -C $(PROMANSIBLE_ALERTMAN)/usr/local/daemon/alertman/

	install -d $(PROMANSIBLE_ALERTMAN)/etc/supervisor/conf.d
	cp $(CURDIR)/daemon/alertman/supervisor/alertman.conf   $(PROMANSIBLE_ALERTMAN)/etc/supervisor/conf.d/

	##############################
	#     PROMANSIBLE_GRAFANA    #
	##############################
	install -d $(PROMANSIBLE_GRAFANA)/usr/local/daemon/grafana
	cd $(CURDIR)/daemon/grafana/ && ./init.sh
	tar vxf $(CURDIR)/daemon/grafana/grafana.tar.gz --strip 1 -C $(PROMANSIBLE_GRAFANA)/usr/local/daemon/grafana/

	install -d $(PROMANSIBLE_GRAFANA)/etc/supervisor/conf.d
	cp $(CURDIR)/daemon/grafana/supervisor/grafana.conf   $(PROMANSIBLE_GRAFANA)/etc/supervisor/conf.d/

	##############################
	#     PROMANSIBLE_SNMP       #
	##############################
	install -d $(PROMANSIBLE_SNMP)/usr/local/daemon/snmp
	cd $(CURDIR)/daemon/snmp/ && ./init.sh
	tar vxf $(CURDIR)/daemon/snmp/snmp_exporter.tar.gz --strip 1 -C $(PROMANSIBLE_SNMP)/usr/local/daemon/snmp/

	install -d $(PROMANSIBLE_SNMP)/etc/supervisor/conf.d
	cp $(CURDIR)/daemon/snmp/supervisor/snmp-exporter.conf   $(PROMANSIBLE_SNMP)/etc/supervisor/conf.d/

	##############################
	#     PROMANSIBLE_WTEE       #
	##############################
	install -d $(PROMANSIBLE_WTEE)/usr/bin/
	cp $(CURDIR)/daemon/wtee/wtee-server            $(PROMANSIBLE_WTEE)/usr/bin/

	install -d $(PROMANSIBLE_WTEE)/etc/supervisor/conf.d
	cp $(CURDIR)/daemon/wtee/supervisor/wtee.conf   $(PROMANSIBLE_WTEE)/etc/supervisor/conf.d/


	################################
	#     PROMANSIBLE_DAEMON       #
	################################
	install -d $(PROMANSIBLE_DAEMON)/usr/local/daemon/monitord
	cd $(CURDIR)/daemon/monitord && sudo -u luhya pyinstaller monitord_cmd_consumer.py -F -s
	cp $(CURDIR)/daemon/monitord/dist/monitord_cmd_consumer  $(PROMANSIBLE_DAEMON)/usr/local/daemon/monitord/

	install -d $(PROMANSIBLE_DAEMON)/etc/supervisor/conf.d
	cp $(CURDIR)/daemon/monitord/supervisor/monitord.conf   $(PROMANSIBLE_DAEMON)/etc/supervisor/conf.d/

	########################
	#     NODE_EXPORTER    #
	########################
	install -d $(NODE_EXPORTER)/usr/local/exporter/node-exporter
	cd $(CURDIR)/daemon/exporter/ && ./init.sh
	tar vxf $(CURDIR)/daemon/exporter/node_exporter.tar.gz --strip 1 -C  $(NODE_EXPORTER)/usr/local/exporter/node-exporter

	install -d $(NODE_EXPORTER)/etc/supervisor/conf.d
	cp $(CURDIR)/daemon/exporter/supervisor/node-exporter.conf   $(NODE_EXPORTER)/etc/supervisor/conf.d/

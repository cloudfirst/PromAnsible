CONF_PATH="/storage/config/educloud.conf"
PROMETHEUS_CONF = "/storage/config/prometheus.yml"

TEMPLATE_GLOABLE='''
global:
  scrape_interval:     1m # By default, scrape targets every 15 seconds.
  evaluation_interval: 1m # Evaluate rules every 15 seconds.

  # Attach these extra labels to all timeseries collected by this Prometheus instance.
  external_labels:
    monitor: 'codelab-monitor'
'''

TEMPLATE_RULE='''
rule_files:
  - "/storage/config/alert.rules"
'''

TEMPLATE_SCRAPE='''
scrape_configs: []
'''


TEMPLATE_ALERT='''
alerting:
  alertmanagers:
  - scheme: http
    static_configs:
    - targets:
      - "127.0.0.1:9093"
'''

TEMPLATE_SNMP='''
scrape_configs:
  - job_name: 'snmp'
    static_configs:
      - targets: [] # SNMP device.
    metrics_path: /snmp
    params:
      module: [default]
    relabel_configs:
      - source_labels: [__address__]
        target_label: __param_target
      - source_labels: [__param_target]
        target_label: instance
      - target_label: __address__
        replacement: 127.0.0.1:9116  # SNMP exporter.   
'''


def add_rule():
    pass

def create_job(job_name):
    ret = {}
    ret['job_name'] = job_name
    ret['scrape_interval'] = '15s'
    ret['static_configs'] = []

    return ret

def create_target(target_str, label):
    ret = {}
    ret['labels'] = {}
    ret['labels']['group'] = label
    ret['targets'] = []
    ret['targets'].append(target_str)
    return ret

def add_target_to_snmp_job(targets, job):
    for t in targets:
        job['scrape_configs'][0]['static_configs'][0]['targets'].append(t)

    return job

def add_target_to_job(target, job):
    flag = False
    t_list = job['static_configs']
    for t in t_list:
        if t['labels']['group'] == target['labels']['group']:
            t['targets'].append(target['targets'][0])
            flag = True
            break
    if not flag:
        t_list.append(target)

    return job

# {
#     "scrape_configs": [
#         {
#             "static_configs": [
#                 {
#                     "labels": {
#                         "group": "production"
#                     },
#                     "targets": [
#                         "localhost:8080",
#                         "localhost:8081"
#                     ]
#                 },
#                 {
#                     "labels": {
#                         "group": "canary"
#                     },
#                     "targets": [
#                         "localhost:8082"
#                     ]
#                 }
#             ],
#             "job_name": "example-random",
#             "scrape_interval": "5s"
#         }
#     ]
# }
# scrape_configs:
# - job_name: example-random
#   scrape_interval: 5s
#   static_configs:
#   - labels:
#       group: production
#     targets:
#     - localhost:8080
#     - localhost:8081
#   - labels:
#       group: canary
#     targets:
#     - localhost:8082


import yaml

TEMPLATE_GLOABLE='''
global:
  scrape_interval:     15s # By default, scrape targets every 15 seconds.
  evaluation_interval: 15s # Evaluate rules every 15 seconds.

  # Attach these extra labels to all timeseries collected by this Prometheus instance.
  external_labels:
    monitor: 'codelab-monitor'
'''
TEMPLATE_RULE='''
rule_files: []
'''
TEMPLATE_SCRAPE='''
scrape_configs: []
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


def create_job(job_name):
    ret = {}
    ret['job_name'] = job_name
    ret['scrape_interval'] = '5s'
    ret['static_configs'] = []

    return ret

def add_target_to_snmp_job(targets, job):
    for t in targets:
        job['scrape_configs'][0]['static_configs'][0]['targets'].append(t)

    return job

def create_target(target_str, label):
    ret = {}
    ret['labels'] = {}
    ret['labels']['group'] = label
    ret['targets'] = []
    ret['targets'].append(target_str)
    return ret


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

yaml_conf = yaml.safe_load(TEMPLATE_SCRAPE)
newjob = create_job("node")
new_t = create_target("10.0.0.100:9100", "clc")
newjob = add_target_to_job(new_t, newjob)

ccs = \
[
        {
            'ccip':   "10.0.0.101",
            'ccname':  'name1',
            'ncs':      ['192.168.0.1', '192.168.0.2'],
        },
        {
            'ccip':   "10.0.0.102",
            'ccname':  'name2',
            'ncs':      ['192.168.10.1', '192.168.10.2'],
        },
]

for cc in ccs:
    new_cc_t = create_target(cc['ccip'] + ":9100", 'cc')
    newjob = add_target_to_job(new_cc_t, newjob)

    ncs = cc['ncs']
    for nc in ncs:
        new_nc_t = create_target(nc + ":9100", cc['ccname'] + "-nc")
        newjob = add_target_to_job(new_nc_t, newjob)

yaml_conf['scrape_configs'].append(newjob)

snmp_job = yaml.safe_load(TEMPLATE_SNMP)
snmp_target = ['192.168.96.254', '129.168.0.10']
snmp_job = add_target_to_snmp_job(snmp_target, snmp_job)

#  print json.dumps(yaml_conf, indent=4)
#  print yaml.safe_dump(newjob, default_flow_style=False)
print TEMPLATE_GLOABLE
content = yaml.safe_dump(yaml_conf, default_flow_style=False)
#content = yaml.safe_dump(yaml_conf)
print content
print yaml.safe_dump(snmp_job['scrape_configs'], default_flow_style=False)



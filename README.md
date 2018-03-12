# promansible-monitor
designed to monitor (real-time) promansible system, with the help of prometheus, grafana,and Ansible, FAI

The whole work flow looks like below:

## I installation
- A Django APP monitor+portal is installed at
       /usr/local/www/monitor
       /usr/local/www/portal
- multiple supervisor controlled web servers are installed at
       /usr/local/daemon/prometheus (/storage/config/prometheus.yml)
       /usr/local/daemon/grafana
       /usr/local/daemon/ansible

## II integrate ansible with prometheus & alertmanage
2.0 assuming the existence of ansible playbook
```
.
├── example.txt
├── geninventory.py
├── playbook
│   ├── alert
│   │   └── roles
│   │       ├── handle_cpu_threshold_exceeded
│   │       │   └── README.md
│   │       ├── handle_DiskWillFillIn4Hours
│   │       │   └── README.md
│   │       ├── handle_HighErrorRate
│   │       │   └── README.md
│   │       ├── handle_net_device_down
│   │       │   └── README.md
│   │       └── handle_server_down
│   │           └── README.md
│   └── routine
│       └── roles
│           ├── check_dns_sinobot_biz
│           │   └── README.md
│           ├── check_EXSi_port
│           │   └── README.md
│           ├── check_ftp_connect
│           │   └── README.md
│           ├── check_LAN_speed
│           │   └── README.md
│           ├── check_vpn_dns
│           │   └── README.md
│           ├── check_vpn_website_abroad_connect
│           │   └── README.md
│           ├── restart_l2tp_vpn
│           │   └── README.md
│           └── restart_pptp_vpn
│               └── README.md
└── README.md
```
```
cmdline:
   ansible-playbook <task>            -i <inventory_path>  -u <user> -K --extra-vars "user=<user>"
   ansible-playbook playbook/ping.yml -i ./geninventory.py -u luhya -k


ping.yml   # task file name
--------------
- hosts: 192.168.56.101  # ip addr comes from alert message
  roles:
      - ping  # role name, namely what shoud be done in playbook/roles/ping/tasks/main.yml

$ ./geninventory.py --list  # dynamic inventory generation
{'monitor-dev': ['192.168.56.101']}

```

2.1 Daily routing ansible-playbook
for each group of servers, we could design a serials daily routing tasks as below
- ansible-playbook playbook/routing_*.yml -i ./geninventory.py -u luhya -k
  in each routing_*.yml,
  - host: targes_group
    roles:
       - routing_task_1
       - routing_task_2
       ...
       - routing_task_n
- config its schedule, per hour, per day, per weekly ?
- and add it to cron job

2.2 alert-event-handler playbook
- list all available alert type
- list all available alert_* role
- configure one or more alert_* role to one alert type
- trigger alert_* playbook when alert happens


2.3 ansible facts
cc | SUCCESS =>
{
    "ansible_facts": {
        "ansible_all_ipv4_addresses": [
            "10.0.2.15",
            "192.168.56.101"
        ],
        "ansible_all_ipv6_addresses": [
            "fe80::a00:27ff:fe36:1617",
            "fe80::a00:27ff:feed:f063"
        ],
        "ansible_apparmor": {
            "status": "enabled"
        },
        "ansible_architecture": "x86_64",
        "ansible_bios_date": "12/01/2006",
        "ansible_bios_version": "VirtualBox",
        "ansible_cmdline": {
            "BOOT_IMAGE": "/boot/vmlinuz-3.13.0-24-generic",
            "quiet": true,
            "ro": true,
            "root": "UUID=0f4d6540-f06f-499b-b054-ece4b299deef",
            "splash": true,
            "vt.handoff": "7"
        },
        "ansible_date_time": {
            "date": "2017-09-11",
            "day": "11",
            "epoch": "1505096041",
            "hour": "10",
            "iso8601": "2017-09-11T02:14:01Z",
            "iso8601_basic": "20170911T101401063777",
            "iso8601_basic_short": "20170911T101401",
            "iso8601_micro": "2017-09-11T02:14:01.063888Z",
            "minute": "14",
            "month": "09",
            "second": "01",
            "time": "10:14:01",
            "tz": "CST",
            "tz_offset": "+0800",
            "weekday": "星期一",
            "weekday_number": "1",
            "weeknumber": "37",
            "year": "2017"
        },
        "ansible_default_ipv4": {
            "address": "10.0.2.15",
            "alias": "eth0",
            "broadcast": "10.0.2.255",
            "gateway": "10.0.2.2",
            "interface": "eth0",
            "macaddress": "08:00:27:36:16:17",
            "mtu": 1500,
            "netmask": "255.255.255.0",
            "network": "10.0.2.0",
            "type": "ether"
        },
        "ansible_default_ipv6": {},
        "ansible_devices": {
            "sda": {
                "holders": [],
                "host": "SATA controller: Intel Corporation 82801HM/HEM (ICH8M/ICH8M-E) SATA Controller [AHCI mode] (rev 02)",
                "model": "VBOX HARDDISK",
                "partitions": {
                    "sda1": {
                        "holders": [],
                        "sectors": "1348466688",
                        "sectorsize": 512,
                        "size": "643.00 GB",
                        "start": "2048",
                        "uuid": "0f4d6540-f06f-499b-b054-ece4b299deef"
                    },
                    "sda2": {
                        "holders": [],
                        "sectors": "2",
                        "sectorsize": 512,
                        "size": "1.00 KB",
                        "start": "1348470782",
                        "uuid": null
                    },
                    "sda5": {
                        "holders": [],
                        "sectors": "2093056",
                        "sectorsize": 512,
                        "size": "1022.00 MB",
                        "start": "1348470784",
                        "uuid": "0751653b-0d7b-4f72-91d4-d2803ee427e8"
                    }
                },
                "removable": "0",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "deadline",
                "sectors": "1350565888",
                "sectorsize": "512",
                "size": "644.00 GB",
                "support_discard": "0",
                "vendor": "ATA"
            },
            "sr0": {
                "holders": [],
                "host": "IDE interface: Intel Corporation 82371AB/EB/MB PIIX4 IDE (rev 01)",
                "model": "CD-ROM",
                "partitions": {},
                "removable": "1",
                "rotational": "1",
                "sas_address": null,
                "sas_device_handle": null,
                "scheduler_mode": "deadline",
                "sectors": "2097151",
                "sectorsize": "512",
                "size": "1024.00 MB",
                "support_discard": "0",
                "vendor": "VBOX"
            }
        },
        "ansible_distribution": "Ubuntu",
        "ansible_distribution_major_version": "14",
        "ansible_distribution_release": "trusty",
        "ansible_distribution_version": "14.04",
        "ansible_dns": {
            "nameservers": [
                "127.0.1.1"
            ]
        },
        "ansible_domain": "",
        "ansible_effective_group_id": 1000,
        "ansible_effective_user_id": 1000,
        "ansible_env": {
            "HOME": "/home/luhya",
            "LANG": "en_US.UTF-8",
            "LC_ADDRESS": "zh_CN.UTF-8",
            "LC_IDENTIFICATION": "zh_CN.UTF-8",
            "LC_MEASUREMENT": "zh_CN.UTF-8",
            "LC_MONETARY": "zh_CN.UTF-8",
            "LC_NAME": "zh_CN.UTF-8",
            "LC_NUMERIC": "zh_CN.UTF-8",
            "LC_PAPER": "zh_CN.UTF-8",
            "LC_TELEPHONE": "zh_CN.UTF-8",
            "LC_TIME": "zh_CN.UTF-8",
            "LOGNAME": "luhya",
            "MAIL": "/var/mail/luhya",
            "PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games",
            "PWD": "/home/luhya",
            "SHELL": "/bin/bash",
            "SHLVL": "1",
            "SSH_CLIENT": "192.168.56.1 64845 22",
            "SSH_CONNECTION": "192.168.56.1 64845 192.168.56.101 22",
            "SSH_TTY": "/dev/pts/5",
            "TERM": "xterm-256color",
            "USER": "luhya",
            "XDG_RUNTIME_DIR": "/run/user/1000",
            "XDG_SESSION_ID": "1",
            "_": "/bin/sh"
        },
        "ansible_eth0": {
            "active": true,
            "device": "eth0",
            "features": {
                "fcoe_mtu": "off [fixed]",
                "generic_receive_offload": "on",
                "generic_segmentation_offload": "on",
                "highdma": "off [fixed]",
                "l2_fwd_offload": "off [fixed]",
                "large_receive_offload": "off [fixed]",
                "loopback": "off [fixed]",
                "netns_local": "off [fixed]",
                "ntuple_filters": "off [fixed]",
                "receive_hashing": "off [fixed]",
                "rx_all": "off",
                "rx_checksumming": "off",
                "rx_fcs": "off",
                "rx_vlan_filter": "on [fixed]",
                "rx_vlan_offload": "on",
                "rx_vlan_stag_filter": "off [fixed]",
                "rx_vlan_stag_hw_parse": "off [fixed]",
                "scatter_gather": "on",
                "tcp_segmentation_offload": "on",
                "tx_checksum_fcoe_crc": "off [fixed]",
                "tx_checksum_ip_generic": "on",
                "tx_checksum_ipv4": "off [fixed]",
                "tx_checksum_ipv6": "off [fixed]",
                "tx_checksum_sctp": "off [fixed]",
                "tx_checksumming": "on",
                "tx_fcoe_segmentation": "off [fixed]",
                "tx_gre_segmentation": "off [fixed]",
                "tx_gso_robust": "off [fixed]",
                "tx_ipip_segmentation": "off [fixed]",
                "tx_lockless": "off [fixed]",
                "tx_mpls_segmentation": "off [fixed]",
                "tx_nocache_copy": "on",
                "tx_scatter_gather": "on",
                "tx_scatter_gather_fraglist": "off [fixed]",
                "tx_sit_segmentation": "off [fixed]",
                "tx_tcp6_segmentation": "off [fixed]",
                "tx_tcp_ecn_segmentation": "off [fixed]",
                "tx_tcp_segmentation": "on",
                "tx_udp_tnl_segmentation": "off [fixed]",
                "tx_vlan_offload": "on [fixed]",
                "tx_vlan_stag_hw_insert": "off [fixed]",
                "udp_fragmentation_offload": "off [fixed]",
                "vlan_challenged": "off [fixed]"
            },
            "ipv4": {
                "address": "10.0.2.15",
                "broadcast": "10.0.2.255",
                "netmask": "255.255.255.0",
                "network": "10.0.2.0"
            },
            "ipv6": [
                {
                    "address": "fe80::a00:27ff:fe36:1617",
                    "prefix": "64",
                    "scope": "link"
                }
            ],
            "macaddress": "08:00:27:36:16:17",
            "module": "e1000",
            "mtu": 1500,
            "pciid": "0000:00:03.0",
            "promisc": false,
            "speed": 1000,
            "type": "ether"
        },
        "ansible_eth1": {
            "active": true,
            "device": "eth1",
            "features": {
                "fcoe_mtu": "off [fixed]",
                "generic_receive_offload": "on",
                "generic_segmentation_offload": "on",
                "highdma": "off [fixed]",
                "l2_fwd_offload": "off [fixed]",
                "large_receive_offload": "off [fixed]",
                "loopback": "off [fixed]",
                "netns_local": "off [fixed]",
                "ntuple_filters": "off [fixed]",
                "receive_hashing": "off [fixed]",
                "rx_all": "off",
                "rx_checksumming": "off",
                "rx_fcs": "off",
                "rx_vlan_filter": "on [fixed]",
                "rx_vlan_offload": "on",
                "rx_vlan_stag_filter": "off [fixed]",
                "rx_vlan_stag_hw_parse": "off [fixed]",
                "scatter_gather": "on",
                "tcp_segmentation_offload": "on",
                "tx_checksum_fcoe_crc": "off [fixed]",
                "tx_checksum_ip_generic": "on",
                "tx_checksum_ipv4": "off [fixed]",
                "tx_checksum_ipv6": "off [fixed]",
                "tx_checksum_sctp": "off [fixed]",
                "tx_checksumming": "on",
                "tx_fcoe_segmentation": "off [fixed]",
                "tx_gre_segmentation": "off [fixed]",
                "tx_gso_robust": "off [fixed]",
                "tx_ipip_segmentation": "off [fixed]",
                "tx_lockless": "off [fixed]",
                "tx_mpls_segmentation": "off [fixed]",
                "tx_nocache_copy": "on",
                "tx_scatter_gather": "on",
                "tx_scatter_gather_fraglist": "off [fixed]",
                "tx_sit_segmentation": "off [fixed]",
                "tx_tcp6_segmentation": "off [fixed]",
                "tx_tcp_ecn_segmentation": "off [fixed]",
                "tx_tcp_segmentation": "on",
                "tx_udp_tnl_segmentation": "off [fixed]",
                "tx_vlan_offload": "on [fixed]",
                "tx_vlan_stag_hw_insert": "off [fixed]",
                "udp_fragmentation_offload": "off [fixed]",
                "vlan_challenged": "off [fixed]"
            },
            "ipv4": {
                "address": "192.168.56.101",
                "broadcast": "192.168.56.255",
                "netmask": "255.255.255.0",
                "network": "192.168.56.0"
            },
            "ipv6": [
                {
                    "address": "fe80::a00:27ff:feed:f063",
                    "prefix": "64",
                    "scope": "link"
                }
            ],
            "macaddress": "08:00:27:ed:f0:63",
            "module": "e1000",
            "mtu": 1500,
            "pciid": "0000:00:08.0",
            "promisc": false,
            "speed": 1000,
            "type": "ether"
        },
        "ansible_fips": false,
        "ansible_form_factor": "Other",
        "ansible_fqdn": "monitor-dev",
        "ansible_gather_subset": [
            "hardware",
            "network",
            "virtual"
        ],
        "ansible_hostname": "monitor-dev",
        "ansible_interfaces": [
            "lo",
            "eth1",
            "eth0"
        ],
        "ansible_kernel": "3.13.0-24-generic",
        "ansible_lo": {
            "active": true,
            "device": "lo",
            "features": {
                "fcoe_mtu": "off [fixed]",
                "generic_receive_offload": "on",
                "generic_segmentation_offload": "on",
                "highdma": "on [fixed]",
                "l2_fwd_offload": "off [fixed]",
                "large_receive_offload": "off [fixed]",
                "loopback": "on [fixed]",
                "netns_local": "on [fixed]",
                "ntuple_filters": "off [fixed]",
                "receive_hashing": "off [fixed]",
                "rx_all": "off [fixed]",
                "rx_checksumming": "on [fixed]",
                "rx_fcs": "off [fixed]",
                "rx_vlan_filter": "off [fixed]",
                "rx_vlan_offload": "off [fixed]",
                "rx_vlan_stag_filter": "off [fixed]",
                "rx_vlan_stag_hw_parse": "off [fixed]",
                "scatter_gather": "on",
                "tcp_segmentation_offload": "on",
                "tx_checksum_fcoe_crc": "off [fixed]",
                "tx_checksum_ip_generic": "on [fixed]",
                "tx_checksum_ipv4": "off [fixed]",
                "tx_checksum_ipv6": "off [fixed]",
                "tx_checksum_sctp": "off [fixed]",
                "tx_checksumming": "on",
                "tx_fcoe_segmentation": "off [fixed]",
                "tx_gre_segmentation": "off [fixed]",
                "tx_gso_robust": "off [fixed]",
                "tx_ipip_segmentation": "off [fixed]",
                "tx_lockless": "on [fixed]",
                "tx_mpls_segmentation": "off [fixed]",
                "tx_nocache_copy": "off [fixed]",
                "tx_scatter_gather": "on [fixed]",
                "tx_scatter_gather_fraglist": "on [fixed]",
                "tx_sit_segmentation": "off [fixed]",
                "tx_tcp6_segmentation": "on",
                "tx_tcp_ecn_segmentation": "on",
                "tx_tcp_segmentation": "on",
                "tx_udp_tnl_segmentation": "off [fixed]",
                "tx_vlan_offload": "off [fixed]",
                "tx_vlan_stag_hw_insert": "off [fixed]",
                "udp_fragmentation_offload": "on",
                "vlan_challenged": "on [fixed]"
            },
            "ipv4": {
                "address": "127.0.0.1",
                "broadcast": "host",
                "netmask": "255.0.0.0",
                "network": "127.0.0.0"
            },
            "ipv6": [
                {
                    "address": "::1",
                    "prefix": "128",
                    "scope": "host"
                }
            ],
            "mtu": 65536,
            "promisc": false,
            "type": "loopback"
        },
        "ansible_lsb": {
            "codename": "trusty",
            "description": "Ubuntu 14.04 LTS",
            "id": "Ubuntu",
            "major_release": "14",
            "release": "14.04"
        },
        "ansible_machine": "x86_64",
        "ansible_machine_id": "02e690b1779c88109b6fdaec595a0ad2",
        "ansible_memfree_mb": 1485,
        "ansible_memory_mb": {
            "nocache": {
                "free": 2391,
                "used": 1562
            },
            "real": {
                "free": 1485,
                "total": 3953,
                "used": 2468
            },
            "swap": {
                "cached": 0,
                "free": 1021,
                "total": 1021,
                "used": 0
            }
        },
        "ansible_memtotal_mb": 3953,
        "ansible_mounts": [
            {
                "device": "/dev/sda1",
                "fstype": "ext4",
                "mount": "/",
                "options": "rw,errors=remount-ro",
                "size_available": 639262838784,
                "size_total": 679447740416,
                "uuid": "N/A"
            }
        ],
        "ansible_nodename": "monitor-dev",
        "ansible_os_family": "Debian",
        "ansible_pkg_mgr": "apt",
        "ansible_processor": [
            "GenuineIntel",
            "Intel(R) Core(TM) i7-3615QM CPU @ 2.30GHz"
        ],
        "ansible_processor_cores": 1,
        "ansible_processor_count": 1,
        "ansible_processor_threads_per_core": 1,
        "ansible_processor_vcpus": 1,
        "ansible_product_name": "VirtualBox",
        "ansible_product_serial": "NA",
        "ansible_product_uuid": "NA",
        "ansible_product_version": "1.2",
        "ansible_python": {
            "executable": "/usr/bin/python",
            "has_sslcontext": false,
            "type": "CPython",
            "version": {
                "major": 2,
                "micro": 6,
                "minor": 7,
                "releaselevel": "final",
                "serial": 0
            },
            "version_info": [
                2,
                7,
                6,
                "final",
                0
            ]
        },
        "ansible_python_version": "2.7.6",
        "ansible_real_group_id": 1000,
        "ansible_real_user_id": 1000,
        "ansible_selinux": false,
        "ansible_service_mgr": "upstart",
        "ansible_ssh_host_key_dsa_public": "AAAAB3NzaC1kc3MAAACBAI40zRvgRQwgft2TIVQQ5iSc2foWVVqRq2fQp7Thq8a8tJ9a8a3U2+PZ9BZQXw3G63Ft95pEn0SSG7Iv26hx4FFrwia3AnCVWfZeLXL4ISn1H01fTA8ERcwto03YD1/CuPF/xyBBS5AoXyk+DMf2r7oGEM+GUThqPFFj5jvYELklAAAAFQCJHdwUnyOe8aVtTW4uJ4alCvUdgQAAAIBMAb2q2ABnykFiwnM6qBu4jtYWwjgJsrXdLlXN3dCwUz4XYdv9GsfsFJgmHYpt6uollDgCYUKKEq0qHY6q4UaGsrhhjB2sHVe1L663/h9ycyynVXit5KE8+P5oIup+xTuF/nplSLyGD1uqUGG0aMMu6CB8eoTaJYm/NUwR9wG6xQAAAIASXd8L12I5TKtzlSjeryJLXNpLBiKcdHHwTl5LEjtyN7cbbVnOv416crcnuqI8w6m/Ni65ZFRghbtrvUtzlT5hDyYiK2iAByfUxvYUlOLpcEqhLFKL471lnPDQsMEeuKwKbMp0HX+9isGgZP9MYpOcdebpD1VGnaK7/Gxyvktfqw==",
        "ansible_ssh_host_key_ecdsa_public": "AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBO2RlSC4auha3cO2LTgYe58NRvPcq7uiDVEZPQ0SHr0FxSR8exGpZ3+LiBDNPETKsaceqmeAkZNAeyOd+GkijqE=",
        "ansible_ssh_host_key_ed25519_public": "AAAAC3NzaC1lZDI1NTE5AAAAIL7Y+pUUdzgKvQ1riwADXyV27CpIPRpQfNrzZXvPQMcD",
        "ansible_ssh_host_key_rsa_public": "AAAAB3NzaC1yc2EAAAADAQABAAABAQC//bEVPM+SHlvpX1VydwpTOkqDJmGWpnRBTw3Zqv/hnrNJGDkCTp7TbzebCmaXQvQ095BKBa3ke4cRxWZArKxlZtjIxzafvXBvR+KnJ/yS8gGaQT8IT6WRXrBjOoSXaINDd8D9Oh+nlbzyGDrHQE2iOOBzdm+XFDgPx0rtvyrZgDExwt0pfe+mMd/WNxaYxu04t11PISfSt7jAK68TRvn6NDOG6FpseTSuqfDLubylT3HGjPnRAIKb4dKNLEYcVkmMzMtxaq8bbvGrOgPv6yhjTTfaOUqep0dYFlajtXy5ro4hSAUaL8h1vCkeYdqN0HZM/o69gUV4cn6KynZSg06T",
        "ansible_swapfree_mb": 1021,
        "ansible_swaptotal_mb": 1021,
        "ansible_system": "Linux",
        "ansible_system_capabilities": [
            ""
        ],
        "ansible_system_capabilities_enforced": "True",
        "ansible_system_vendor": "innotek GmbH",
        "ansible_uptime_seconds": 2279,
        "ansible_user_dir": "/home/luhya",
        "ansible_user_gecos": "luhya,,,",
        "ansible_user_gid": 1000,
        "ansible_user_id": "luhya",
        "ansible_user_shell": "/bin/bash",
        "ansible_user_uid": 1000,
        "ansible_userspace_architecture": "x86_64",
        "ansible_userspace_bits": "64",
        "ansible_virtualization_role": "guest",
        "ansible_virtualization_type": "virtualbox",
        "module_setup": true
    },
    "changed": false
}

## III Re-thinking Auto IT management with prometheus & ansible
3.1 Overview
Goal
- by applying the SRE concept to SMB, to help automating their IT management
  collect metrics first, alert by rules, and handle alert automatically, plus routine operation.
Content
- * network service management
- * server & OS management
- (plus)application management
Steps
- a template yml file as belwo
     1	- hosts: '{{ myhost }}'
     2	  become: true
     3	  become_user: root
     4	  become_method: sudo
     5	  roles:
     6	    - '{{ myrole }}'
- for routine :
     1 run-once : select target(groups or single), and save the history record in db
     2 cron-job :
       * select target(groups or single)
       * select time & frequency
- for alert
     1 add handler to alert
     2 target
       - machine report alert
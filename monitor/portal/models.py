# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# system parameters
class mn_DeviceType(models.Model):
    type_name = models.CharField(max_length=30)

class mn_ServerGroup(models.Model):
    group_name = models.CharField(max_length=30)
    listen_port= models.IntegerField(default=9100)

class mn_OSTypes(models.Model):
    # Windows:  Windows XP, Windows 7, Windows 2003, Windows 2008, Windows 2012
    # Linux:    Ubuntu, Ubuntu_64, redhat, centos, etc
    ostype     = models.CharField(max_length=30)

# network device
class mn_NetDevices(models.Model):
    device_type = models.CharField(max_length=30)
    device_ip   = models.CharField(max_length=30)
    device_mac  = models.CharField(max_length=30)

    memo    = models.CharField(max_length=300, default="please add some description here")

# computing servers
class mn_Servers(models.Model):
    sip     = models.CharField(max_length=30)
    smac    = models.CharField(max_length=30)
    sostype = models.CharField(max_length=30)
    smodel  = models.CharField(max_length=100)

    sgroup1 = models.CharField(max_length=50)
    sgroup2 = models.CharField(max_length=50)
    sgroup3 = models.CharField(max_length=50)
    sgroup4 = models.CharField(max_length=50)

    sadmin  = models.CharField(max_length=30)
    spasswd = models.CharField(max_length=30)

    memo    = models.CharField(max_length=300, default="please add some description here")

# enterprise wechat
class mn_Enterprise_wechat(models.Model):
    corp_id    = models.CharField(max_length=100)
    app_secret = models.CharField(max_length=100)
    app_id     = models.IntegerField(default=0)
    # alert message to these user ids, a json list
    user_ids   = models.CharField(max_length=300)

# ansible parameters
class mn_Ansible_git_para(models.Model):
    git_url    = models.CharField(max_length=300)
    git_pubkey = models.CharField(max_length=300)
    git_prvkey = models.CharField(max_length=300)

class mn_Ansible_action(models.Model):
    # action_name is the playbook roles
    action_name = models.CharField(max_length=30)
    action_desc = models.CharField(max_length=300)

class mn_alert2action(models.Model):
    alert_name = models.CharField(max_length=30)
    # actions'name is a json list
    alert_actions = models.CharField(max_length=300)

class mn_routine_op_history(models.Model):
    action_name  = models.CharField(max_length=30)
    group_name   = models.CharField(max_length=100)
    target_name  = models.CharField(max_length=100)
    invoke_times = models.IntegerField(default=0)

class mn_routine_crob_job(models.Model):
    action_name = models.CharField(max_length=30)
    target_name = models.CharField(max_length=100)
    cron_paras  = models.CharField(max_length=100)

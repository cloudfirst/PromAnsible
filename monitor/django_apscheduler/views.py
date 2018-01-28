# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
import os, requests, json
from zmqWrapper import *
from monitor.settings import ANSIBLE_PATH
from portal.ansible_helper import ansible_get_git_url, get_host_username_and_password
from apscheduler.triggers.cron import CronTrigger
from cron.ExpressionParser import *
from cron.Options import *

from monitorLog import *
logger = getMonitorLogger()

from apscheduler.schedulers.background import BackgroundScheduler
from jobstores import DjangoJobStore
from apscheduler.executors.pool import ProcessPoolExecutor, ThreadPoolExecutor
from tzlocal import get_localzone

def get_timezone():
    tz = get_localzone()
    return str(tz)

ansible_scheduler = BackgroundScheduler({
    'apscheduler.job_defaults.coalesce': 'true',
    'apscheduler.job_defaults.max_instances': '5',
    'apscheduler.timezone': get_timezone(),
})

logger.error("create backgroupd schedule with id=%s" % id(ansible_scheduler))
ansible_scheduler.add_jobstore(DjangoJobStore(), 'default')
# ansible_scheduler.add_executor(ProcessPoolExecutor(10), 'default')
ansible_scheduler.add_executor(ThreadPoolExecutor(20), 'default')
ansible_scheduler.start()

def run_cron_job(op, group, entity):
    url = ansible_get_git_url()
    prj_name = url.split('/')[-1].split('.')[0]
    message = {}
    message['event']= "APSchedule"
    message['type'] = "routine"
    message["role"] = op
    message['group']= group
    message["host"] = entity
    message["src_path"] = ANSIBLE_PATH + prj_name
    message['username'], message['password'] = get_host_username_and_password(entity)
    message["before_prompt"] = "Ansible Scheduled Routine Operation start ... ..."
    message["after_prompt"]  = "Ansible Scheduled Routine Operation finished."
    logger.error("send zmq message as below %s" % json.dumps(message, indent=4))
    _message = json.dumps(message)
    zmq_send('127.0.0.1', _message, MONITORD_CMD_QUEUE_PORT)

Day_of_Week = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]

def parse_day_of_week(myinput):
    if myinput == "" or myinput == "*":
       return None
    else:
        return Day_of_Week[int(myinput)]

def format_exp(myinput):
    if myinput == "" or myinput == "*":
       return None
    else:
       return myinput

def cron_add(request):
    op     = request.POST['op']
    group  = request.POST['group']
    entity = request.POST['entity']
    cron   = request.POST['cron']

    cron_obj = ExpressionParser(cron, Options())
    cron_str_list = cron_obj.parse()

    # mycrontrigger = CronTrigger(
    #     year        = format_exp(cron_str_list[6]),
    #     day_of_week = parse_day_of_week(cron_str_list[5]),
    #     month       = format_exp(cron_str_list[4]),
    #     day         = format_exp(cron_str_list[3]),
    #     hour        = format_exp(cron_str_list[2]),
    #     minute      = format_exp(cron_str_list[1]),
    #     second      = format_exp(cron_str_list[0]),
    #     start_date  = None,
    #     end_date    = None,
    #     timezone    = None
    # )

    ret = ansible_scheduler.add_job(
                              run_cron_job,
                              trigger="cron",
                              year=format_exp(cron_str_list[6]),
                              day_of_week=parse_day_of_week(cron_str_list[5]),
                              month=format_exp(cron_str_list[4]),
                              day=format_exp(cron_str_list[3]),
                              hour=format_exp(cron_str_list[2]),
                              minute=format_exp(cron_str_list[1]),
                              second=format_exp(cron_str_list[0]),
                              start_date=None,
                              end_date=None,
                              timezone=get_timezone(),
                              args=[op, group, entity])

    logger.error("a new sched job is created with result = %s" % str(ret))
    response = {}
    response["Result"] = "OK"
    return HttpResponse(json.dumps(response), content_type='application/json')

def cron_del(request):
    id = request.POST['id']
    ansible_scheduler.remove_job(id)

    logger.error("Remove job id=%s" % id)
    response = {}
    response["Result"] = "OK"
    return HttpResponse(json.dumps(response), content_type='application/json')

def cron_pause(request):
    id = request.POST['id']
    ret = ansible_scheduler.pause_job(id)

    response = {}
    response["Result"] = "OK"
    return HttpResponse(json.dumps(response), content_type='application/json')

def cron_resume(request):
    id = request.POST['id']
    ansible_scheduler.resume_job(id)

    response = {}
    response["Result"] = "OK"
    return HttpResponse(json.dumps(response), content_type='application/json')

def cron_list(request):
    response = {}
    response["Result"] = "OK"
    response['data'] = []
    job_list  = ansible_scheduler.get_jobs()
    for j in job_list:
        data = {}
        data['id']   = j.id
        data['role'] = j.args[0]
        data['host'] = j.args[1]
        data['next'] = str(j.next_run_time).split('+')[0]
        tstr = str(j.trigger)
        logger.error("trigger = %s" % tstr)
        tstr = tstr.replace("[", "#").replace("]", "#")
        r_list = tstr.split("#")
        data["trigger_type"] = r_list[0]
        data["trigger_cond"] = r_list[1]
        response['data'].append(data)

    return HttpResponse(json.dumps(response), content_type='application/json')




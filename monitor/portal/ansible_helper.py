# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
import requests, json, memcache, os
from models import *
from zmqWrapper import *
from monitorLog import *
logger = getMonitorLogger()

from monitor.settings import ANSIBLE_PATH

def ansible_gen_net_inventory():
    dynamic_inventory = {}
    stype_objs = mn_DeviceType.objects.all()
    for st in stype_objs:
        dynamic_inventory[st.type_name] = []

    sobjs = mn_NetDevices.objects.all()
    for so in sobjs:
        if so.device_type != "" and dynamic_inventory.has_key(so.device_type):
            dynamic_inventory[so.device_type].append(so.device_ip)

    output = json.dumps(dynamic_inventory)
    return output

def ansible_gen_inventory(encode):
    dynamic_inventory = {}
    stype_objs = mn_ServerGroup.objects.all()
    for st in stype_objs:
        dynamic_inventory[st.group_name] = []

    sobjs = mn_Servers.objects.all()
    for so in sobjs:
        if so.sgroup1 != "" and dynamic_inventory.has_key(so.sgroup1):
            dynamic_inventory[so.sgroup1].append(so.sip)
        if so.sgroup2 != "" and dynamic_inventory.has_key(so.sgroup2):
            dynamic_inventory[so.sgroup2].append(so.sip)
        if so.sgroup3 != "" and dynamic_inventory.has_key(so.sgroup3):
            dynamic_inventory[so.sgroup3].append(so.sip)
        if so.sgroup4 != "" and dynamic_inventory.has_key(so.sgroup4):
            dynamic_inventory[so.sgroup4].append(so.sip)

    if encode == 'html':
        output = json.dumps(dynamic_inventory, indent=4)
        # output = output.replace("\n", "<br>")
        # output = output.replace(" ", "&nbsp;")
    else:
        output = json.dumps(dynamic_inventory)
    return output

def ansible_get_git_url():
    git_url = ""
    recs = mn_Ansible_git_para.objects.all()
    if recs.count() > 0:
        rec = recs.first()
        git_url = rec.git_url

    return git_url

def ansible_set_git_url(url):
    recs = mn_Ansible_git_para.objects.all()
    if recs.count() > 0:
        rec = recs.first()
        rec.git_url = url
        rec.save()
    else:
        rec = mn_Ansible_git_para(
            git_url = url,
        )
        rec.save()

def ansible_do_git_pull():
    url = ansible_get_git_url()
    prj_name = url.split('/')[-1].split('.')[0]
    if os.path.exists(ANSIBLE_PATH + prj_name):
        cmd = "cd " + ANSIBLE_PATH + prj_name + " && git pull "
    else:
        cmd = "cd " + ANSIBLE_PATH + " && git clone --progress " + url

    # send cmd to monitord
    message = {}
    message['type'] = "command"
    message["cmd"] = cmd
    message["before_prompt"] = "现在开始下载更新代码, ... ..."
    message["after_prompt"]  = "现在可以刷新页面了!"
    _message = json.dumps(message)
    zmq_send('127.0.0.1', _message, MONITORD_CMD_QUEUE_PORT)
    logger.error("--- --- ---zmq: send %s/%s to monitord_cmdConsumer sucessfully")

# {
#     "routine": [
#         {"name": '', "desc": ''},
#         {"name": '', "desc": ''},
#     ],
#     "alert": [
#         {"name": '', "desc": ''},
#         {"name": '', "desc": ''},
#     ],
# }
def ansible_get_roles():
    r_st = u"/playbook/routine/roles/"
    a_st = u"/playbook/alert/roles/"
    desc_str = u"README.md"

    result = {
        "routine": [],
        "alert"  : []
    }
    url = ansible_get_git_url()
    if len(url) < 7:
        return result

    prj_name = url.split('/')[-1].split('.')[0]
    prj_path = ANSIBLE_PATH + prj_name
    if  os.path.exists(prj_path) and os.path.exists(prj_path+r_st):
        # get routine list and desc
        r_list = sorted(os.listdir(prj_path+r_st))
        for r in r_list:
            filepath = prj_path + r_st +  r + '/' + desc_str
            content = "任务说明:无"
            if os.path.exists(filepath):
                with open(filepath, "r") as freadme:
                    content = freadme.read()

            recs = mn_routine_op_history.objects.filter(action_name=r)
            op_histories = []
            for rec in recs:
                op_histories.append(rec.group_name + "/" + rec.target_name)

            data = {
                "name": r,
                "desc": content.replace("\n", "<br>"),
                "histories": op_histories
                # "histories": ["webserver", "192.168.0.1", "dns"],
            }
            result["routine"].append(data)

        # get alert list and desc
        a_list = sorted(os.listdir(prj_path+a_st))
        for a in a_list:
            filepath = prj_path + a_st + a + '/' + desc_str
            content = "任务说明:无"
            if os.path.exists(filepath):
                with open(filepath, "r") as freadme:
                    content = freadme.read()

            data = {
                "name": a,
                "desc": content.replace("\n", "<br>")
            }
            result["alert"].append(data)

    return result

def ansible_get_alert_by_rules():
    alist = []
    with open("/storage/config/alert.rules") as f:
        lines = f.readlines()
    for line in lines:
        tmp = line.strip().split()
        if len(tmp) > 1 and tmp[0] == "ALERT":
            alist.append(tmp[1])
    return alist

def ansible_get_alerts():
    alert_list = ansible_get_alert_by_rules()
    rlist = []
    recs = mn_alert2action.objects.all()
    for rec in recs :
        rlist.append(rec.alert_name)

    new_alert = filter(lambda x: x not in rlist, alert_list)
    del_alert = filter(lambda x: x not in alert_list, rlist)

    #delete obselote alert
    for d in del_alert:
        mn_alert2action.object.filter(alert_name=d).first().delete()

    if len(new_alert) > 0:
        actions = []
        for l in new_alert:
            new_rec = mn_alert2action(
                alert_name=l,
                alert_actions=json.dumps(actions))
            new_rec.save()

    return alert_list


def find_alert_handler_by_name(hname, hroles):
    for hr in hroles:
        if hr["name"] == hname:
           return hr
    return {}


# [
#     {
#         "alert_name": "jfdklsa",
#         "alert_handler": [
#             {"name": "", "desc": ""}
#         ]
#     },
# ]
def ansible_get_alert2handler():
    result = []
    recs = mn_alert2action.objects.all()
    roles = ansible_get_roles()
    for rec in recs :
        data = {}
        data["alert_name"] = rec.alert_name
        data["alert_handler"] = []
        actions = json.loads(rec.alert_actions)
        for ha in actions:
            ah= find_alert_handler_by_name(ha, roles["alert"])
            data["alert_handler"].append(ah)
        result.append(data)

    return result

def ansible_add_action_2_alert(aname, hname):
    rec = mn_alert2action.objects.filter(alert_name=aname).first()
    actions = json.loads(rec.alert_actions)
    actions.append(hname)
    tmp = []
    for x in actions:
        if x not in tmp:
            tmp.append(x)
    rec.alert_actions = json.dumps(tmp)
    rec.save()

def ansible_del_action_2_alert(aname, hname):
    rec = mn_alert2action.objects.filter(alert_name=aname).first()
    actions = json.loads(rec.alert_actions)
    actions.remove(hname)
    rec.alert_actions = json.dumps(actions)
    rec.save()


def get_host_username_and_password(group ,host):
    #net_inventories    = ansible_gen_net_inventory()
    server_inventories = json.loads(ansible_gen_inventory('json'))
    #if host in list(net_inventories.keys()):
    #    bIsIP = 0

    if host == "all":
        ip = server_inventories[group][0]
    else:
        ip = host

    rec = mn_Servers.objects.filter(sip=ip).first()
    return rec.sadmin, rec.spasswd

def ansible_routine_run_once(op, group, entity):
    recs = mn_routine_op_history.objects.filter(action_name=op, group_name=group, target_name=entity)
    if recs.count() > 0:
        rec = recs.first()
        rec.invoke_times += 1
        rec.save()
    else:
        rec = mn_routine_op_history(
            action_name=op,
            group_name =group,
            target_name=entity,
            invoke_times=1
        )
        rec.save()

    # send cmd to monitord
    url = ansible_get_git_url()
    prj_name = url.split('/')[-1].split('.')[0]
    message = {}
    message['type'] = "routine"
    message["role"] = op
    message["group"]= group
    message["host"] = entity
    message["src_path"] = ANSIBLE_PATH + prj_name
    message['username'], message['password'] = get_host_username_and_password(group, entity)
    message["before_prompt"] = "Ansible Routine Operation start ... ..."
    message["after_prompt"]  = "Ansible Routine Operation finished."
    _message = json.dumps(message)
    zmq_send('127.0.0.1', _message, MONITORD_CMD_QUEUE_PORT)

def ansible_alert_take_over(hosts, ops):
    url = ansible_get_git_url()
    prj_name = url.split('/')[-1].split('.')[0]
    message = {}
    message['type'] = "alert"
    message["roles"] = ops
    message["hosts"] = hosts
    message["src_path"] = ANSIBLE_PATH + prj_name
    message['username'], message['password'] = get_host_username_and_password("", hosts[0])
    message["before_prompt"] = "Ansible Alert Operation start ... ..."
    message["after_prompt"]  = "Ansible Alert Operation finished."
    _message = json.dumps(message)
    zmq_send('127.0.0.1', _message, MONITORD_CMD_QUEUE_PORT)
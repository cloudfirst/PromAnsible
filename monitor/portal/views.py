# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
import os
import requests, json, yaml
from yaml_helper import *
from ansible_helper import *
from wechatapi import *
from models import *

from monitorLog import *
logger = getMonitorLogger()

# Create your views here.
def index(request):
    return render(request, 'portal/index.html', {})

def portal_adm_login(request):
    context = {
    }
    return render(request, 'portal/adm_login.html', context)

def admin_login(request):
    response = {}
    username = request.POST['email']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        response['status'] = "SUCCESS"
        response['url'] = "/portal/manage"
        return HttpResponse(json.dumps(response), content_type='application/json')
    else:
        # Return an 'invalid login' error message.
        response['status'] = "FAILURE"
        response['reason'] = "账号或密码错误！"
        return HttpResponse(json.dumps(response), content_type='application/json')

@login_required(login_url='/portal/admlogin')
def edit_password(request, uid):
    context = {
        'uid': uid,
    }
    return render(request, 'portal/reset_account_password.html', context)

@login_required(login_url='/portal/admlogin')
def account_reset_password(request):
    flag = False
    uid = request.POST['userid']
    oldpw = request.POST['oldpassword']
    newpw = request.POST['newpassword']

    # verify old password
    response = {}
    user = authenticate(username=uid, password=oldpw)
    if user is not None:
        flag = True

    if flag:
         # set new password
        user.set_password(newpw)
        user.save()

        response['Result'] = "OK"
        return HttpResponse(json.dumps(response), content_type='application/json')
    else:
        # Return an 'invalid login' error message.
        response['Result'] = "FAILURE"
        response['errormsg'] = _("Password is not correct!")
        return HttpResponse(json.dumps(response), content_type='application/json')

@login_required(login_url='/portal/admlogin')
def user_logout(request):
    logout(request)
    return render(request, 'portal/index.html', {})

# main entry for administrator management
@login_required(login_url='/portal/admlogin')
def manage(request):
    return settings(request)

@login_required(login_url='/portal/admlogin')
def settings(request):
    context = {
        'uid': request.user,
        'showname': request.user,
        'dashboard': "系统参数设置",
    }
    return render(request, 'portal/settings.html', context)

def device_type_add(request):
    rec = mn_DeviceType(
        type_name = request.POST["type_name"]
    )
    rec.save()

    response = {}
    response["Result"] = "OK"
    return HttpResponse(json.dumps(response), content_type='application/json')

def device_type_edit(request):
    rec = mn_DeviceType.objects.filter(type_name=request.POST["old_type_name"]).first()
    rec.type_name = request.POST["new_type_name"]
    rec.save()

    response = {}
    response["Result"] = "OK"
    return HttpResponse(json.dumps(response), content_type='application/json')

def device_type_del(request):
    typename = request.POST["type_name"]
    rec = mn_DeviceType.objects.filter(type_name=typename).first()
    rec.delete()

    response = {}
    response["Result"] = "OK"
    return HttpResponse(json.dumps(response), content_type='application/json')

def device_type_list(request):
    draw  = request.GET['draw']
    start = request.GET['start']
    response = {}

    dt_list = mn_DeviceType.objects.all()
    response['draw'] = draw
    response['recordsTotal'] = dt_list.count()
    response['recordsFiltered'] = dt_list.count()
    response['data'] = []
    for dt in dt_list:
        data = ["",]
        data.append(dt.type_name)
        response['data'].append(data)

    return HttpResponse(json.dumps(response), content_type='application/json')

def server_group_add(request):
    rec = mn_ServerGroup(
        group_name = request.POST["group_name"],
        listen_port= int(request.POST["group_port"])
    )
    rec.save()

    response = {}
    response["Result"] = "OK"
    return HttpResponse(json.dumps(response), content_type='application/json')

def server_group_edit(request):
    rec = mn_ServerGroup.objects.filter(group_name=request.POST["old_server_group_name"]).first()
    rec.group_name = request.POST["new_server_group_name"]
    rec.listen_port= int(request.POST["new_server_group_port"])
    rec.save()

    response = {}
    response["Result"] = "OK"
    return HttpResponse(json.dumps(response), content_type='application/json')

def server_group_del(request):
    groupname = request.POST["group_name"]
    rec = mn_ServerGroup.objects.filter(group_name=groupname).first()
    rec.delete()

    response = {}
    response["Result"] = "OK"
    return HttpResponse(json.dumps(response), content_type='application/json')

def server_group_list(request):
    draw  = request.GET['draw']
    start = request.GET['start']
    response = {}

    dt_list = mn_ServerGroup.objects.all()
    response['draw'] = draw
    response['recordsTotal'] = dt_list.count()
    response['recordsFiltered'] = dt_list.count()
    response['data'] = []
    for dt in dt_list:
        data = ["",]
        data.append(dt.group_name)
        data.append(dt.listen_port)
        response['data'].append(data)

    return HttpResponse(json.dumps(response), content_type='application/json')

def os_type_add(request):
    rec = mn_OSTypes(
        ostype = request.POST["os_type"]
    )
    rec.save()

    response = {}
    response["Result"] = "OK"
    return HttpResponse(json.dumps(response), content_type='application/json')

def os_type_edit(request):
    rec = mn_OSTypes.objects.filter(ostype=request.POST["old_os_type_name"]).first()
    rec.ostype = request.POST["new_os_type_name"]
    rec.save()

    response = {}
    response["Result"] = "OK"
    return HttpResponse(json.dumps(response), content_type='application/json')

def os_type_del(request):
    os_type = request.POST["os_type"]
    rec = mn_OSTypes.objects.filter(ostype=os_type).first()
    rec.delete()

    response = {}
    response["Result"] = "OK"
    return HttpResponse(json.dumps(response), content_type='application/json')

def os_type_list(request):
    draw  = request.GET['draw']
    start = request.GET['start']
    response = {}

    dt_list = mn_OSTypes.objects.all()
    response['draw'] = draw
    response['recordsTotal'] = dt_list.count()
    response['recordsFiltered'] = dt_list.count()
    response['data'] = []
    for dt in dt_list:
        data = ["",]
        data.append(dt.ostype)
        response['data'].append(data)

    return HttpResponse(json.dumps(response), content_type='application/json')

@login_required(login_url='/portal/admlogin')
def netdevices(request):
    types_obj = mn_DeviceType.objects.all()
    types = []
    for obj in types_obj:
        types.append(obj.type_name)

    nds = mn_NetDevices.objects.all()
    recs = []
    for nd in nds:
        rec = {}
        rec["device_type"] = nd.device_type
        rec["device_ip"]   = nd.device_ip
        rec["device_mac"]  = nd.device_mac
        rec["memo"]        = nd.memo
        recs.append(rec)

    context = {
        'uid': request.user,
        'showname': request.user,
        'dashboard': "网络设备管理",
        "deviceTypes": types,
        "recs": recs
    }
    return render(request, 'portal/netdevices.html', context)

def net_device_list(request):
    draw  = request.GET['draw']
    start = request.GET['start']
    response = {}

    dt_list = mn_NetDevices.objects.all()
    response['draw'] = draw
    response['recordsTotal'] = dt_list.count()
    response['recordsFiltered'] = dt_list.count()
    response['data'] = []
    for dt in dt_list:
        data = []
        data.append(dt.device_type)
        data.append(dt.device_ip)
        data.append(dt.device_mac)
        data.append(dt.memo)
        response['data'].append(data)

    return HttpResponse(json.dumps(response), content_type='application/json')

def net_device_add(request):
    rec = mn_NetDevices(
        device_type = request.POST['net_device_type'],
        device_ip   = request.POST['net_device_ip'],
        device_mac  = request.POST['net_device_mac'],
        memo        = request.POST['net_device_memo'],
    )
    rec.save()

    response = {}
    response["Result"] = "OK"
    return HttpResponse(json.dumps(response), content_type='application/json')

def net_device_edit(request):
    rec = mn_NetDevices.objects.filter(device_ip=request.POST["old_net_device_ip"]).first()
    rec.device_type = request.POST["new_net_device_type"]
    rec.device_ip   = request.POST["new_net_device_ip"]
    rec.device_mac  = request.POST["new_net_device_mac"]
    rec.memo        = request.POST["new_net_device_memo"]
    rec.save()

    response = {}
    response["Result"] = "OK"
    return HttpResponse(json.dumps(response), content_type='application/json')

def net_device_del(request):
    rec = mn_NetDevices.objects.filter(device_ip = request.POST["device_ip"]).first()
    rec.delete()

    response = {}
    response["Result"] = "OK"
    return HttpResponse(json.dumps(response), content_type='application/json')

@login_required(login_url='/portal/admlogin')
def servers(request):
    group_objs = mn_ServerGroup.objects.all()
    sgs = []
    for obj in group_objs:
        sgs.append(obj.group_name)

    sostype_objs = mn_OSTypes.objects.all()
    sos = []
    for obj in sostype_objs:
        sos.append(obj.ostype)

    nds = mn_Servers.objects.all()
    recs = []
    for nd in nds:
        rec = {}
        rec["sip"]     = nd.sip
        rec["smac"]    = nd.smac
        rec["sostype"] = nd.sostype
        rec["smodel"]  = nd.smodel
        rec["sadmin"]  = nd.sadmin
        # rec["spasswd"] = nd.spasswd
        # rec["sgroup1"] = nd.sgroup1
        # rec["sgroup2"] = nd.sgroup2
        # rec["sgroup3"] = nd.sgroup3
        # rec["sgroup4"] = nd.sgroup4

        rec["sgroup"]  = ""
        if nd.sgroup1 != "":
            rec["sgroup"] += nd.sgroup1
        if nd.sgroup2 != "":
            rec["sgroup"] += "," + nd.sgroup2
        if nd.sgroup3 != "":
            rec["sgroup"] += "," + nd.sgroup3
        if nd.sgroup4 != "":
            rec["sgroup"] += "," + nd.sgroup4

        rec["memo"]    = nd.memo

        recs.append(rec)

    context = {
        'uid': request.user,
        'showname': request.user,
        'dashboard': "服务器管理",
        "sgroups": sgs,
        "sos":     sos,
        "recs":    recs
    }
    return render(request, 'portal/servers.html', context)

def servers_list(request):
    pass

def servers_add(request):
    rec = mn_Servers(
        sip     = request.POST["sip"],
        smac    = request.POST["smac"],
        sostype = request.POST["sostype"],
        smodel  = request.POST["smodel"],
        sadmin  = request.POST["sadmin"],
        spasswd = request.POST["spasswd"],
        sgroup1 = request.POST["sgroup1"],
        sgroup2 = request.POST["sgroup2"],
        sgroup3 = request.POST["sgroup3"],
        sgroup4 = request.POST["sgroup4"],
        memo    = request.POST["smemo"],
    )
    rec.save()

    response = {}
    response["Result"] = "OK"
    return HttpResponse(json.dumps(response), content_type='application/json')

def servers_edit(request):
    rec = mn_Servers.objects.filter(sip=request.POST["old_sip"]).first()
    rec.sip = request.POST["sip"]
    rec.smac = request.POST["smac"]
    rec.sostype = request.POST["sostype"]
    rec.smodel = request.POST["smodel"]
    rec.sadmin = request.POST["sadmin"]
    if request.POST["spasswd"] != "":
        rec.spasswd = request.POST["spasswd"]
    rec.sgroup1 = request.POST["sgroup1"]
    rec.sgroup2 = request.POST["sgroup2"]
    rec.sgroup3 = request.POST["sgroup3"]
    rec.sgroup4 = request.POST["sgroup4"]
    rec.memo    = request.POST["smemo"]
    rec.save()

    response = {}
    response["Result"] = "OK"
    return HttpResponse(json.dumps(response), content_type='application/json')

def servers_del(request):
    rec = mn_Servers.objects.filter(sip=request.POST["sip"]).first()
    rec.delete()

    response = {}
    response["Result"] = "OK"
    return HttpResponse(json.dumps(response), content_type='application/json')

@login_required(login_url='/portal/admlogin')
def alertman(request):
    pass

@login_required(login_url='/portal/admlogin')
def snmpman(request):
    pass

@login_required(login_url='/portal/admlogin')
def wechatman(request):
    recs = mn_Enterprise_wechat.objects.all()
    data = {}
    if recs.count() > 0:
        bconfigured = 1
        rec = recs.first()
        data["corp_id"]     = rec.corp_id
        data["app_secret"]  = rec.app_secret
        data["app_id"]      = rec.app_id
        data["user_ids"]    = rec.user_ids
    else:
        bconfigured = 0

    context = {
        'uid':          request.user,
        'showname':     request.user,
        'dashboard':    "微信企业号设置",
        "bconfigured":  bconfigured,
        "data":         data,
    }
    return render(request, 'portal/enterprise_wechat.html', context)

def upload_wechat(request):
    uf = request.FILES["myfile"]
    with open("/storage/static/wechat/erweima.png", 'w') as df:
        for chunk in uf.chunks():
            df.write(chunk)

    response = ["/storage/static/wechat/erweima.png"]
    return HttpResponse(json.dumps(response), content_type='application/json')

def edit_wechat(request):
    recs = mn_Enterprise_wechat.objects.all()
    if recs.count() > 0:
        # edit record
        rec = recs.first()
        rec.corp_id     = request.POST["corp_id"]
        rec.app_id      = int(request.POST["app_id"])
        rec.app_secret  = request.POST["app_secret"]
        rec.user_ids    = request.POST["user_ids"]
        rec.save()
    else:
        # new record
        rec = mn_Enterprise_wechat(
            corp_id     = request.POST["corp_id"],
            app_id      = int(request.POST["app_id"]),
            app_secret  = request.POST["app_secret"],
            user_ids    = request.POST["user_ids"]
        )
        rec.save()

    response = {}
    response["Result"] = "OK"
    return HttpResponse(json.dumps(response), content_type='application/json')


@login_required(login_url='/portal/admlogin')
def ansibleman(request):
    context = {
        'uid':          request.user,
        'showname':     request.user,
        'dashboard':    "自动化管理设置(Ansible)",
        "git_url":      ansible_get_git_url(),
        "roles"  :      ansible_get_roles(),
    }
    return render(request, 'portal/ansible.html', context)

def gen_wizard_context_tables():
    inventories = json.loads(ansible_gen_inventory('json'))
    netdevices = json.loads(ansible_gen_net_inventory())

    l_table = []
    for n in list(netdevices.keys()):
        data = {
            "category": "net_device",
            "type": n,
        }
        l_table.append(data)
    for i in list(inventories.keys()):
        data = {
            "category": "server_device",
            "type": i,
        }
        l_table.append(data)

    r_table = []
    for n in list(netdevices.keys()):
        entities = netdevices[n]
        for e in entities:
            data = {}
            data["type"] = n
            data["ip"] = e
            r_table.append(data)
    for s in inventories:
        entities = inventories[s]
        for e in entities:
            data = {}
            data["type"] = s
            data["ip"] = e
            r_table.append(data)



    return l_table, r_table

@login_required(login_url='/portal/admlogin')
def set_devops_schedule(request,title):
    ltable, rtable = gen_wizard_context_tables()
    context = {
        'title': title,
        'ltable': ltable,
        'rtable': rtable,
    }
    return render(request, 'portal/routine_run_schedule.html', context)

@login_required(login_url='/portal/admlogin')
def set_devops_target(request, title):
    ltable, rtable = gen_wizard_context_tables()
    context = {
        'title': title,
        'ltable': ltable,
        'rtable': rtable,
    }
    return render(request, 'portal/routine_run_once.html', context)

@login_required(login_url='/portal/admlogin')
def aiman(request):
    context = {
        'uid':          request.user,
        'showname':     request.user,
        'dashboard':    "报警自动处理",
        "alerts":       ansible_get_alerts(),
        "roles":        ansible_get_roles(),
        "a2hs":         ansible_get_alert2handler()
    }
    return render(request, 'portal/aiman.html', context)

from monitor.settings import DEBUG
@login_required(login_url='/portal/admlogin')
def apscheduleman(request):
    if DEBUG == True:
        url = "http://127.0.0.1:8000/schedule/api/1.0/cron/list"
    else:
        url = "http://127.0.0.1/schedule/api/1.0/cron/list"

    r = requests.get(url)
    ret = json.loads(r.content)
    context = {
        'uid':          request.user,
        'showname':     request.user,
        'dashboard':    "计划任务管理",
        "schetasks":    ret['data'],
    }
    return render(request, 'portal/apscheduleman.html', context)

def save_yml(request, target):
    tmpfile = "/tmp/test.yml"
    if target == "prometheus":
        fname = "/storage/config/prometheus.yml"
        sname = "prometheus-server"
        cmd   = "promtool check-config " + tmpfile
    if target == "alertman":
        fname = "/storage/config/alertman.yml"
        sname = "alertman-server"
        cmd   = ""
    if target == "alertrule":
        fname = "/storage/config/alert.rules"
        sname = "alertman-server"
        tmpfile = "/tmp/test.rules"
        cmd = "promtool check-rules " + tmpfile
    if target == "snmpman":
        fname = "/storage/config/snmp.yml"
        sname = "snmp_exporter"
        cmd   = ""

    src_code = request.POST["src"]
    src_code = src_code.encode('UTF-8')

    with open(tmpfile, 'w') as f:
        f.write(src_code)

    # verify syntax of /tmp/test.yml
    response = {}
    import commands
    if cmd != "":
        out = commands.getoutput(cmd)
        if out.find("SUCCESS") > 0:
            response["Result"] = "OK"
            response["error"]  = out
            os.system("cp " + tmpfile + " " + fname)
            os.system("sudo supervisorctl restart " + sname)
        else:
            response["Result"] = "FAIL"
            response["error"] = out
    else:
        try:
            conf = yaml.safe_load(tmpfile)
            response["Result"] = "OK"
            response["error"] = ""
            os.system("cp " + tmpfile + " " + fname)
            os.system("sudo supervisorctl restart " + sname)
        except yaml.YAMLError as e:
            response["Result"] = "FAIL"
            response["error"] = str(e)

    return HttpResponse(json.dumps(response), content_type='application/json')

def gen_yaml():
    pass


def config_prometheus(request):
    context = {
        'uid': request.user,
        'showname': request.user,
        'dashboard': "监控服务设置",

    }
    return render(request, 'portal/prometheus.html', context)

def config_edit_yaml(request, target):
    if target == "prometheus":
        fname = "/storage/config/prometheus.yml"
    if target == "alertman":
        fname = "/storage/config/alertman.yml"
    if target == "alertrule":
        fname = "/storage/config/alert.rules"
    if target == "snmpman":
        fname = "/storage/config/snmp.yml"

    with open(fname, 'r') as content_file:
        tcontent =  content_file.read()
    context = {
        "source_code": tcontent
    }
    return render(request, 'portal/yamleditor.html', context)

# generate prometheus.yml
# one type of server group is a job
def config_gen_yaml(request):
    snmp_flag = False
    netdevices = mn_NetDevices.objects.all()
    net_devices_list = []
    for nd in netdevices:
        net_devices_list.append(nd.device_ip)

    if len(net_devices_list) > 0:
        snmp_flag = True
        snmp_job = yaml.safe_load(TEMPLATE_SNMP)
        snmp_job = add_target_to_snmp_job(net_devices_list, snmp_job)


    # generate jobs
    machine_flag = False
    pyml = yaml.safe_load(TEMPLATE_SCRAPE)

    inventories = json.loads(ansible_gen_inventory('json'))
    jobs = inventories.keys()

    for job in jobs:
        s_list = inventories[job]
        s_port = mn_ServerGroup.objects.filter(group_name=job).first().listen_port
        if s_port == 0:
            continue

        if len(s_list) > 0:
            machine_flag = True
            newjob = create_job(job)
            for sip in s_list:
                new_t = create_target(sip + ":" + str(s_port), job+"_exporter")
                newjob = add_target_to_job(new_t, newjob)
            pyml['scrape_configs'].append(newjob)

    with open(PROMETHEUS_CONF, 'w') as the_file:
        the_file.write(TEMPLATE_GLOABLE)
        the_file.write(TEMPLATE_RULE)
        
        if not machine_flag and not snmp_flag:
            the_file.write(TEMPLATE_SCRAPE)
        if machine_flag and not snmp_flag:
            content = yaml.safe_dump(pyml, default_flow_style=False)
            the_file.write(content)
        if not machine_flag and snmp_flag:
            snmp_content = yaml.safe_dump(snmp_job, default_flow_style=False)
            the_file.write(snmp_content)
        if machine_flag and snmp_flag:
            content = yaml.safe_dump(pyml, default_flow_style=False)
            snmp_content = yaml.safe_dump(snmp_job['scrape_configs'], default_flow_style=False)
            the_file.write(content)
            the_file.write(snmp_content)

        the_file.write(TEMPLATE_ALERT)

    os.system("sudo supervisorctl restart prometheus-server")

    response = {}
    response["Result"] = "OK"
    return HttpResponse(json.dumps(response), content_type='application/json')

def config_alertman(request):
    context = {
        'uid': request.user,
        'showname': request.user,
        'dashboard': "报警服务设置",

    }
    return render(request, 'portal/alertman.html', context)

def config_alertrule(request):
    context = {
        'uid': request.user,
        'showname': request.user,
        'dashboard': "报警规则设置",

    }
    return render(request, 'portal/alertrule.html', context)

def config_snmp(request):
    context = {
        'uid': request.user,
        'showname': request.user,
        'dashboard': "SNMP监控设置",

    }
    return render(request, 'portal/snmpman.html', context)

def config(request):
    clcip = request.POST["clcip"]

    #0. save CONF_PATH
    with open(CONF_PATH, 'w') as the_file:
        the_file.write(clcip)

    #1. get machine list by clcip
    url = "http://%s/clc/api/1.0/servers/list/all" % (clcip)
    r = requests.get(url)
    result = json.loads(r.content)

    if result["arch"] == "allinone":
        # only one node to monitor
        clcip = result["mlist"]
        yaml_conf = yaml.safe_load(TEMPLATE_SCRAPE)
        newjob = create_job("node")
        new_t = create_target(clcip+":9100", "allinone")
        newjob = add_target_to_job(new_t, newjob)
        yaml_conf['scrape_configs'].append(newjob)

    if result["arch"] == "singlecluster":
        # only one clc and multiple ncs to monitor
        clcip = result["mlist"]["clc"]
        yaml_conf = yaml.safe_load(TEMPLATE_SCRAPE)
        newjob = create_job("node")
        new_t = create_target(clcip + ":9100", "singlecluster-clc")
        newjob = add_target_to_job(new_t, newjob)

        ncs   = result["mlist"]["ncs"]
        for nc in ncs:
            new_t = create_target(nc + ":9100", "singlecluster-nc")
            newjob = add_target_to_job(new_t, newjob)

        yaml_conf['scrape_configs'].append(newjob)

    if result["arch"] == "dist":
        # only one clc, multiple ccs, and multiple ncs to monitor
        clcip = result["mlist"]["clc"]
        yaml_conf = yaml.safe_load(TEMPLATE_SCRAPE)
        newjob = create_job("node")
        new_t = create_target(clcip + ":9100", "clc")
        newjob = add_target_to_job(new_t, newjob)

        ccs = result["mlist"]["ccs"]
        for cc in ccs:
            new_cc_t = create_target(cc['ccip'] + ":9100", cc['ccname']+'-cc')
            newjob = add_target_to_job(new_cc_t, newjob)

            ncs = cc['ncs']
            for nc in ncs:
                new_nc_t = create_target(nc + ":9100", cc['ccname']+"-nc")
                newjob = add_target_to_job(new_nc_t, newjob)

        yaml_conf['scrape_configs'].append(newjob)

    content = yaml.safe_dump(yaml_conf, default_flow_style=False)

    #2. build snmp yaml config
    snmp_job = yaml.safe_load(TEMPLATE_SNMP)
    #snmp_target = ['192.168.96.254', '129.168.0.10']
    #snmp_job = add_target_to_snmp_job(snmp_target, snmp_job)
    snmp_content = yaml.safe_dump(snmp_job['scrape_configs'], default_flow_style=False)

    with open(PROMETHEUS_CONF, 'w') as the_file:
        the_file.write(TEMPLATE_GLOABLE)
        the_file.write(TEMPLATE_RULE)
        the_file.write(content)
        the_file.write(snmp_content)
        the_file.write(TEMPLATE_ALERT)

    #3. restart prometheus server
    os.system("sudo supervisorctl restart prometheus-server")

    response = {}
    response['Result'] = "OK"
    return HttpResponse(json.dumps(response), content_type='application/json')

# JOB: NODESTATUS
# {
#     "status": "firing",
#     "groupLabels": {
#         "alertname": "service_down"
#     },
#     "groupKey": "{}:{alertname=\"service_down\"}",
#     "commonAnnotations": {
#         "summary": "Instance 10.147.17.35:9100 is down"
#     },
#     "alerts": [
#         {
#             "status": "firing",
#             "labels": {
#                 "instance": "10.147.17.35:9100",
#                 "job": "node",
#                 "group": "allinone",
#                 "monitor": "codelab-monitor",
#                 "alertname": "service_down",
#                 "urgency": "immediate"
#             },
#             "endsAt": "0001-01-01T00:00:00Z",
#             "generatorURL": "http://SRE:9090/graph?g0.expr=up+%3D%3D+0&g0.tab=0",
#             "startsAt": "2017-07-26T10:47:22.808+08:00",
#             "annotations": {
#                 "summary": "Instance 10.147.17.35:9100 is down"
#             }
#         }
#     ],
#     "version": "4",
#     "receiver": "luhya",
#     "externalURL": "http://SRE:9093",
#     "commonLabels": {
#         "instance": "10.147.17.35:9100",
#         "job": "node",
#         "group": "allinone",
#         "monitor": "codelab-monitor",
#         "alertname": "service_down",
#         "urgency": "immediate"
#     }
# }

#  JOB: SNMP
# {
#     "status": "resolved",
#     "groupLabels": {
#         "alertname": "service_down"
#     },
#     "groupKey": "{}:{alertname=\"service_down\"}",
#     "commonAnnotations": {},
#     "alerts": [
#         {
#             "status": "resolved",
#             "labels": {
#                 "instance": "192.168.96.254",
#                 "job": "snmp",
#                 "monitor": "codelab-monitor",
#                 "alertname": "service_down"
#             },
#             "endsAt": "2017-07-25T23:53:52.807551974+08:00",
#             "generatorURL": "http://SRE:9090/graph?g0.expr=up+%3D%3D+0&g0.tab=0",
#             "startsAt": "2017-07-25T23:52:52.804+08:00",
#             "annotations": {
#                 "summary": "Instance 192.168.96.254 is down"
#             }
#         },
#         {
#             "status": "resolved",
#             "labels": {
#                 "instance": "192.168.96.1",
#                 "job": "snmp",
#                 "monitor": "codelab-monitor",
#                 "alertname": "service_down"
#             },
#             "endsAt": "2017-07-25T23:53:52.807551974+08:00",
#             "generatorURL": "http://SRE:9090/graph?g0.expr=up+%3D%3D+0&g0.tab=0",
#             "startsAt": "2017-07-25T23:52:52.804+08:00",
#             "annotations": {
#                 "summary": "Instance 192.168.96.1 is down"
#             }
#         }
#     ],
#     "version": "4",
#     "receiver": "luhya",
#     "externalURL": "http://SRE:9093",
#     "commonLabels": {
#         "job": "snmp",
#         "monitor": "codelab-monitor",
#         "alertname": "service_down"
#     }
# }
def formate_time(timestring):
    # timestring is as 2017-07-25T23:52:52.804+08:00
    # return as 2017-07-25 23:52:52
    mydate, mytime = timestring.split("T")
    mytime = mytime.split(".")[0]

    return mydate + " " + mytime

def alertDelHandler(request):
    aname = request.POST["aname"]
    hname = request.POST["hname"]

    ansible_del_action_2_alert(aname, hname)

    response = {}
    response['Result'] = "OK"
    return HttpResponse(json.dumps(response), content_type='application/json')

def alertAddHandler(request):
    aname = request.POST["aname"]
    hname = request.POST["hname"]

    ansible_add_action_2_alert(aname, hname)

    response = {}
    response['Result'] = "OK"
    return HttpResponse(json.dumps(response), content_type='application/json')

def getPreDefinedAlertHandlers(alert_name):
    ops = []
    a2hs = ansible_get_alert2handler()
    for a2h in a2hs:
        if a2h["alert_name"] == alert_name:
            if len(a2h["alert_handler"]) > 0:
                for op in a2h["alert_handler"]:
                    ops.append(op["name"])
            break
    return ops

# {
#     "role":
#     "role_desc":
#     "time":
#     "targets":
# }
def alertByAnsible(request):
    data = []
    data.append("!!!Ansible警报发生!!!")
    data.append("\n\n报警内容:\n" + request.POST["role"])
    data.append("\n\n详细内容:\n" + request.POST["role_desc"])
    data.append("\n\n报警时间:\n" + request.POST["time"])
    data.append("\n\n报警目标:\n" + request.POST["targets"])
    data.append("\n")

    ulist = get_user_list()
    wechat_msg = ''.join(data)
    logger.error("ansible alert message will be send to %s" % json.dumps(ulist))
    send_text_msg(ulist, wechat_msg)
    logger.error("below is the ansible alert message\n%s" % wechat_msg)

    response = {}
    response['Result'] = "OK"
    logger.error("--- leave alertHandler()")
    return HttpResponse(json.dumps(response), content_type='application/json')

def wechat_handler(alert_msg):
    # route it to rigth place
    data = []
    if alert_msg["status"] == "firing":
        data.append("!!!警报发生!!!")
    if alert_msg["status"] == "resolved":
        data.append("~~~警报解除~~~")
    data.append("\n" + alert_msg['commonLabels']['title'])
    for alert in alert_msg['alerts']:
        data.append("\n\n报警内容:\n" + alert['annotations']['summary'])
        data.append("\n\n详细内容:\n" + alert['annotations']['description'])
        data.append("\n\n报警时间:\n" + formate_time(alert['startsAt']))
        if alert['status'] == "resolved":
            data.append("\n\n解决时间:\n" + formate_time(alert['endsAt']))
        else:
            ops = getPreDefinedAlertHandlers(alert_msg["groupLabels"]["alertname"])
            if len(ops) > 0:
                data.append("\n\n自动修复:\n" + "有配置")
            else:
                data.append("\n\n自动修复:\n" + "无配置")
        data.append("\n")

    ulist = get_user_list()
    wechat_msg = ''.join(data)
    logger.error("wechat message will be send to %s" % json.dumps(ulist))
    send_text_msg(ulist, wechat_msg)
    logger.error("below is the wechat message\n%s" % wechat_msg)

def playbook_handler(alert_msg):
    aname = alert_msg["groupLabels"]["alertname"]
    if alert_msg["status"] == "resolved":
        logger.error("Recieved Resolved Alert:%s" % aname)
        return

    logger.error("Recieved Firing Alert:%s" % aname)
    hosts = []
    for alert in alert_msg['alerts']:
        tmp_host = alert["labels"]["instance"]
        tmp_host = tmp_host.split(":")[0]
        hosts.append(tmp_host)

    ops = getPreDefinedAlertHandlers(aname)
    if len(ops) > 0:
        logger.error("Alert %s with predefined handlers." % aname)
        ansible_alert_take_over(hosts, ops)
    else:
        logger.error("Alert %s without predefined handlers." % aname)

def alertHandler(request):
    logger.error("--- enter alertHandler()")
    # get alert message
    alert_msg  = request.body
    alert_msg  = json.loads(alert_msg)
    logger_msg = json.dumps(alert_msg, indent=4)
    logger.error("below is the alert message\n%s" % logger_msg.encode("utf-8"))

    wechat_handler(alert_msg)
    playbook_handler(alert_msg)
    
    # trigger ansible operation if configured.
    response = {}
    response['Result'] = "OK"
    logger.error("--- leave alertHandler()")
    return HttpResponse(json.dumps(response), content_type='application/json')

# ==================
# ansible function
# ==================
def gen_inventory(request):
    if request.POST.has_key("encode"):
        encode = request.POST["encode"]
    else:
        encode = "json"

    data =  ansible_gen_inventory(encode)
    response = {}
    response["Result"] = "OK"
    response["data"]   = data
    return HttpResponse(json.dumps(response), content_type='application/json')

def set_git_url(request):
    git_url = request.POST["git_url"]
    ansible_set_git_url(git_url)

    response = {}
    response["Result"] = "OK"
    return HttpResponse(json.dumps(response), content_type='application/json')

def do_git_pull(request):
    ansible_do_git_pull()

    response = {}
    response["Result"] = "OK"
    return HttpResponse(json.dumps(response), content_type='application/json')

def routine_run_once(request):
    op     = request.POST['op']
    group  = request.POST['group']
    entity = request.POST['entity']

    ansible_routine_run_once(op, group, entity)

    response = {}
    response["Result"] = "OK"
    return HttpResponse(json.dumps(response), content_type='application/json')

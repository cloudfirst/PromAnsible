# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
import requests, json, memcache
from models import *

############################################################
#  Basic API
############################################################
def get_user_list():
    rec = mn_Enterprise_wechat.objects.all().first()
    temp = rec.user_ids.replace(" ", "")
    user_list = temp.split(",")
    return user_list

def get_corp_id():
    rec = mn_Enterprise_wechat.objects.all().first()
    return rec.corp_id

def get_app_secret():
    rec = mn_Enterprise_wechat.objects.all().first()
    return rec.app_secret

def get_app_id():
    rec = mn_Enterprise_wechat.objects.all().first()
    return rec.app_id

def get_access_token():
    flag = False
    access_token = ''
    mc = memcache.Client(['127.0.0.1:11211'], debug=0)
    key = "AccessToken"
    try:
        access_token = mc.get(key)
        if access_token != None:
            flag = True
    except Exception as e:
        pass

    if not flag:
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s' % (get_corp_id(), get_app_secret())
        response = requests.get(url)
        if response.status_code == 200:
            ret = response.content
            ret = json.loads(ret)
            if ret['errmsg'] == 'ok' and ret['errcode'] == 0:
                access_token = ret['access_token']
                mc.set(key, access_token, 7000)

    return access_token
############################################################
#  Member API
############################################################
# member_data =
# {
#    "userid": "zhangsan",
#    "name": "张三",
#    "english_name": "jackzhang"
#    "mobile": "15913215421",
#    "department": [1, 2],
#    "order":[10,40],
#    "position": "产品经理",
#    "gender": "1",
#    "email": "zhangsan@gzdev.com",
#    "isleader": 1,
#    "enable":1,
#    "avatar_mediaid": "2-G6nrLmr5EC3MNb_-zL1dDdzkd0p7cNliYu9V5w7o8K0",
#    "telephone": "020-123456"，
#    "extattr": {"attrs":[{"name":"爱好","value":"旅游"},{"name":"卡号","value":"1234567234"}]}
# }

def create_member(member_data):
    flag = False
    url = 'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=%s' % get_access_token()
    response = requests.post(url, member_data)
    if response.status_code == 200:
        ret = response.content
        ret = json.loads(ret)
        if ret['errcode'] == 0 and ret['errmsg'] == 'created':
            flag = True

    return flag

def get_member(userid):
    url = 'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=%s&userid=%s' % (get_access_token(), userid)
    response = requests.get(url)
    if response.status_code == 200:
        ret = response.content
        ret = json.loads(ret)
        if ret['errmsg'] == 'ok' and ret['errcode'] == 0:
            return ret
        else:
            return ''
    else:
        return ''

def update_member(member_data):
    flag = False
    url = 'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=%s' %  get_access_token()
    response = requests.post(url, member_data)
    if response.status_code == 200:
        ret = response.content
        ret = json.loads(ret)
        if ret['errcode'] == 0 and ret['errmsg'] == 'update':
            flag = True

    return flag

def delete_member(userid):
    flag = False
    url = 'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=%s&userid=%s' % (get_access_token(), userid)
    response = requests.get(url)
    if response.status_code == 200:
        ret = response.content
        ret = json.loads(ret)
        if ret['errcode'] == 0 and ret['errmsg'] == 'deleted':
            flag = True

    return flag

def delete_member_by_batch(userid_list):
    pass

def get_member_by_department(department_id, fetch_id):
    result = []
    url = 'https://qyapi.weixin.qq.com/cgi-bin/user/simplelist?access_token=%s&department_id=%s&fetch_child=%s' \
            % (get_access_token(), department_id, fetch_id)
    response = requests.get(url)
    if response.status_code == 200:
        ret = response.content
        ret = json.loads(ret)
        if ret['errcode'] == 0 and ret['errmsg'] == 'ok':
            result = ret['userlist']

    return result

def get_member_detail_by_department(department_id, fetch_id):
    pass

############################################################
#  Department API
############################################################
# data =
# {
#    "name": "广州研发中心",
#    "parentid": 1,
#    "order": 1,
#    "id": 2 #option
# }
def create_department(data):
    flag = False
    errmsg =  ""
    url = 'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token=%s' % get_access_token()
    response = requests.post(url, data)
    if response.status_code == 200:
        ret = response.content
        ret = json.loads(ret)
        if ret['errcode'] == 0 and ret['errmsg'] == 'created':
            flag = True
        else:
            errmsg = ret['errmsg']

    return flag, errmsg

def update_department(data):
    flag = False
    url = 'https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token=%s' % get_access_token()
    response = requests.post(url, data)
    if response.status_code == 200:
        ret = response.content
        ret = json.loads(ret)
        if ret['errcode'] == 0 and ret['errmsg'] == 'updated':
            flag = True

    return flag

def delete_department(department_id):
    flag = False
    url = 'https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token=%s&id=%s' % (get_access_token(), department_id)
    response = requests.get(url)
    if response.status_code == 200:
        ret = response.content
        ret = json.loads(ret)
        if ret['errmsg'] == 'deleted' and ret['errcode'] == 0:
            flag = True

    return flag

def get_department_list():
    result = []
    url = 'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token=%s' % (get_access_token())
    response = requests.get(url)
    if response.status_code == 200:
        ret = response.content
        ret = json.loads(ret)
        if ret['errmsg'] == 'ok' and ret['errcode'] == 0:
            result =  ret['department']

    return result

############################################################
#  tag API
############################################################
# data =
# {
#    "tagname": "UI",
#    "tagid": 12
# }
def create_tag(data):
    flag = False
    errmsg = ""
    url = 'https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token=%s' % get_access_token()
    response = requests.post(url, data)
    if response.status_code == 200:
        ret = response.content
        ret = json.loads(ret)
        if ret['errcode'] == 0 and ret['errmsg'] == 'created':
            flag = True
        else:
            errmsg = ret["errmsg"]

    return flag, errmsg

def update_tag(data):
    flag = False
    url = 'https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token=%s' % get_access_token()
    response = requests.post(url, data)
    if response.status_code == 200:
        ret = response.content
        ret = json.loads(ret)
        if ret['errcode'] == 0 and ret['errmsg'] == 'updated':
            flag = True

    return flag

def delete_tag(tagid):
    flag = False
    url = 'https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token=%s&tagid=%s' % (get_access_token(), tagid)
    response = requests.get(url)
    if response.status_code == 200:
        ret = response.content
        ret = json.loads(ret)
        if ret['errmsg'] == 'deleted' and ret['errcode'] == 0:
            flag = True

    return flag

# {
#    "errcode": 0,
#    "errmsg": "ok",
#    "userlist": [
#          {
#              "userid": "zhangsan",
#              "name": "李四"
#          }
#      ],
#    "partylist": [2]
# }
def get_users_by_tag(tagid):
    result = []
    url = 'https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token=%s&tagid=%s' % (get_access_token(), tagid)
    response = requests.get(url)
    if response.status_code == 200:
        ret = response.content
        ret = json.loads(ret)
        if ret['errmsg'] == 'ok' and ret['errcode'] == 0:
            result = ret['userlist']

    return result

# data =
# {
#    "tagid": 12,
#    "userlist":[ "user1","user2"],
#    "partylist": [4]
# }
def add_user_by_tag(data):
    flag = False
    ret = {}
    url = 'https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers?access_token=%s' % get_access_token()
    response = requests.post(url, data)
    if response.status_code == 200:
        ret = response.content
        ret = json.loads(ret)
        if ret['errcode'] == 0 and ret['errmsg'] == 'ok':
            flag = True

    return flag, ret

# data =
# {
#    "tagid": 12,
#    "userlist":[ "user1","user2"],
#    "partylist":[2,4]
# }
def delete_user_by_tag(data):
    flag = False
    ret = {}
    url = 'https://qyapi.weixin.qq.com/cgi-bin/tag/deltagusers?access_token=%s' % get_access_token()
    response = requests.post(url, data)
    if response.status_code == 200:
        ret = response.content
        ret = json.loads(ret)
        if ret['errcode'] == 0 and ret['errmsg'] == 'deleted':
            flag = True

    return flag, ret

def get_tag_list():
    result = []
    url = 'https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token=%s' % get_access_token()
    response = requests.get(url)
    if response.status_code == 200:
        ret = response.content
        ret = json.loads(ret)
        if ret['errmsg'] == 'ok' and ret['errcode'] == 0:
            result = ret['taglist']

    return result
############################################################
#  application API
############################################################
# result =
# {
#    "errcode":0,
#    "errmsg":"ok" ,
#    "agentid":"1" ,
#    "name":"NAME" ,
#    "square_logo_url":"xxxxxxxx" ,
#    "description":"desc" ,
#    "allow_userinfos":{
#        "user":[
#              {
#                  "userid":"id1",
#              },
#              {
#                  "userid":"id2",
#              },
#              {
#                  "userid":"id3",
#              }
#               ]
#     },
#    "allow_partys":{
#        "partyid": [1]
#     },
#     "allow_tags":{
#        "tagid": [1,2,3]
#     }
#    "close":0 ,
#    "redirect_domain":"www.qq.com",
#    "report_location_flag":0,
#    "isreportenter":0,
#    "home_url":"http://www.qq.com"
# }
def get_app_list():
    result = {}
    url = 'https://qyapi.weixin.qq.com/cgi-bin/agent/get?access_token=%s&agentid=%s' % \
          (get_access_token(), get_app_id())
    response = requests.get(url)
    if response.status_code == 200:
        ret = response.content
        ret = json.loads(ret)
        if ret['errmsg'] == 'ok' and ret['errcode'] == 0:
            result = ret

    return result

# data =
# {
#    "agentid": 5,
#    "report_location_flag": 0,
#    "logo_mediaid": "xxxxx",
#    "name": "NAME",
#    "description": "DESC",
#    "redirect_domain": "xxxxxx",
#    "isreportenter":0,
#    "home_url":"http://www.qq.com"
# }
def set_app_attr(data):
    flag = False
    url = 'https://qyapi.weixin.qq.com/cgi-bin/agent/set?access_token=%s' % get_access_token()
    response = requests.post(url)
    if response.status_code == 200:
        ret = response.content
        ret = json.loads(ret)
        if ret['errmsg'] == 'ok' and ret['errcode'] == 0:
            flag = True

    return flag

# result = "agentlist":
#    [
#         {
#             "agentid":1,
#             "name":"NAME",
#             "square_logo_url":"xxxxxxxx"
#         },
#         {
#             "agentid":2,
#             "name":"NAME",
#             "square_logo_url":"xxxxxxxx"
#         }
#     ]
def get_simple_app_list():
    result = []
    url = 'https://qyapi.weixin.qq.com/cgi-bin/agent/list?access_token=%s' % get_access_token()
    response = requests.get(url)
    if response.status_code == 200:
        ret = response.content
        ret = json.loads(ret)
        if ret['errmsg'] == 'ok' and ret['errcode'] == 0:
            result = ret['agentlist']

    return result

############################################################
#  Message API
############################################################
# text_data =
# {
#    "touser" : "UserID1|UserID2|UserID3",
#    "toparty" : " PartyID1|PartyID2 ",
#    "totag" : " TagID1 | TagID2 ",
#    "msgtype" : "text",
#    "agentid" : 1, # get_app_id()
#    "text" : {
#        "content" : "你的快递已到，请携带工卡前往邮件中心领取。\n
#                     出发前可查看<a href=\"http://work.weixin.qq.com\">邮件中心视频实况</a>，聪明避开排队。"
#    },
#    "safe":1
# }

# card_dta =
# {
#    "touser" : "serID1|UserID2|UserID3",
#    "toparty" : " PartyID1 | PartyID2 ",
#    "totag" : " TagID1 | TagID2 ",
#    "msgtype" : "textcard",
#    "agentid" : 1,
#    "textcard" : {
#      "title" : "领奖通知",
#      "description" : "<div class=\"gray\">2016年9月26日</div> <div class=\"normal\">恭喜你抽中iPhone 7一台，领奖码：xxxx</div><div class=\"highlight\">请于2016年10月10日前联系行政同事领取</div>",
#      "url" : "URL"
#    }
# }
def send_text_msg(user_list, content):
    text_data = {
       "touser"  : "",
       "toparty" : "",
       "totag"   : "",
       "msgtype" : "text",
       "agentid" : get_app_id(),
       "text" : {
           "content" : content
       },
       "safe":0
    }

    for user in user_list:
        text_data["touser"] += user+"|"
    text_data["touser"]=text_data["touser"][:-1]

    flag = False
    errmsg = ''
    url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s' % get_access_token()
    response = requests.post(url, data=json.dumps(text_data))
    if response.status_code == 200:
        ret = response.content
        ret = json.loads(ret)
        if ret['errmsg'] == 'ok' and ret['errcode'] == 0:
            flag = True
        else:
            errmsg = ret['errmsg']
            
    return flag, errmsg


if __name__ == '__main__':
    content = "领奖通知\n2016年9月26日\n恭喜你抽中iPhone 7一台，领奖码：xxxx\n请于2016年10月10日前联系行政同事领取"
    print send_text_msg(get_user_list(), content)

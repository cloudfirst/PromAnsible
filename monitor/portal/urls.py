from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',       views.index,  name='index'),
    url(r'^config$', views.config, name='config'),
    url(r'^config/prometheus$',      views.config_prometheus,       name='config_prometheus'),
    url(r'^config/yaml/editor/(?P<target>[-\w]+)$', views.config_edit_yaml,  name='config_edit_yaml'),
    url(r'^config/yaml/generator$',  views.config_gen_yaml, name='config_gen_yaml'),

    url(r'^config/alertman$',   views.config_alertman,   name='config_alertman'),
    url(r'^config/alertrule$',  views.config_alertrule,  name='config_alertrule'),
    url(r'^config/snmp$',        views.config_snmp,       name='config_snmp'),

    url(r'^manage$',        views.manage,       name='manage'),
    url(r'^settings$',      views.settings,     name='settings'),
    url(r'^netdevices$',    views.netdevices,   name='netdevices'),
    url(r'^servers$',       views.servers,      name='servers'),
    url(r'^alertman$',      views.alertman,     name='alertman'),
    url(r'^snmpman$',       views.snmpman,      name='snmpman'),
    url(r'^wechatman$',     views.wechatman,    name='wechatman'),
    url(r'^ansibleman',     views.ansibleman,   name='ansibleman'),
    url(r'^aiman$',         views.aiman,        name='aiman'),
    url(r'^apscheduleman$', views.apscheduleman,        name='apscheduleman$'),

    url(r'^api/1.0/wechat/edit$',       views.edit_wechat,       name='edit_wechat'),
    url(r'^api/1.0/wechat/upload$',     views.upload_wechat,     name='upload_wechat'),

    url(r'^api/1.0/alert$',             views.alertHandler,      name='alertHandler'),
    url(r'^api/1.0/alertbyansible$',    views.alertByAnsible,    name='alertByAnsible'),
    url(r'^api/1.0/alert/handler/add$', views.alertAddHandler,   name='alertAddHandler'),
    url(r'^api/1.0/alert/handler/del$', views.alertDelHandler,   name='alertDelHandler'),
    url(r'^api/1.0/admin_login$',       views.admin_login,       name='admin_login'),
    url(r'^api/1.0/gen_yaml$',          views.gen_yaml,          name='gen_yaml'),

    url(r'^api/1.0/devicetype/list/',   views.device_type_list,  name="device_type_list"),
    url(r'^api/1.0/devicetype/add$',    views.device_type_add,   name="device_type_add"),
    url(r'^api/1.0/devicetype/edit$',   views.device_type_edit,  name="device_type_edit"),
    url(r'^api/1.0/devicetype/del$',    views.device_type_del,   name="device_type_del"),

    url(r'^api/1.0/servergroup/list/',  views.server_group_list, name="server_group_list"),
    url(r'^api/1.0/servergroup/add$',   views.server_group_add,  name="server_group_add"),
    url(r'^api/1.0/servergroup/edit$',  views.server_group_edit, name="server_group_edit"),
    url(r'^api/1.0/servergroup/del$',   views.server_group_del,  name="server_group_del"),

    url(r'^api/1.0/ostype/list/',       views.os_type_list,      name="os_type_list"),
    url(r'^api/1.0/ostype/add$',        views.os_type_add,       name="os_type_add"),
    url(r'^api/1.0/ostype/edit$',       views.os_type_edit,      name="os_type_edit"),
    url(r'^api/1.0/ostype/del$',        views.os_type_del,       name="os_type_del"),

    url(r'^api/1.0/netdevice/list/',    views.net_device_list,   name="net_device_list"),
    url(r'^api/1.0/netdevice/add$',     views.net_device_add,    name="net_device_add"),
    url(r'^api/1.0/netdevice/edit$',    views.net_device_edit,   name="net_device_edit"),
    url(r'^api/1.0/netdevice/del$',     views.net_device_del,    name="net_device_del"),

    url(r'^api/1.0/servers/list/',      views.servers_list,      name="servers_list"),
    url(r'^api/1.0/servers/add$',       views.servers_add,       name="servers_add"),
    url(r'^api/1.0/servers/edit$',      views.servers_edit,      name="servers_edit"),
    url(r'^api/1.0/servers/del$',       views.servers_del,       name="servers_del"),

    url(r'^api/1.0/save/(?P<target>\w+)',   views.save_yml,       name="save_prometheus_yml"),

    url(r'^admlogin$',              views.portal_adm_login,          name='portal_adm_login'),

    url(r'^api/1.0/ansible/gen/inventory',   views.gen_inventory,       name="gen_inventory"),
    url(r'^api/1.0/ansible/set/giturl',      views.set_git_url,         name="set_git_url"),
    url(r'^api/1.0/ansible/do/gitpull',      views.do_git_pull,         name="do_git_pull"),
    url(r'^api/1.0/ansible/routine/run_once',       views.routine_run_once,         name="routine_run_once"),


    url(r'^wizard/set/devops/target/(?P<title>[-\w]+)',        views.set_devops_target,         name="set_devops_target"),
    url(r'^wizard/set/devops/schedule/(?P<title>[-\w]+)',      views.set_devops_schedule,       name="set_devops_schedule"),

    url(r'^user/edit_password/(?P<uid>\w+)$',                  views.edit_password,             name='edit_password'),
    url(r'^api/1.0/account/reset_password',                    views.account_reset_password,    name='account_reset_password'),
    url(r'^user_logout$',                                      views.user_logout,               name='user_logout'),
]
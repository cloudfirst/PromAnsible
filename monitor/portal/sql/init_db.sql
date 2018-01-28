SET NAMES utf8;

alter table portal_mn_alert2action convert to character set utf8;
alter table portal_mn_ansible_action convert to character set utf8;
alter table portal_mn_ansible_git_para convert to character set utf8;
alter table portal_mn_devicetype convert to character set utf8;
alter table portal_mn_enterprise_wechat convert to character set utf8;
alter table portal_mn_netdevices convert to character set utf8;
alter table portal_mn_ostypes convert to character set utf8;
alter table portal_mn_servergroup convert to character set utf8;
alter table portal_mn_servers convert to character set utf8;

INSERT INTO portal_mn_devicetype (`type_name` ) VALUES ("交换机" );
INSERT INTO portal_mn_devicetype (`type_name` ) VALUES ("路由器" );
INSERT INTO portal_mn_devicetype (`type_name` ) VALUES ("无线路由器");
INSERT INTO portal_mn_devicetype (`type_name` ) VALUES ("无线AP"  );

INSERT INTO portal_mn_servergroup (`group_name`, `listen_port` ) VALUES ("NODE", 9100 );
INSERT INTO portal_mn_servergroup (`group_name`, `listen_port` ) VALUES ("WIN_NODE", 9182 );

INSERT INTO portal_mn_ostypes (`ostype` ) VALUES ("WindowsXP" );
INSERT INTO portal_mn_ostypes (`ostype` ) VALUES ("Windows7" );
INSERT INTO portal_mn_ostypes (`ostype` ) VALUES ("Windows7_64" );
INSERT INTO portal_mn_ostypes (`ostype` ) VALUES ("Ubuntu_64" );
INSERT INTO portal_mn_ostypes (`ostype` ) VALUES ("Windows8" );
INSERT INTO portal_mn_ostypes (`ostype` ) VALUES ("Windows2003" );
INSERT INTO portal_mn_ostypes (`ostype` ) VALUES ("Windows2003_64" );
INSERT INTO portal_mn_ostypes (`ostype` ) VALUES ("Windows2008" );
INSERT INTO portal_mn_ostypes (`ostype` ) VALUES ("Windows2008_64" );
INSERT INTO portal_mn_ostypes (`ostype` ) VALUES ("Windows2012_64" );




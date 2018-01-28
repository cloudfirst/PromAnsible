BEGIN;
--
-- Create model mn_alert2action
--
CREATE TABLE `portal_mn_alert2action` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `alert_name` varchar(30) NOT NULL, `alert_actions` varchar(300) NOT NULL);
--
-- Create model mn_Ansible_action
--
CREATE TABLE `portal_mn_ansible_action` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `action_name` varchar(30) NOT NULL, `action_desc` varchar(300) NOT NULL);
--
-- Create model mn_Ansible_git_para
--
CREATE TABLE `portal_mn_ansible_git_para` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `git_url` varchar(300) NOT NULL, `git_pubkey` varchar(300) NOT NULL, `git_prvkey` varchar(300) NOT NULL);
--
-- Create model mn_DeviceType
--
CREATE TABLE `portal_mn_devicetype` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `type_name` varchar(30) NOT NULL);
--
-- Create model mn_Enterprise_wechat
--
CREATE TABLE `portal_mn_enterprise_wechat` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `corp_id` varchar(100) NOT NULL, `app_secret` varchar(100) NOT NULL, `app_id` integer NOT NULL, `user_ids` varchar(300) NOT NULL);
--
-- Create model mn_NetDevices
--
CREATE TABLE `portal_mn_netdevices` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `device_type` varchar(30) NOT NULL, `device_ip` varchar(30) NOT NULL, `device_mac` varchar(30) NOT NULL);
--
-- Create model mn_OSTypes
--
CREATE TABLE `portal_mn_ostypes` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `ostype` varchar(30) NOT NULL);
--
-- Create model mn_ServerGroup
--
CREATE TABLE `portal_mn_servergroup` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `group_name` varchar(30) NOT NULL);
--
-- Create model mn_Servers
--
CREATE TABLE `portal_mn_servers` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `sip` varchar(30) NOT NULL, `smac` varchar(30) NOT NULL, `sostype` varchar(30) NOT NULL, `smodel` varchar(100) NOT NULL, `sgroup1` varchar(50) NOT NULL, `sgroup2` varchar(50) NOT NULL, `sgroup3` varchar(50) NOT NULL, `sgroup4` varchar(50) NOT NULL, `sadmin` varchar(30) NOT NULL, `spasswd` varchar(30) NOT NULL);
COMMIT;

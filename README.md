# Goal and Philosophy
PromAnsible的目标是为了中小企业的IT环境提供一个全自动化的运维管理工具，涵盖从系统性能指标实时监控，异常报警，和自动化报警处理等一条龙服务。

同时，我们的开发目标也希望PromAnsible的应用门槛尽可能的低，无需专业的运维人员也能顺利安装部署和应用。因此在安装部署和应用方面，也尽量体现了自动化的思想。

更多介绍，请查阅[Wiki](https://github.com/cloudfirst/PromAnsible/wiki/1-Overview)

# Design Principle
PromAnsible能够
- 自动生成监控参数配置
- 提供预定义好的监控图表
- 提供预定义好的报警规则
- 提供基于ansible的安装部署脚本
- 提供基于ansible的，可定制的报警处理脚本sample
- 提供了基于微信的报警功能模块
- 可图形化定义报警后续处理模块

# Architecture
![](https://s5.postimg.cc/jf8g27i87/promansible-arch.png)

# Requirements
- OS: Ubuntu 16.04 Server 64bit
- Python 2.7

PromAnsible的运行依赖如下软件：
- Django 1.11.3
- MySQL 5.5
- memcache
- ZMQ
- supervisor

# Build 
请参考 [How to Build](https://github.com/cloudfirst/PromAnsible/wiki/2-How-to-Build)

# Installation
我们提供了基于ansible的安装脚本 [promansible-Install](https://github.com/cloudfirst/promansible-Install)

具体信息请参考 [README.md](https://github.com/cloudfirst/promansible-Install/blob/master/README.md)

# Usage
请参考 [How to use PromAnsible](https://github.com/cloudfirst/PromAnsible/wiki/3-How-to-use-PromAnsible-(Quick-Start))

# Reference
- 《SRE：Google运维解密》【美】Betsy Beyer（贝特西 拜尔）等
- 《Ansible自动化运维：技术与佳实践》  陈金窗 / 沈灿 


# License
Apache License 2.0
参见 [COPYING](https://github.com/cloudfirst/PromAnsible/blob/master/LICENSE) 

# Sponsor
如果觉得这个repository对你有用，欢迎打赏！(点击页面右上角的粉色sponsor按钮)

# 猜你可能感兴趣的
- 下一代VPN(http://www.oxfold.cn), 通过纯软件的方式，帮助客户在互联网上创建只对授权员工可见的，面向公司专有的虚拟办公网络。加入到这个虚拟办公网络的设备和员工，彼此之间就像真正在办公室一样的互联互通。
- 有了下一代企业级VPN，可以替换已经有的又慢有难用的传统VPN；可以轻松，免费的实现远程办公和远程技术支持，可以安全低成本的实现异地机构的互联互通。最重要的是，例如在供应链上下游企业之间，可以安全地实现各自业务系统和数据的打通. 为了更好的服务中小企业，10人一下企业团队是终身免费使用；其它规模的企业送6个月的免费使用时间。
- 传统VPN只是帮员工接入到公司内部网络，在安全性，稳定性和易用性上面，和下一代企业级VPN相差甚远。下一代企业级VPN是纯软件解决方案，不需要公网IP，不需要防火墙，天然免疫DDOS攻击，几乎不掉线，传输速度是传统VPN的10倍以上。管理维护几乎零门槛，会操作小程序创建用户账号就能做管理员。


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

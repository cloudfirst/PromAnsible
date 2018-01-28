# -*- coding: utf-8 -*-
from zmqWrapper import *
import multiprocessing, memcache
import zmq, json, os, pexpect, time
from monitorLog import *
logger = getMonitorLogger()

redirect_str = " 2>&1 | tee -a /storage/log/task.log"

class monitord_cmdConsumer():
    def __init__(self, port=MONITORD_CMD_QUEUE_PORT):
        logger.error("zmq: monitord_cmdConsumer start running")
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
        self.socket.bind("tcp://*:%s" % port)

    def cmdHandle(self, body):
        logger.error('zmq: clc get msg body = %s' % body)
        try:
            message = json.loads(body)
            if message.has_key('type') and message['type'] in  cmd_handlers and cmd_handlers[message['type']] != None:
                logger.error("zmq: monitord_cmdConsumer get cmd = %s" %  body)
                cmd_handlers[message['type']](message)
            else:
                logger.error("zmq: monitord_cmdConsumer get unknown cmd : %s", body)
        except Exception as e:
            logger.error("zmq: monitord_cmdConsumer exception = %s", str(e))

    def run(self):
        while True:
            msg = self.socket.recv()
            self.socket.send('OK')
            self.cmdHandle(msg)
#
#  ansible-playbook
#    -i ./geninventory.py
#    playbook/routine/routinehandler.yml
#    -u luhya
#    -kK
#    --extra-vars "myhost=192.168.56.103 myrole=install-node-exporter"
class routine_handle_process(multiprocessing.Process):
    def __init__(self, msg):
        multiprocessing.Process.__init__(self)
        self.msg = msg

    def run_once_by_pexpect(self, cmd, password):
        os.system("echo '" + self.msg["before_prompt"].encode("UTF-8") + "' >> /storage/log/task.log")
        child = pexpect.spawn('/bin/bash', ['-c', cmd])
        child.expect('SSH password:')
        child.sendline(password)
        child.expect("SUDO password")
        child.sendline(password)

        while 1:
            time.sleep(3)
            if child.isalive():
                continue
            else:
                os.system("echo '" + self.msg["after_prompt"].encode("UTF-8") + "' >> /storage/log/task.log")
                break

    def run_once(self, cmd):
        os.system(cmd)

    def run(self):
        if self.msg['group'].lower().find("win") == 0:
            # this is a windows target
            self.fwin = True
            cmd = 'ansible-playbook -c winrm -i %s %s -u %s -kK -e \'{"myhost": %s, "myrole": %s, "ansible_port": 5986, "ansible_winrm_transport": "plaintext", "ansible_winrm_server_cert_validation": "ignore"}\''
            yml = self.msg['src_path'] + "/playbook/routine/routinehandler-win.yml"
        else:
            # this is a linux target
            cmd = 'ansible-playbook -i %s %s -u %s -kK --extra-vars "myhost=%s myrole=%s"'
            yml = self.msg['src_path'] + "/playbook/routine/routinehandler.yml"

        if self.msg["host"] == "all":
            real_host = self.msg["group"]
        else:
            real_host = self.msg["host"]

        cmd = cmd % (self.msg["src_path"] + "/geninventory.py",
                     yml,
                     self.msg['username'],
                     real_host,
                     self.msg["role"]) + redirect_str
        logger.error("routine_handle_process: cmd = %s" % cmd)
        self.run_once_by_pexpect(cmd, self.msg['password'])

class alert_handle_process(multiprocessing.Process):
    def __init__(self, msg):
        multiprocessing.Process.__init__(self)
        self.msg = msg

    def run_once_by_pexpect(self, cmd, password):
        os.system("echo '" + self.msg["before_prompt"].encode("UTF-8") + "' >> /storage/log/task.log")
        child = pexpect.spawn('/bin/bash', ['-c', cmd])
        child.expect('SSH password:')
        child.sendline(password)
        child.expect("SUDO password")
        child.sendline(password)
        while 1:
            time.sleep(3)
            if child.isalive():
                continue
            else:
                os.system("echo '" + self.msg["after_prompt"].encode("UTF-8") + "' >> /storage/log/task.log")
                break

    def run(self):
        if self.msg['group'].lower().find("win") == 0:
            # this is a windows target
            cmd = 'ansible-playbook -c winrm -i %s %s -u %s -kK -e \'{"myhost": %s, "myrole": %s, "ansible_port": 5986, "ansible_winrm_transport": "plaintext", "ansible_winrm_server_cert_validation": "ignore"}\''
            yml = self.msg['src_path'] + "/playbook/alert/alerthandler-win.yml",
        else:
            # this is a linux target
            cmd = 'ansible-playbook -i %s %s -u %s -kK --extra-vars "myhost=%s myrole=%s"'
            yml = self.msg['src_path'] + "/playbook/alert/alerthandler.yml",

        if self.msg["host"] == "all":
            real_host = self.msg["group"]
        else:
            real_host = self.msg["host"]

        roles = self.msg['roles']
        for r in roles:
            cmd = cmd % (self.msg["src_path"] + "/geninventory.py",
                         yml,
                         self.msg['username'],
                         real_host,
                         r) + redirect_str
            logger.error("alert_handle_process: cmd = %s" % cmd)
            self.run_once_by_pexpect(cmd, self.msg['password'])

class command_handle_process(multiprocessing.Process):
    def __init__(self, msg):
        multiprocessing.Process.__init__(self)
        self.msg = msg

    def run(self):
        os.system("echo '" + self.msg["before_prompt"].encode("UTF-8") + "' >> /storage/log/task.log")
        os.system(self.msg['cmd'] + redirect_str)
        os.system("echo '" + self.msg["after_prompt"].encode("UTF-8")  + "' >> /storage/log/task.log")

def command_handle(msg):
    worker = command_handle_process(msg)
    worker.start()

def routine_handle(msg):
    worker = routine_handle_process(msg)
    worker.start()

def alert_handle(msg):
    worker = alert_handle_process(msg)
    worker.start()

cmd_handlers = {
    'routine'         : routine_handle,
    'alert'           : alert_handle,
    'command'         : command_handle,
}

def main():
    consumer = monitord_cmdConsumer()
    consumer.run()

if __name__ == '__main__':
    main()
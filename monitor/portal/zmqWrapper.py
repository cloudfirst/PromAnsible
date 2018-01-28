import zmq

from monitorLog import *

logger = getMonitorLogger()

MONITORD_CMD_QUEUE_PORT = 9997

def zmq_send(ip, msg, port):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://%s:%s" % (ip,port))

    socket.send(msg)
    message = socket.recv()
    logger.error("zmq_send result = %s" % message)

def zmq_recv():
    pass
import zmq
import random
import sys
import time
import numpy as np

port = "5555"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.PUB)
# socket.bind("tcp://*:%s" % port)
socket.bind("tcp://*:5555")
while True:
    n = random.uniform(-3.14,3.14)
    qpos = n*np.ones(13)
    topic = "qpos_array"
    qpos_str = np.array2string(qpos, precision=2, separator=',',suppress_small=True)
    string = topic+" "+qpos_str
    print (string)
    # socket.send(string.encode('ascii'))
    socket.send(qpos)
    time.sleep(1)


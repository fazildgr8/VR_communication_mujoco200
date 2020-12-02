import zmq
import numpy as np
from time import sleep
import random
context = zmq.Context()

# Socket to talk to server
print("Connecting to hello world server...")
socket = context.socket(zmq.REP)
socket.connect("tcp://localhost:5555")

def arr_fromat(arr):
    string = str(arr[0]);
    arr2 = arr[1:]
    for e in arr2:
        string = string+' '+str(e)
    return string
def send_qpos(qpos):
    request = socket.recv()
    print("Received request [", request, "]")
    print("Sending reply to request", request, '== ',arr_fromat(qpos))
    socket.send_string(arr_fromat(qpos))

# # Tester
while(True):
    # Get the request.
    n = random.uniform(-3.14,3.14)
    qpos = n*np.ones(13)
    send_qpos(qpos)



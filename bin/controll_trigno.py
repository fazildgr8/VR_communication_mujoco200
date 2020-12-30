import zmq
import numpy as np
from time import sleep
import pytrigno
import random
context = zmq.Context()

# Socket to talk to server
print("Connecting to hello world server...")
socket = context.socket(zmq.REP)
socket.connect("tcp://localhost:5555")

def arr_fromat(arr):
    string = str(arr[0])
    arr2 = arr[1:]
    for e in arr2:
        string = string+' '+str(e)
    return string
def send_qpos(qpos):
    request = socket.recv()
    print("Received request [", request, "]")
    print("Sending reply to request", request, '== ',arr_fromat(qpos))
    socket.send_string(arr_fromat(qpos))

def send_qpos_emg(qpos):
    request = socket.recv()
    print("Received request [", request, "]")
    print("Sending reply to request", request, '== ',arr_fromat(qpos))
    socket.send_string(arr_fromat(qpos))

def normalize(x,upper,lower):
    num = x - lower
    den = upper-lower
    return num/den

class emg_qpos:
    def __init__(self,channels_range,sample=150):
        self.sample = sample
        self.channel = channels_range-1
        self.host = 'localhost'
        self.dev = pytrigno.TrignoEMG(channel_range=(0, self.channel), samples_per_read=self.sample,host=self.host)
    def stream_emg(self,callback,n_qpos):
        self.dev.start()
        while(True):
            self.data = self.dev.read()
            self.sensor_val = self.data
            if(self.sample>1):
                self.sensor_val = list()
                for val in self.data:
                    self.sensor_val.append(np.mean(val))
            print(self.sensor_val)
            qpos = np.zeros(n_qpos)
            qpos[1] = abs(self.sensor_val[0])*25000
            qpos[2] = abs(self.sensor_val[1])*25000
            qpos[7] = abs(self.sensor_val[2])*25000

            callback(qpos)
        self.dev.stop()      



# # Tester
while(True):
    emg = emg_qpos(3,150)
    emg.stream_emg(send_qpos_emg,13)





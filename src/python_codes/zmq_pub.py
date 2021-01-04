import zmq
import datetime

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:5555")
# socket.bind("tcp://localhost:5555")

while True:
    now = datetime.datetime.now()
    nowInMicroseconds = str(now.microsecond)
    socket.send_string(nowInMicroseconds)
    print(nowInMicroseconds)
import zmq
from time import sleep
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

while True:
    msg = "hello"
    socket.send_string(msg)
    print("sent "+ msg)
    sleep(0.5)
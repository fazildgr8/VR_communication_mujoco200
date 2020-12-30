import socket
import numpy as np
import random
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 27015))
s.listen(5)
clientsocket, address = s.accept()
while True:
    # now our endpoint knows about the OTHER endpoint.
    n = random.uniform(-3.14,3.14)
    qpos = n*np.ones(13)
    print(f"Connection from {address} has been established.")
    clientsocket.send(bytes(str(qpos),"utf-8"))
    time.sleep(1)
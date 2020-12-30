import sys
import zmq

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)
    
if len(sys.argv) > 2:
    port1 =  sys.argv[2]
    int(port1)

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

print ("Collecting updates from weather server...")
socket.connect ("tcp://localhost:%s" % port)

if len(sys.argv) > 2:
    socket.connect ("tcp://localhost:%s" % port1)
# Subscribe to zipcode, default is NYC, 10001
topicfilter = "qpos_array"
socket.setsockopt(zmq.SUBSCRIBE, topicfilter.encode('ascii'))



for update_nbr in range (10):
    string = socket.recv()
    print(string)
    topic, messagedata = string.split()
    print (topic, messagedata)

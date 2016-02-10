import zmq
import random
import sys
import time

#we want to connect to same port as forwarder frontend SUB socket
port = "5559"
context = zmq.Context()
#Server is publisher of info
socket = context.socket(zmq.PUB)
socket.connect("tcp://localhost:%s" % port)
publisher_id = random.randrange(0,9999)

while True:
	topic = random.randrange(1,10)
	messagedata = "server#%s" % publisher_id
	print "%s %s" % (topic, messagedata)
	socket.send("%d %s" % (topic, messagedata))
	time.sleep(1)
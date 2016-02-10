import sys
import zmq

#we want to connect the subscriber to the forwarder's backend PUB socket
port = "5560"
context = zmq.Context()
socket = context.socket(zmq.SUB)
print "Attempting to get updates from publisher server"
socket.connect("tcp://localhost:%s" % port)

topicfilter = "3"

socket.setsockopt(zmq.SUBSCRIBE, topicfilter)

for update_num in range(50)
	string = socket.recv()
	topic, messagedata = string.split()
	print topic, messagedata

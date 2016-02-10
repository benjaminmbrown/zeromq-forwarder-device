import zmq

#PUBLISHERS -> fe SUB socket - FORWARDER - be PUB socket <-- SUBSCRIBERS
def main():
	context= zmq.Context()


 	try:
 		#create front end SUB socket for the forwarder coming from PUBLISHER
		fe = context.socket(zmq.SUB)
		fe.bind("tcp://*:5559")
		fe.setsockopt(zmq.SUBSCRIBE, "")

		#create backend PUB socket for the forwarder coming from SUBSCRIBER
		be = context.socket(zmq.PUB)
		backend.bind("tcp://*:5560")

		zmq.device(zmq.FORWARDER, frontend, backend)
		
	except Exception, e:
		print e
		print "Destroying ZMQ forwarder forwarder device."
	finally:
		pass
		fe.close()
		be.close()
		context.term()

if __name__ == "__main__"
	main()


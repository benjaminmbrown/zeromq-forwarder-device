# zeromq-forwarder-device
Forwarder device for use with Pub/Sub patterns in zeroMQ
<br/>

Forwarder acts as a proxy server for pub/sub pattern. Pubs/Subs can change independently and forwarder becomes stable point.

<br>
To run, start the forwarder device, then the publishers, then the servers. Use multiple servers to see how a subscriber can get an update from any publisher that publishes a matching topic:<br/>

python zmq-forwarder-device.py<br/>
python zmq-forwarder-subscriber.py<br/>
python zmq-forwarder-publisher.py<br/>
python zmq-forwarder-publisher.py<br/>
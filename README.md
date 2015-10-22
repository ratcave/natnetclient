# natnetclient
Python NatNet Client for retrieving NaturalPoint's Optitrack data from their Motive software using depacketization.

##Installation
To install, simply download the repository, navigate to its directory, and use the 'python setup.py install' command.  
For example:

```
cd Downloads/natnetclient
python setup.py install
```

## Quick Guide

While I plan to add some documentation in the future, it might be a while,
(please message me if you'd like it, and I'll get right on it!), so here is a quick summary of how to get started:

### Connecting to Motive

Before connecting, make sure that your Motive software is actually streaming NatNet data.  Also, note the IP address and data and command
socket port numbers.  If they don't match, there won't be a connection.  Then, simply use the *NatClient* class to connect:

```python
import natnetclient as natnet
client = natnet.NatClient(client_ip='127.0.0.1', data_port=1511, comm_port=1510)
```

The NatClient contains a NatCommSocket and a NatDataSocket, and when connected, automatically starts a Threading thread that continually
retrieves data.  In addition, it performs depacketization and stores the data.

### Miscellaneous Commands

Try the following to get started.  You'll find a lot of useful functions and properties in the NatClient, RigidBody, and Marker classes.

```python
rigid_body_dict = client.rigid_bodies
body = rigid_body_dict['NameOfBody']
xyz = body.position
xyz_rot = body.rotation
body_markers = body.markers
body_marker_position = body_markers[0].position
```

## Retriving 




[![Build Status](https://travis-ci.org/neuroneuro15/natnetclient.svg?branch=master)](https://travis-ci.org/neuroneuro15/natnetclient)

![Window Build Status](https://ci.appveyor.com/api/projects/status/github/neuroneuro15/natnetclient?svg=True)

[![Coverage Status](https://coveralls.io/repos/github/neuroneuro15/natnetclient/badge.svg?branch=master)](https://coveralls.io/github/neuroneuro15/natnetclient?branch=master)

# natnetclient
Python NatNet Client for retrieving NaturalPoint's Optitrack data from their Motive software using socket depacketization. This project cross-platform and compatible with both Python 2 and Python 3.


##Installation

```
pip install natnetclient
```

## Quick Guide

### Connecting to Motive

Before connecting, make sure that your Motive software is actually streaming NatNet data.  Also, note the IP address and data and command
socket port numbers.  If they don't match, there won't be a connection.  Then, simply use the *NatClient* class to connect:

```python
import natnetclient as natnet
client = natnet.NatClient(client_ip='127.0.0.1', data_port=1511, comm_port=1510)
```

### Get Rigid Bodies

Once the NatClient is connected, it will automatically and continuously get the latest information on its own thread.

Rigid bodies are stored in a dictionary, and classes exist for Rigid Bodies and Markers, each with their own properties, supplied by Motive:

```python
hand = client.rigid_bodies['Hand'] # Assuming a Motive Rigid Body is available that you named "Hand"
print(hand.position)
print(hand.rotation)

hand_markers = hand.markers  # returns a list of markers, each with their own properties
print(hand_markers[0].position)
```

## Troubleshooting

### NatClient is timing out and not connecting.

  - Make sure that Motive is streaming--for some reason, recent versions of Motive have this off by default.
  - Make sure the IP and ports in NatClient match Motive's settings, so they can talk to each other.

### NatClient's Rigidbody dictionary is Empty

  - Make sure Motive's "Stream Rigid Bodies" option is turned on.  Recently, Motive's default is to not stream that info.


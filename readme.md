# URMQTT

``urmqtt`` is an open source fork of ``amqtt`` which `MQTT`_ client and broker implementation.

Built on top of `asyncio`_, Python's standard asynchronous I/O framework, urmqtt provides a straightforward API
based on coroutines, making it easy to write highly concurrent applications.

``amqtt`` was forked from `HBMQTT`_ after it was deprecated by the original author.


.. _asyncio: https://docs.python.org/3/library/asyncio.html
.. _HBMQTT: https://github.com/beerfactory/hbmqtt

Features
--------

urmqtt implements the full set of `MQTT 3.1.1`_ protocol specifications and provides the following features:

- Support QoS 0, QoS 1 and QoS 2 messages flow
- Client auto-reconnection on network lost
- Authentication through password file (more methods can be added through a plugin system)
- Basic ``$SYS`` topics
- TCP and websocket support
- SSL support over TCP and websocket
- Plugin system
- ACL
- lua based filter map system

.. _MQTT: http://www.mqtt.org
.. _MQTT 3.1.1: http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/os/mqtt-v3.1.1-os.html


## To use
Edit `config.json`,`acl.json`,`filter-map.json` to your flavor.  
Run 
```bash
python newserver.py
```
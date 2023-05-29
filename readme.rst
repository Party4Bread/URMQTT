|license| |ci| |coverage| |rtfm| |gitter| |python_versions| |python_wheel| |PyPI|

.. |license| image:: https://img.shields.io/github/license/Yakifo/urmqtt?style=flat-square
    :target: https://urmqtt.readthedocs.io/en/latest/
    :alt: MIT licensed

.. |ci| image:: https://img.shields.io/github/workflow/status/Yakifo/urmqtt/Python%20package?style=flat-square
    :target: https://github.com/Yakifo/urmqtt/actions/workflows/python-package.yml

.. |coverage| image:: https://img.shields.io/coveralls/github/Yakifo/urmqtt?style=flat-square
    :target: https://coveralls.io/github/Yakifo/urmqtt?branch=master

.. |rtfm| image:: https://img.shields.io/readthedocs/urmqtt?style=flat-square
    :target: https://urmqtt.readthedocs.io/en/latest/
    :alt: Documentation Status

.. |gitter| image:: https://img.shields.io/gitter/room/Yakifo/urmqtt?style=flat-square
    :target: https://gitter.im/urmqtt/community
    :alt: 'Join the chat at https://gitter.im/urmqtt/community'

.. |python_versions| image:: https://img.shields.io/pypi/pyversions/urmqtt?style=flat-square
    :alt: Python Version

.. |python_wheel| image:: https://img.shields.io/pypi/wheel/urmqtt?style=flat-square 
    :alt: supports python wheel

.. |PyPI| image:: https://img.shields.io/pypi/v/urmqtt?style=flat-square
    :target: https://pypi.org/project/urmqtt/
    :alt: PyPI


urmqtt
======

``urmqtt`` is an open source fork of ``amqtt`` which `MQTT`_ client and broker implementation.

Built on top of `asyncio`_, Python's standard asynchronous I/O framework, urmqtt provides a straightforward API
based on coroutines, making it easy to write highly concurrent applications.

It was forked from `HBMQTT`_ after it was deprecated by the original author.


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


Project Status and Roadmap
---------------------------

The current focus is to build setup the project infrastructure for the new fork.
From there the goal is to fix outstanding known issues and clean up the code.

+----------+---------------------------+----------------------------+--------------+
| Version  | hbmqtt compatibility      | Supported Python Versions  | PyPi Release |
+----------+---------------------------+----------------------------+--------------+
| 0.10.x   | YES - Drop-in Replacement | 3.7*                       | 0.10.1       |
+----------+---------------------------+----------------------------+--------------+
| 0.11.x   | NO - Module renamed       | 3.7 - 3.10                 | No release   |
|          | and small API differences |                            | yet          |
+----------+---------------------------+----------------------------+--------------+


* Due to a change in Python 3.8 where the semantics of asyncio.CancelledError was changed
    to be a subclass of BaseException instead of Exception, old versions of hbmqtt and urmqtt
    will break, see https://github.com/Yakifo/urmqtt/issues/133.
    Therefore only 3.7 is mentioned as supported version for 0.10.x.


Getting started
---------------

`urmqtt` is available on `Pypi <https://pypi.python.org/pypi/urmqtt>`_ and can installed simply using ``pip`` :
::

    $ pip install urmqtt

Documentation is available on `Read the Docs`_.

Bug reports, patches and suggestions welcome! Just `open an issue`_ or join the `gitter channel`_.



.. _MQTT: http://www.mqtt.org
.. _MQTT 3.1.1: http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/os/mqtt-v3.1.1-os.html
.. _Read the Docs: http://urmqtt.readthedocs.org/
.. _open an issue: https://github.com/Yakifo/urmqtt/issues/new
.. _gitter channel: https://gitter.im/urmqtt/community

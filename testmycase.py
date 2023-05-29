import logging
import asyncio
import os
from urmqtt.broker import Broker

logger = logging.getLogger(__name__)

config = {
    "listeners": {
        "default": {
            "type": "tcp",
            "bind": "0.0.0.0:1884",
        },
        "ws-mqtt": {
            "bind": "127.0.0.1:8080",
            "type": "ws",
            "max_connections": 10,
        },
    },
    "sys_interval": 10,
    "auth": {
        "allow-anonymous": True,
        "password-file": os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "passwd"
        ),
        "plugins": ["auth_file", "auth_anonymous"],
    },
    "topic-check": {
        "enabled": True,
        "plugins": ["topic_acl"],
        "publish-acl": {
            # username: [list of allowed topics]
            "admin": ["temperature/get","door/unlock"],
            "temperature": ["temperature/get"],
            "door": ["door/unlock"],
            "eve": [],
            "anonymous": [],
        },
        "acl": {
            # username: [list of allowed topics]
            "admin": ["temperature/get","door/unlock"],
            "temperature": ["temperature/get"],
            "door": ["door/unlock"],
            "eve": [],
            "anonymous": [],
        },
    },
}

broker = Broker(config)

from urmqtt.client import MQTTClient, ClientException
from urmqtt.mqtt.constants import QOS_1

async def test_coro():
    await broker.start()

async def test_sub():
    C = MQTTClient()
    await C.connect("mqtt://test:test@127.0.0.1:1883")
    await C.subscribe(
        [
            ("data/memes", QOS_1),  # Topic allowed
            ("data/classified", QOS_1),  # Topic forbidden
            ("repositories/urmqtt/master", QOS_1),  # Topic allowed
            ("repositories/urmqtt/devel", QOS_1),  # Topic forbidden
            ("calendar/urmqtt/releases", QOS_1),  # Topic allowed
        ]
    )
    logger.info("Subscribed")
    try:
        for i in range(2):
            message = await C.deliver_message()
            packet = message.publish_packet
            print(
                "%d: %s => %s"
                % (i, packet.variable_header.topic_name, str(packet.payload.data))
            )
        await C.unsubscribe(["$SYS/broker/uptime", "$SYS/broker/load/#"])
        logger.info("UnSubscribed")
        await C.disconnect()
    except ClientException as ce:
        logger.error("Client exception: %s" % ce)

async def test_pub():
    await asyncio.sleep(1)
    C = MQTTClient()
    await C.connect("mqtt://test:test@127.0.0.1:1883")
    tasks = [
        asyncio.ensure_future(C.publish("data/memes", b"TEST MESSAGE WITH QOS_0")),
        asyncio.ensure_future(C.publish("data/memes", b"TEST MESSAGE WITH QOS_1", qos=QOS_1)),
    ]
    await asyncio.wait(tasks)
    logger.info("messages published")
    await C.disconnect()

if __name__ == "__main__":
    formatter = "[%(asctime)s] :: %(levelname)s :: %(name)s :: %(message)s"
    logging.basicConfig(level=logging.WARN, format=formatter)
    asyncio.get_event_loop().run_until_complete(test_coro())
    # asyncio.get_event_loop().run_until_complete(asyncio.wait(
    #     [test_sub(),test_pub()]
    #     ))
    asyncio.get_event_loop().run_forever()

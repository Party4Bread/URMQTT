from collections import defaultdict
import logging
import asyncio
import os
import json
from urmqtt.broker import Broker

logger = logging.getLogger(__name__)

config = {
    "topic-check": {
        "enabled": True,
        "plugins": ["topic_acl"],
        "publish-acl": defaultdict(list),
        "acl": {
        },
    },
}

def parse_config():
    with open("config.json",encoding='u8') as f:
        cfg=json.load(f)
    for i in cfg:
        config[i]=cfg[i]

def parse_acl():
    with open("acl.json",encoding='u8') as f:
        cfg=json.load(f)
    groups=cfg["group"]
    for ac in cfg["acls"]:
        if ac["action"]=="allow":
            ty=ac["type"].split("/")
            if "pub" in ty:
                users=[]
                for src in ac["src"]:
                    t,n = src.split(":")
                    if t=="user":users.append(src)
                    elif t=="group":users.extend(groups[n])
                for user in users:
                    config["topic-check"]["publish-acl"]\
                        [user.split(":")[1]].extend(ac["dst"])
        else:
            raise NotImplemented

def parse_filtermap():
    with open("config.json",encoding='u8') as f:
        cfg=json.load(f)
    for i in cfg:
        config[i]=cfg[i]

parse_config()
parse_acl()
parse_filtermap()
print(config)
exit()
broker = Broker(config)



async def test_coro():
    await broker.start()

if __name__ == "__main__":
    formatter = "[%(asctime)s] :: %(levelname)s :: %(name)s :: %(message)s"
    logging.basicConfig(level=logging.WARN, format=formatter)
    asyncio.get_event_loop().run_until_complete(test_coro())
    asyncio.get_event_loop().run_forever()

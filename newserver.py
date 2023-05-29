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

# config 적재
def parse_config():
    with open("config.json",encoding='u8') as f:
        cfg=json.load(f)
    for i in cfg:
        config[i]=cfg[i]

# 기존 ACL과 호환되는 포맷으로 acl.json 포팅
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
                    broker.config["topic-check"]["publish-acl"]\
                        [user.split(":")[1]].extend(ac["dst"])
        else:
            raise NotImplemented

# 필터맷 로드
def parse_filtermap():
    with open("filter-map.json",encoding='u8') as f:
        cfg=json.load(f)
    # config 갱신후 script rebuild
    for i in cfg:
        broker.config[i]=cfg[i]
        broker.rebuild_script()

#config 선적재
parse_config()
broker = Broker(config)

#broker에 직접 acl세팅
parse_acl()
parse_filtermap()
broker.rebuild_script()

async def server_start():
    await broker.start()
    print("SERVER UP")

from watchfiles import awatch
# acl.json 및 filter-map.json 감시
async def watch_update():
    async for changes in awatch('acl.json','filter-map.json'):
        parse_acl()
        parse_filtermap()
        broker.rebuild_script()
        print("ACL, SCRIPT RELOADED")

if __name__ == "__main__":
    formatter = "[%(asctime)s] :: %(levelname)s :: %(name)s :: %(message)s"
    logging.basicConfig(level=logging.WARN, format=formatter)
    asyncio.get_event_loop().run_until_complete(server_start())
    asyncio.get_event_loop().run_until_complete(watch_update())
    asyncio.get_event_loop().run_forever()

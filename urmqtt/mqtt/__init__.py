# Copyright (c) 2015 Nicolas JOUANIN
#
# See the file license.txt for copying permission.
from urmqtt.errors import urmqttException
from urmqtt.mqtt.packet import (
    CONNECT,
    CONNACK,
    PUBLISH,
    PUBACK,
    PUBREC,
    PUBREL,
    PUBCOMP,
    SUBSCRIBE,
    SUBACK,
    UNSUBSCRIBE,
    UNSUBACK,
    PINGREQ,
    PINGRESP,
    DISCONNECT,
    MQTTFixedHeader,
)
from urmqtt.mqtt.connect import ConnectPacket
from urmqtt.mqtt.connack import ConnackPacket
from urmqtt.mqtt.disconnect import DisconnectPacket
from urmqtt.mqtt.pingreq import PingReqPacket
from urmqtt.mqtt.pingresp import PingRespPacket
from urmqtt.mqtt.publish import PublishPacket
from urmqtt.mqtt.puback import PubackPacket
from urmqtt.mqtt.pubrec import PubrecPacket
from urmqtt.mqtt.pubrel import PubrelPacket
from urmqtt.mqtt.pubcomp import PubcompPacket
from urmqtt.mqtt.subscribe import SubscribePacket
from urmqtt.mqtt.suback import SubackPacket
from urmqtt.mqtt.unsubscribe import UnsubscribePacket
from urmqtt.mqtt.unsuback import UnsubackPacket

packet_dict = {
    CONNECT: ConnectPacket,
    CONNACK: ConnackPacket,
    PUBLISH: PublishPacket,
    PUBACK: PubackPacket,
    PUBREC: PubrecPacket,
    PUBREL: PubrelPacket,
    PUBCOMP: PubcompPacket,
    SUBSCRIBE: SubscribePacket,
    SUBACK: SubackPacket,
    UNSUBSCRIBE: UnsubscribePacket,
    UNSUBACK: UnsubackPacket,
    PINGREQ: PingReqPacket,
    PINGRESP: PingRespPacket,
    DISCONNECT: DisconnectPacket,
}


def packet_class(fixed_header: MQTTFixedHeader):
    try:
        cls = packet_dict[fixed_header.packet_type]
        return cls
    except KeyError:
        raise urmqttException("Unexpected packet Type '%s'" % fixed_header.packet_type)

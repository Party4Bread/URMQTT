# Copyright (c) 2015 Nicolas JOUANIN
#
# See the file license.txt for copying permission.
from urmqtt.mqtt.packet import MQTTPacket, MQTTFixedHeader, PINGRESP
from urmqtt.errors import urmqttException


class PingRespPacket(MQTTPacket):
    VARIABLE_HEADER = None
    PAYLOAD = None

    def __init__(self, fixed: MQTTFixedHeader = None):
        if fixed is None:
            header = MQTTFixedHeader(PINGRESP, 0x00)
        else:
            if fixed.packet_type is not PINGRESP:
                raise urmqttException(
                    "Invalid fixed packet type %s for PingRespPacket init"
                    % fixed.packet_type
                )
            header = fixed
        super().__init__(header)
        self.variable_header = None
        self.payload = None

    @classmethod
    def build(cls):
        return cls()

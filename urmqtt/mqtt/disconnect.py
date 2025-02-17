# Copyright (c) 2015 Nicolas JOUANIN
#
# See the file license.txt for copying permission.
from urmqtt.mqtt.packet import MQTTPacket, MQTTFixedHeader, DISCONNECT
from urmqtt.errors import urmqttException


class DisconnectPacket(MQTTPacket):
    VARIABLE_HEADER = None
    PAYLOAD = None

    def __init__(self, fixed: MQTTFixedHeader = None):
        if fixed is None:
            header = MQTTFixedHeader(DISCONNECT, 0x00)
        else:
            if fixed.packet_type is not DISCONNECT:
                raise urmqttException(
                    "Invalid fixed packet type %s for DisconnectPacket init"
                    % fixed.packet_type
                )
            header = fixed
        super().__init__(header)
        self.variable_header = None
        self.payload = None

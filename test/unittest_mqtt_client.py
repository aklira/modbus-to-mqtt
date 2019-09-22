#!/usr/bin/env python
# coding: utf-8
# info
__version__ = "0.1"
__author__  = "Akli R"
__date__    = "04/10/18"

import modbustomqtt.mqtt_client as mqtt

conf_mqtt = '/appli/conf/config_mqtt.yml'

def main():
    payload = 'Hello message from NPE X500'
    topic = 'modbus/data'
    mqtt.send_to_mqtt_broker(conf_mqtt, str(payload))

if __name__ == '__main__':
    main()




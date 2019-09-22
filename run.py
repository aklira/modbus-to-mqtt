#!/usr/bin/env python
# coding: utf-8
# info
__version__ = "0.1"
__author__  = "Akli R"
__date__    = "04/10/18"

import modbustomqtt.modbus_master as mm
import modbustomqtt.mqtt_client as mqtt
import modbustomqtt.mqtts_client as mqtts

import time
import sys

import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

import traceback

modbus_registers = '/appli/conf/modbus_registers.yml'
conf_modbus = '/appli/conf/config_modbus.yml'
conf_mqtt = '/appli/conf/config_mqtt.yml'

def main():
    log.info('waiting 60s for gprs connection to be available')
    time.sleep(60)

    errCnt = 0

    tls = str(sys.argv[1])

    if (tls == '--tls'):
        mqttc = mqtts
        log.info('using mqtt over tls')
    else:
        # tls == '--notls'
        mqttc = mqtt
        log.info('using mqtt without tls')

    while 1:
        try:
            log.info('reading modbus registers values')
            payload = mm.read_modbus_from_tcp_port(conf_modbus, modbus_registers)  

            log.info('sending payload to remote mqtt broker')
            mqttc.send_to_mqtt_broker(conf_mqtt, str(payload))
            log.info('sleeping for 30 min')
            
        except:
            errCnt += 1
            tb = traceback.format_exc()
            log.debug("!mqtt_client:\terrCnt: %s; last tb: %s" % (errCnt, tb))
        finally:
            time.sleep(1800)

# script entry point
if __name__ == '__main__':
    main()
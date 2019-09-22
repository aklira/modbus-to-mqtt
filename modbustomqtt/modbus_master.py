#!/usr/bin/env python
# coding: utf-8
# info
__version__ = "0.1"
__author__  = "Akli R"
__date__    = "04/10/18"

'''
-----------------------------------------------------------------------------
Pymodbus Synchronous Client
-----------------------------------------------------------------------------
'''
#---------------------------------------------------------------------------#
# import the various server implementations
#---------------------------------------------------------------------------#
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
#from pymodbus.client.sync import ModbusUdpClient as ModbusClient
#from pymodbus.client.sync import ModbusSerialClient as ModbusClient

#---------------------------------------------------------------------------#
# configure the client logging
#---------------------------------------------------------------------------#
import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

import traceback
import time
import yaml
import json

#---------------------------------------------------------------------------#
# reading modbus conf from yaml file
#---------------------------------------------------------------------------#

def read_modbus_conf(conf_file):
    with open(conf_file, 'r') as config:
        out = yaml.load(config)
    return out

def read_modbus_registers(modbus_registers):
    with open(modbus_registers, 'r') as config:
        out = yaml.load(config)
    return out

def build_registers_list(input_dict):
    out = []
    for key, value in input_dict.iteritems():
        out.append(int(value['address']))
    out.sort()
    return out

def read_modbus_from_tcp_port(conf_file, modbus_registers):

    log.info("Read modbus config from yaml file")
    modbus_conf = read_modbus_conf(conf_file)
    slaveAddr = modbus_conf['slaveaddr'] # ip du slave Modbus
    tcpport = modbus_conf['tcpport'] # port std modbus TCP
    
    log.info("Read modbus registers list from yaml file")
    input_regs = read_modbus_registers(modbus_registers)

    log.info("Build registers list")
    regs_list = build_registers_list(input_regs)

    payload = {}

    #---------------------------------------------------------------------------#
    # instanciating the approriate modbus client
    #---------------------------------------------------------------------------#
    client = ModbusClient(slaveAddr, port=tcpport)
    #client = ModbusClient(method='ascii', port=port, timeout=1)
    #client = ModbusClient(method='rtu', port='/dev/ttyp0', timeout=1)

    log.info("Connecting to Modbus slave")
    connect_ok = client.connect()

    if connect_ok:
        #---------------------------------------------------------------------------#
        # reading all registers and building payload
        #---------------------------------------------------------------------------#
        log.info("Read all input registers in sequence")

        errCnt = 0
        regCnt = 0

        timestamp = str(time.time())

        for reg in regs_list:
            try:    
                rr = client.read_input_registers(reg, 1, unit=1)

                message = {
                    'register_name': input_regs[regCnt]['name'],
                    'register_alias': input_regs[regCnt]['alias'],
                    'register_address': input_regs[regCnt]['address'],
                    'register_value': rr.registers,
                    'timestamp': timestamp
                }

                payload.update({str(regCnt):message})

                regCnt += 1

            except:
                errCnt += 1
                tb = traceback.format_exc()
                log.debug("!pymodbus:\terrCnt: %s; last tb: %s" % (errCnt, tb))
                
            finally:
                # close the client
                client.close()
    else:
        payload = 'Failed to connect to Modbus slave over TCP'
        log.error(payload)

    return payload

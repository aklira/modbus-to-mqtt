#!/usr/bin/env python
# coding: utf-8
# info
__version__ = "0.1"
__author__  = "Akli R"
__date__    = "04/10/18"

import modbustomqtt.modbus_master as mm

modbus_registers = '/appli/conf/modbus_registers.yml'
conf_modbus = '/appli/conf/config_modbus.yml'

def main():
    payload = mm.read_modbus_from_tcp_port(conf_modbus, modbus_registers)
    print payload

if __name__ == '__main__':
    main()

# coding: utf-8
# info
__version__ = "0.1"
__author__  = "Akli R"
__date__    = "04/10/18"

import minimalmodbus

def main():
    instrument = minimalmodbus.Instrument('/dev/ttySC0', 1) # port name RS485, slave address (in decimal)

    ## Read input registers
    serial_number = instrument.read_register(0, 1, minimalmodbus.MODE_ASCII) # Register number, number of decimals
    print('serial_number = %s' % serial_number)

if __name__ == '__main__':
    main()

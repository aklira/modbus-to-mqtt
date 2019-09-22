#!/usr/bin/env python
# coding: utf-8
# info
__version__ = "0.1"
__author__  = "Akli R"
__date__    = "04/10/18"

import modbustomqtt.gprs_connection as gc

def main():
    gc.establish_gprs_conn()

if __name__ == '__main__':
    main()
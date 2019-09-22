#!/usr/bin/env python
# coding: utf-8
# info
__version__ = "0.1"
__author__  = "Akli R"
__date__    = "04/10/18"

import subprocess

def establish_gprs_conn():

    cmd = 'gprs connect'

    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)

    (output, err) = p.communicate()

    success = output.find('[CONNECTED]')

    p_status = p.wait()
    
    print "Command output : ", output
    print "Command err : ", err
    print "Command exit status/return code : ", p_status
    print "Success : ", success

    return success

def get_device_mac_address():

    cmd = 'ifconfig ppp0 | grep "HWaddr"'

    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)

    (output, err) = p.communicate()

    out = output.split("HWaddr")

    macAddr = out[1].strip().replace(':','')

    return macAddr

def get_device_ip_address():

    cmd = 'ifconfig ppp0 | grep "inet addr"'

    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)

    (output, err) = p.communicate()

    out = output.split("Bcast")

    out = out[0].split(":")

    ipAddr = out[1].strip()

    return ipAddr

def abort_gprs_conn():

    cmd = 'gprs abort'

    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)

    (output, err) = p.communicate()

    success = output.find('')

    p_status = p.wait()
    
    print "Command output : ", output
    print "Command err : ", err
    print "Command exit status/return code : ", p_status
    print "Success : ", success

    return success


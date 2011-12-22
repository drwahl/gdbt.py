#!/usr/bin/env python

import os, time, subprocess, sys, bluetooth

mac = 'D4:88:90:87:70:90'

def btconnect(mac):
    """ connect to target bluetooth device """

    sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    sock.connect((mac, 1))

    sock.send('hello!!')

    return sock

def btdisconnect(socket):
    """ disconnection from target bluetooth device """

    socket.close()

if __name__ == "__main__":
    """ mainline command """

    if not mac:
        try:
            mac = sys.argv1
        except KeyError:
            mac = raw_input('Bluetooth address: ')
        if not mac:
            print 'Unable to determine target bluetooth mac address'
            sys.exit(1)

    socket = btconnect(mac)        
    print 'Disconnecting in 2 seconds'
    time.sleep(2)
    btdisconnect(socket)
    print 'Garage door toggled' 
    sys.exit(0)

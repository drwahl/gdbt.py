#!/usr/bin/env python

import os, time, subprocess, sys, bluetooth

bt_addr = ''

def btconnect(bt_addr):
    """ connect to target bluetooth device """

    sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    sock.connect((bt_addr, 1))

    sock.send('hello!!')

    return sock

def btdisconnect(socket):
    """ disconnection from target bluetooth device """

    socket.close()

if __name__ == "__main__":
    """ mainline command """

    if not bt_addr:
        try:
            bt_addr = sys.argv1
        except KeyError:
            bt_addr = raw_input('Bluetooth address: ')
        if not bt_addr:
            print 'Unable to determine target bluetooth address'
            sys.exit(1)

    socket = btconnect(bt_addr)
    print 'Disconnecting in 2 seconds'
    time.sleep(2)
    btdisconnect(socket)
    print 'Garage door toggled' 
    sys.exit(0)

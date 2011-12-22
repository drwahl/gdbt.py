#!/usr/bin/env python

import os, time, subprocess, sys, bluetooth, logging

bt_addr = ''
timeout = 2

# logging setup
global_log_level = logging.DEBUG
default_log_file = '/var/log/gdbt/gdbt.log'
default_log_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

logging.basicConfig(filename=default_log_file,
                    level=logging.DEBUG,
                    format='%(asctime)s %(name)s - %(levelname)s - %(message)s',
                    datefmt='%y.%m.%d %H:%M:%S'
                   )
console = logging.StreamHandler(sys.stderr)
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger("gdbt").addHandler(console)

log = logging.getLogger("gdbt")
log.debug("Starting log")

def btconnect(bt_addr):
    """ connect to target bluetooth device """
    log.debug("in btconnect")

    log.debug("intializing socket")
    sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    log.debug("connecting target device to socket")
    sock.connect((bt_addr, 1))
    log.debug("target device connected")

    log.debug("sending 'hello!!' to bluetooth target device")
    sock.send('hello!!')
    log.debug("'hello!!' message sent to bluetooth target device")

    log.debug("returning socket %s" % sock )
    return sock

def btdisconnect(socket):
    """ disconnection from target bluetooth device """
    log.debug("in btdisconnect")

    log.debug("closing socket")
    socket.close()
    log.debug("socket closed")

if __name__ == "__main__":
    """ mainline command """

    if not bt_addr:
        log.debug("bt_addr not set, trying sys.argv[1]")
        try:
            bt_addr = sys.argv[1]
        except IndexError:
            log.debug("bt_addr not supplied at sys.argv[1], prompting for input")
            bt_addr = raw_input('Bluetooth address: ')
        if not bt_addr:
            log.debug("bt_addr not supplied at prompt, giving up")
            log.WARN("Unable to determine target bluetooth address")
            sys.exit(1)

    socket = btconnect(bt_addr)
    log.info("Disconnecting in %i seconds" % timeout)
    time.sleep(timeout)
    btdisconnect(socket)
    log.info("Garage door toggled")
    log.debug("Closing log")
    sys.exit(0)

#udevmonitor.py
#Weston Shakespear

import pyudev
import numpy

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='usb')

while True:
    print(monitor.poll(timeout=1))
    print('asdf')

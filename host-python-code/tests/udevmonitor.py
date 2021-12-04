#udevmonitor.py
#Weston Shakespear

import pyudev
import numpy

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='usb')

for device in iter(monitor.poll, None):
    print('Action: ', end='')
    print(device.action)
    print('Parent: ', end='')
    print(str(device.parent))
    print('Name:' , end='')
    print(str(device.sys_name))
    print(device.get('ID_BUS'))
    print('')

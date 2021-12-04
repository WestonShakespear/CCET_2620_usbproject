#filterparent-listname.py
#Weston Shakespear

import pyudev
import numpy
import subprocess
import os

def notify(message):
    subprocess.Popen(['notify-send', message])
    return


context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='usb')

current_devices = {}

for device in iter(monitor.poll, None):
    c_action = str(device.action)
    c_driver = str(device.driver)
    c_name = str(device.sys_name)

    if c_action == 'add' or c_action == 'remove':

        if c_action == 'add':
            if c_driver == 'usb-storage':
                notify("Device " + c_name + " Attached")
                current_devices[c_name] = device

                c_path = device.sys_path

        elif c_action == 'remove':
            if c_name in current_devices:
                current_devices.pop(c_name)
                notify("Device " + c_name + " Removed")
            print('USB Device ', c_action)

        print('\n\n')
        print('Current devices: ')
        for k in current_devices:
            print(k, end='  -  ')

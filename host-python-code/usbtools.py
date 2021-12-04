import pyudev
import numpy
import subprocess
import os

class usbtools:
    def __init__(self, timeout):
        self.context = pyudev.Context()
        self.monitor = pyudev.Monitor.from_netlink(self.context)
        self.monitor.filter_by(subsystem='usb')

        self.current_devices = {}

    def poll(self):
        c_poll = self.monitor.poll(timeout=1)

        if c_poll != None:
            device = c_poll
            c_action = str(device.action)
            c_driver = str(device.driver)
            c_name = str(device.sys_name)

            if c_action == 'add' or c_action == 'remove':

                if c_action == 'add':
                    if c_driver == 'usb-storage':
                        self.notify("Device " + c_name + " Attached")
                        self.current_devices[c_name] = device

                        c_path = device.sys_path

                elif c_action == 'remove':
                    if c_name in self.current_devices:
                        self.current_devices.pop(c_name)
                        self.notify("Device " + c_name + " Removed")
                    print('USB Device ', c_action)

                print('\n\n')
                print('Current devices: ')
                for k in self.current_devices:
                    print(k, end='  -  ')

            return 1
        else:
            return 0

    def notify(self, message):
        subprocess.Popen(['notify-send', message])
        return

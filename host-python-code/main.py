from usbtools import usbtools
from hubtools import hubtools

looptimeout = 1
port = '/dev/ttyACM1'
baudrate = 115200

usb = usbtools(looptimeout)
hub = hubtools(port, baudrate)



#forever loop
while True:
    usb_status = usb.poll()
    hub_status = hub.poll()

    print("usb: ", usb_status)
    print("hub: ", hub_status)

    if usb_status == 'add' or usb_status == 'remove':
        if usb_status == 'add':
            hub.sendChar('a')
        elif usb_status == 'remove':
            hub.sendChar('r')

    else:
        pass

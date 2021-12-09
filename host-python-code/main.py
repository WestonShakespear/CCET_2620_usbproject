from usbtools import usbtools
from hubtools import hubtools

looptimeout = 1
port = '/dev/ttyACM0'
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
            c = current_num - 1
            if c > 0:
                hub.sendChar('r')
            elif c == 0:
                hub.sendChar('x')
    else:
        current_num = int(usb_status)

    # else:
    #     pass

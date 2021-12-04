from usbtools import usbtools
from hubtools import hubtools

looptimeout = 1

usb = usbtools(looptimeout)
# hub = hubtools()



#forever loop
while True:
    print(usb.poll())

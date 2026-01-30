# usb-powered-relay
for LCUS-1 5V USB Relay Module CH340 USB Control Switch **in LINUX**

![](LCUS-1-5V-USB-Relay-Module.png)

Baud Rate: 9600bps

## HowTo

	Usage: ./usbser2relay.sh <path_to_tty_device> <0|1>
		   0: Turn the Relay ON
		   1: Turn the Relay OF

	Data (1) – startup logo (the default is 0 xA0) Data (2) – switch address code (the default is 0 x01, identifies the first switch) Data (3) – operation data (0 x00 to “off”, 0 x01 to “on”) Data (4) – check code For example: Open the USB switch:A0 01 01 A2 Close the USB switch: A0 01 00 A1

**note**: you should run the script with root permission!

Example:

	# ./test.py
	

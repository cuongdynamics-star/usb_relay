import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600)

cmd_on  = bytes.fromhex('A0 01 01 A2')
cmd_off = bytes.fromhex('A0 01 00 A1')
while True:
    ser.write(cmd_on)   # bật relay
    time.sleep(2)
    ser.write(cmd_off)  # tắt relay
    time.sleep(2)
ser.close()
print("Relay control completed.")
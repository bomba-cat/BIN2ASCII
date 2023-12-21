import serial
import pyautogui as py

binaryLength = 0
binary = ""

try:
    arduino = serial.Serial("/dev/ttyCH341USB0")
except:
    print("Couldn't detect any arduino at any Port, reconnect!")

while True:
    data = str(arduino.readline().decode("utf-8").strip('\r\n'))
    if data:
        binary+=data
        binaryLength+=1
        if binaryLength == 8:
            print('--------------------------------')
            print(binary)
            character = ''.join([chr(int(binary[i:i+8],2)) for i in range(0,len(binary), 8)])
            print(character)
            if character != '=':
                py.write(character)
            elif character == '=':
                py.write('=')
            print('--------------------------------')
            binary = ""
            binaryLength = 0
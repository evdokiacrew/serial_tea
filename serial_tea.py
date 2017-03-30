import serial                                       #Load pySerial module
import time                                         #Load time module

print('Serial Tea: testing serial ports with a mug of black, green or herbal tea :)')
print('Please connect any serial device or a jumper (lock 2 and 3 pin) to test the port.')
print('And enter port nomber (for example "COM1" for Win or "/dev/ttyS1" for *nix). Leave empty for exit.')

port = raw_input('Port: ')                          #Input port file/name
if port == '':                                      #Close program if port is empty
    exit()
ser = serial.Serial(port, timeout=1)                #Opening port
if ser.isOpen():                                    #Print name of port if port is opened
    print('Port ' + ser.name + ' is open...')
while True:                                         #Input text for sending or exit program
    cmd = raw_input("Enter some text or 'exit':")
    if cmd == 'exit':
        ser.close()
        exit()
    else:                                           #Sending text
        ser.write(cmd + '\r\n')
        out = ''                                    #Reset output variable
        time.sleep(2)                               #Wait 2 seconf for port responce
        out = ser.readline()                        #Reading port ouput
        if out != '':
            print('Receiving: ' + out)
            print('Seems like port is functioning normally. Lets drink some tea.')
        else:
            print('We waited 3 seconds but received no response. Maybe port is malfunctioning?')
import serial
import time

## This serial port will change depending on your OS and other things
## A good way to find your port is to open up the Arduino IDE, click
## Tools -> Port and the string before your arduino is the port.
SERIAL_PORT = 'COM3' 
BAUD = 9600

class Arduino:
  def __init__(self):
    super().__init__()

    self.arduino  = serial.Serial(SERIAL_PORT, BAUD)
    print("Arduino connected")

    ## neccesary for the arduino to start up
    time.sleep(1) 

  def send(self, command):
    self.arduino.write(command.encode('utf8'))

    ## Arduino echoes back that the delay is changing
    return self.arduino.readline()
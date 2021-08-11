# SERVER COMMUNICATIONS
import socket
import threading
import time
from .Arduino import Arduino

class ServerComms:
  def __init__(self, HOST, PORT):
    self.HOST = HOST
    self.PORT = PORT

    ## Connect Arduino
    self.arduino = Arduino()

    ## Create Server Socket
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.socket.bind((HOST, PORT))

    ## Wait for client to connect
    self.socket.listen(5)
    self.conn, self.address = self.socket.accept()
    self.receive()

  def receive(self):
        received = ""
        sending = ""
        while(True):
            received = self.conn.recv(2048)
            received = received.decode('utf8')

            if(received == "quit"):
                print("Serving shutting down.")
                self.socket.close()
                break
            else:
                print("SENDING TO ARDUINO: " + received)
                response = self.arduino.send(received).decode('utf8')
                print("Arduino sent: ", response)

  def send(self, command):
    self.socket.send(command.encode('utf8'))

  def close(self):
    self.arduino.close()
    self.socket.close()

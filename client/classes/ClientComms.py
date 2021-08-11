# CLIENTS COMMUNICATIONS
import socket
import threading

class ClientComms:
  def __init__(self, HOST, PORT):
    self.HOST = HOST
    self.PORT = PORT

    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  def connect(self):
    self.socket.connect((self.HOST, self.PORT))

  def send(self, command):
    self.socket.send(command.encode('utf8'))

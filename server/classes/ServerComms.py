# SERVER COMMUNICATIONS
import socket
import threading
import time

class ServerComms:
  def __init__(self, HOST, PORT):
    self.HOST = HOST
    self.PORT = PORT

    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.socket.bind((HOST, PORT))

  def connect(self):
    self.socket.listen(5)
    self.conn, self.address = self.socket.accept()

    self.receive()

    # self.receive_thread = threading.Thread(target=self.receive)
    # self.receive_thread.start()

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
                print("RECEIVED MSG: " + received)
                    

  def send(self, command):
    self.socket.send(command.encode('utf8'))

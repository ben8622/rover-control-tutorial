# Client main.py
from classes import ServerComms

HOST = "localhost"
PORT = 5000

def main():
  comms = ServerComms.ServerComms(HOST, PORT)
  comms.connect()

if __name__ == "__main__":
  main()
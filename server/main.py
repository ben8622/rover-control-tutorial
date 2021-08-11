# Client main.py
from classes import ServerComms

HOST = "localhost"
PORT = 5000

def main():
  comms = ServerComms.ServerComms(HOST, PORT)
  comms.close()

if __name__ == "__main__":
  main()
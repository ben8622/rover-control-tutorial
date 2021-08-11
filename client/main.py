# Client main.py
from classes import ClientComms
from tkinter import *

HOST = "localhost"
PORT = 5000

root = Tk()
root.title("Rover Control Tutorial")
command_entry = Entry(root)
command_entry.pack(padx=5, pady=5)
btn = Button(root, text="Send Command", bg="green", fg="white")
btn.pack(padx=5, pady=5)

def main():
  comms = ClientComms.ClientComms(HOST, PORT)
  comms.connect()
  print("Comms connected!")

  btn['command'] = lambda: comms.send(command_entry.get())

  root.mainloop()


  # while(True):
  #   command = input("Send a message to the server: ")
  #   if(command == "quit"):
  #     comms.send(command)
  #     comms.socket.close()
  #     break
  #   comms.send(command)

  comms.send("quit")
  coms.close()
  print("Client shutting down.")

if __name__ == "__main__":
  main()
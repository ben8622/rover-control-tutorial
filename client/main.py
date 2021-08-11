# Client main.py
from classes import ClientComms
from tkinter import *

## Socket Connection Info
HOST = "localhost"
PORT = 5000

## GUI Setup
root = Tk()
root.title("Rover Control Tutorial")
command_entry = Entry(root)
command_entry.pack(padx=5, pady=5)
btn = Button(root, text="Send Command", bg="green", fg="white")
btn.pack(padx=5, pady=5)

def main():
  ## Connect the socket
  comms = ClientComms.ClientComms(HOST, PORT)
  print("Comms connected!")

  ## Assign a callback when the button gets pushed in GUI
  btn['command'] = lambda: comms.send(command_entry.get())

  root.mainloop()

  ## Mainloop exits, send quit to server and cleanup
  comms.send("quit")
  comms.socket.close()
  print("Client shutting down.")

if __name__ == "__main__":
  main()
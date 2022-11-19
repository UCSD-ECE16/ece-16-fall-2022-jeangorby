"""
@author: Ramsin Khoshabeh
"""

from ECE16Lib.Communication import Communication
import ECE16Lib.DSP as filt
import numpy as np
from time import sleep
import socket, pygame

# Setup the Socket connection to the Space Invaders game
host = "127.0.0.1"
port = 65432
mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mySocket.connect((host, port))
mySocket.setblocking(False)

class PygameController:
  comms = None

  def __init__(self, serial_name, baud_rate):
    self.comms = Communication(serial_name, baud_rate)

  def run(self):
    # 1. make sure data sending is stopped by ending streaming
    self.comms.send_message("stop")
    self.comms.clear()

    # 2. start streaming orientation data
    input("Ready to start? Hit enter to begin.\n")
    self.comms.send_message("start")

    # 3. Forever collect orientation and send to PyGame until user exits
    print("Use <CTRL+C> to exit the program.\n")

    while True:
      message = self.comms.receive_message()
      if(message != None):
        command = None

        try:
          (ax, ay, az) = message.split(',')
        except ValueError:        # if corrupted data, skip the sample
          continue

        orientation = filt.l1_norm(int(ax), int(ay), int(az))

        if(orientation == 0):
          command = "FIRE"
        elif(orientation < 6150):
          command = "RIGHT"
        elif(orientation > 6450):
          command = "LEFT"
        
        # message = int(message)
        # # if message == 0:
        # #   command = "FLAT"
        # # if message == 1:
        # #   command = "UP"
        # if message == 2:
        #   command = "FIRE"
        # elif message == 3:
        #   command = "RIGHT"
        # elif message == 4:
        #   command = "LEFT"

        if command is not None:
          mySocket.send(command.encode("UTF-8"))


if __name__== "__main__":
  serial_name = "COM4"
  baud_rate = 115200
  controller = PygameController(serial_name, baud_rate)

  try:
    controller.run()
  except(Exception, KeyboardInterrupt) as e:
    print(e)
  finally:
    print("Exiting the program.")
    controller.comms.send_message("stop")
    controller.comms.close()
    mySocket.send("QUIT".encode("UTF-8"))
    mySocket.close()

  input("[Press ENTER to finish.]")

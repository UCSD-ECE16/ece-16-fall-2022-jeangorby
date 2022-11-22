"""
@author: Ramsin Khoshabeh
"""

from ECE16Lib.Communication import Communication
import ECE16Lib.DSP as filt
import numpy as np
from math import sqrt, atan
from time import sleep, time
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
    X_ZERO = 1850
    Y_ZERO = 1850
    Z_ZERO = 1950
    refresh_time = 0.01
    previous_time = time()
    while True:
      message = self.comms.receive_message()
      if(message != None):
        command = None
        try:
          (ax, ay, az, ppg) = message.split(',')
        except ValueError:        # if corrupted data, skip the sample
          continue
        
        ax = int(ax)-X_ZERO
        ay = int(ay)-Y_ZERO
        az = int(az)-Z_ZERO

        # X-Axis
        result=sqrt(ay**2+az**2)
        result=ax/result
        accel_angle_x = atan(result)*180

        # Y Axis
        result=sqrt(ax**2+az**2)
        result=ay/result
        accel_angle_y = atan(result)*180

        # print(accel_angle_x)
        if(int(ppg) == -1):
          print("i am taking shot")
          command = "FIRE"
          continue
        
        current_time = time()
        if current_time - previous_time > refresh_time:
          print(accel_angle_x)
          previous_time = current_time
          
          if(int(ppg) < 5000):
            command = "PAUSE"
          elif(accel_angle_x < 0):
            command = "RIGHT"
          elif(accel_angle_x > 60):
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
  serial_name = "COM3"
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

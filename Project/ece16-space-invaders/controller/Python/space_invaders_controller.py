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

    ppg_down = False
    sens = np.array([[-10, 60],[0,40],[-200,200]])
    sens_counter = 0

    game_start = False

    response = ""
    while True:
      # Receive message from arduino
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
        current_time = time()

        # print(accel_angle_y)
        if int(ppg) == -1 and game_start == False:
          command = "START"
          game_start = True
        elif game_start == True:
          
          # PPG Debouncing
          if int(ppg) < 7000 and ppg_down == False and int(ppg) != -1 and int(ppg) != -2:
            ppg_down = True

          # Keep track of which sensitivity profile is being used
          if(int(ppg) == -2 and sens_counter < 2):
            sens_counter = sens_counter + 1
          elif(int(ppg) == -2 and game_start == True):
            sens_counter = 0

          # Prioritze firing over any other command
          if(int(ppg) == -1):
            command = "FIRE"
          # Check for movement/pause/quit every refresh time
          elif current_time - previous_time > refresh_time and command != "FIRE":
            previous_time = current_time
            
            if(int(ppg) > 7000 and ppg_down == True):
              ppg_down = False
              command = "PAUSE"
            # Sens 1: -10,60; sens 2: 0,40; sens 3: -200,200
            elif(accel_angle_x < sens[sens_counter][0]):
              command = "RIGHT"
            elif(accel_angle_x > sens[sens_counter][1]):
              command = "LEFT"
            elif(accel_angle_y < -200):
              command = "QUIT"
        

        if command is not None:
          mySocket.send(command.encode("UTF-8"))

        # Receive response from the server
        try:
          response = mySocket.recv(1024)
          response = response.decode("utf-8")
          print("Response: ", response)
        except BlockingIOError:
          pass # do nothing if there's no data

        if(response == "HIT"):
          self.comms.send_message("HIT")
          response = ""



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

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 00:03:15 2022
@author: chuha
"""

from ECE16Lib.Communication import Communication
from ECE16Lib.CircularList import CircularList
from ECE16Lib.Pedometer import Pedometer
from matplotlib import pyplot as plt
from time import time
import numpy as np

if __name__ == "__main__":
  fs = 50                         # sampling rate
  num_samples = 250               # 5 seconds of data @ 50Hz
  process_time = 1                # compute the step count every second

  ped = Pedometer(num_samples, fs, [])

  comms = Communication("COM4", 115200)
  comms.clear()                   # just in case any junk is in the pipes
  comms.send_message("wearable")  # begin sending data

  recording = True
  print("Connected to board successfully")

  counter = 0
  try:
    # previous_time = time()
    while(recording):
      message = comms.receive_message()
      if(message != None):
        print(message)
        try:
          (m2, m3, m4) = message.split(',')
        except ValueError:        # if corrupted data, skip the sample
          continue
        # Collect data in the pedometer
        ped.add(int(m2),int(m3),int(m4))
        counter = counter + 1

      if(counter == 256):
        print("got to done if statement")
        recording = False

    print("Got out of loop")
    # After receiving all the data, process it
    steps, peaks, filtered = ped.process()
    # print("got hereeeeee")
    print("Step count: {:d}".format(steps))
    comms.send_message("Step count: {:d}".format(steps))

  except(Exception, KeyboardInterrupt) as e:
    print(e)                     # Exiting the program due to exception
  finally:
    print("Closing connection.")
    comms.send_message("sleep")  # stop sending data
    comms.close()
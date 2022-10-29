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

  step_count = 0
  jump_count = 0
  recording = True
  print("Connected to board successfully")
  done_flag = 0
  counter = 0
  try:
    # previous_time = time()
    comms.send_message("Step count: {:d},Jump count: {:d}".format(step_count, jump_count))
    while(True):
      if(recording):
        message = comms.receive_message()
        if(message != None):
          print(message)

          try:
            done_flag = int(message)
          except ValueError:
            pass

          try:
            (m2, m3, m4) = message.split(',')
          except ValueError:        # if corrupted data, skip the sample
            continue
          # Collect data in the pedometer
          ped.add(int(m2),int(m3),int(m4))
          counter += 1
          print(counter)

        if(done_flag == 71):
          recording = False
          done_flag = 0
      else:
        # After receiving all the data, process it
        steps, jumps, peaks, filtered = ped.process()
        # print("got hereeeeee")
        step_count = steps
        jump_count = jumps
        print("Step count: {:d},Jump count: {:d}".format(step_count, jump_count))
        comms.send_message("Step count: {:d}, Jump count: {:d}".format(step_count, jump_count))

        # reset to 0 so they don't double the next set
        steps = 0
        jumps = 0

        # counter = 0
        recording = True

  except(Exception, KeyboardInterrupt) as e:
    print(e)                     # Exiting the program due to exception
  finally:
    print("Closing connection.")
    comms.send_message("sleep")  # stop sending data
    comms.close()
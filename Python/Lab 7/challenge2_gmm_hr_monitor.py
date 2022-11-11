from ECE16Lib.Communication import Communication
from ECE16Lib.CircularList import CircularList
from ECE16Lib.HRMonitor import HRMonitor
from matplotlib import pyplot as plt
from time import time
import numpy as np

if __name__ == "__main__":
  fs = 50                         # sampling rate
  num_samples = 500               # 5 seconds of data @ 50Hz
  refresh_time = 10                # update heartrate every second

  times = CircularList([], num_samples)
  ppg = CircularList([], num_samples)

  comms = Communication("COM3", 115200)
  comms.clear()                   # just in case any junk is in the pipes
  comms.send_message("wearable")  # begin sending data

  hrmon = HRMonitor(500, 50)
  hrmon.train()
  
  try:
    previous_time = time()
    while(True):
      message = comms.receive_message()
      if(message != None):
        try:
          (m1, m2) = message.split(',')
        except ValueError:        # if corrupted data, skip the sample
          continue

        # add the new values to the circular lists
        # hrmon.add(int(m1), int(m2))
        times.add(int(m1))
        ppg.add(int(m2))

        # if enough time has elapsed, update the LED display with the current heartrate
        current_time = time()
        if (current_time - previous_time > refresh_time):
          previous_time = current_time

          data = np.column_stack([times, ppg])
          data_t = data[:, 0]
          data_t = (data_t - data_t[0])/1e3
          data_ppg = data[:, 1]

        #   print(data_t)
          hrmon.add(data_t, data_ppg)

          hr = hrmon.predict()

          hr_round = round(hr, 3)
          hr_str = str(hr_round)
          print(hr_str)

          comms.send_message(hr_str)

  except(Exception, KeyboardInterrupt) as e:
    print(e) # exiting the program due to exception
  finally:
    print("Closing connection.")
    comms.send_message("sleep")  # stop sending data
    comms.close()
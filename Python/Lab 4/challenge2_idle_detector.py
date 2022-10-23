from ECE16Lib.Communication import Communication
from ECE16Lib.CircularList import CircularList
from matplotlib import pyplot as plt
from time import time, sleep
import numpy as np

if __name__ == "__main__":
  num_samples = 100               # 2 seconds of data @ 50Hz
  refresh_time = 0.1              # update the plot every 0.1s (10 FPS)
  on = True

  times = CircularList([], num_samples)
  ax = CircularList([], num_samples)
  ay = CircularList([], num_samples)
  az = CircularList([], num_samples)

  average_x = CircularList([], num_samples)
  N = 70

  delta_z = CircularList([], num_samples)
  # delta_y = CircularList([], num_samples)
  # delta_x = CircularList([], num_samples)

  comms = Communication("COM4", 115200)
  comms.clear()                   # just in case any junk is in the pipes
  comms.send_message("off")  # begin sending data

  try:
    previous_time = 0
    time_inactive = 0
    while(True):
      # Getting the accelerometer readings
      message = comms.receive_message()
      if(message != None):
        try:
          (m1, m2, m3, m4) = message.split(',')
        except ValueError:        # if corrupted data, skip the sample
          pass

        # add the new values to the circular lists
        times.add(int(m1))
        ax.add(int(m2))
        ay.add(int(m3))
        az.add(int(m4))
        
        average_x.add(np.mean(ax[:N]))
        delta_z.add(int(m4) - az[num_samples - 2])
        # delta_y.add(int(m3) - ay[num_samples - 2])
        # delta_x.add(int(m2) - ax[num_samples - 2])

        # if enough time has elapsed, clear the axis, and plot az
        current_time = time()
        if (current_time - previous_time > refresh_time):
          previous_time = current_time

          # plt.cla()
          # plt.plot(delta_z)
          inactivity = current_time - time_inactive
          print(inactivity)
          # print(on)
          # Checking if the button is pressed
          if(any(i>100 for i in delta_z)):
            on = not on
            time_inactive = current_time
            delta_z.clear()

          if(any(i>1940 for i in average_x) and on == True):
            comms.clear()
            comms.send_message("active")
            time_inactive = current_time
          elif(inactivity > 5 and inactivity < 10 and on == True):
            comms.clear()
            comms.send_message("inactive_5")
          elif(inactivity > 10 and on == True):
            comms.clear()
            comms.send_message("inactive_10")
          elif(on == False):
            comms.clear()
            comms.send_message("off")
          elif(on == True):
            comms.clear()
            comms.send_message("on")

          # plt.show(block=False)
          # plt.pause(0.001)
    

  except(Exception, KeyboardInterrupt) as e:
    print(e)                     # Exiting the program due to exception
  finally:
    comms.send_message("sleep")  # stop sending data
    comms.close()
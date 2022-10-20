from ECE16Lib.Communication import Communication
from ECE16Lib.CircularList import CircularList
from matplotlib import pyplot as plt
from time import time
import numpy as np

if __name__ == "__main__":
  num_samples = 100               # 2 seconds of data @ 50Hz
  refresh_time = 0.2              # update the plot every 0.1s (10 FPS)

  times = CircularList([], num_samples)
  ax = CircularList([], num_samples)
  ay = CircularList([], num_samples)
  az = CircularList([], num_samples)

  N = 70

#   average_x = CircularList([], num_samples)
  delta_z = CircularList([], num_samples)
  delta_y = CircularList([], num_samples)
  delta_x = CircularList([], num_samples)
#   L1 = CircularList([], num_samples)
#   L2 = CircularList([], num_samples)
#   transformed  = CircularList([], num_samples)

  comms = Communication("COM4", 115200)
  comms.clear()                   # just in case any junk is in the pipes
  comms.send_message("wearable")  # begin sending data

  try:
    previous_time = 0
    while(True):
      message = comms.receive_message()
      if(message != None):
        try:
          (m1, m2, m3, m4) = message.split(',')
        except ValueError:        # if corrupted data, skip the sample
          continue


        # add the new values to the circular lists
        times.add(int(m1))
        ax.add(int(m2))
        ay.add(int(m3))
        az.add(int(m4))

        # average_x.add(np.mean(ax[:N]))
        delta_z.add(int(m4) - az[num_samples - 2])
        delta_y.add(int(m3) - ay[num_samples - 2])
        delta_x.add(int(m2) - ax[num_samples - 2])

        # L2.add(np.sqrt((int(m2)**2)+(int(m3)**2)+(int(m4)**2)))
        # L1.add(np.abs(int(m2)) + np.abs(int(m3)) + np.abs(int(m4)))

        # Take the base 10 logarithm of the streamed z value
        # transformed.add(np.log10(int(m4)))

        # if enough time has elapsed, clear the axis, and plot az
        current_time = time()
        if (current_time - previous_time > refresh_time):
          previous_time = current_time
          
        #   plt.cla()
        #   plt.plot(delta_x)
        #   plt.plot(delta_y)
        #   plt.plot(delta_z)


          plt.subplot(311)
          plt.cla()
          plt.title("Delta Z")
          plt.plot(delta_z)

          plt.subplot(312)
          plt.cla()
          plt.title("Delta Y")
          plt.plot(delta_y)

          plt.subplot(313)
          plt.cla()
          plt.title("Delta X")
          plt.plot(delta_x)

          plt.show(block=False)
          plt.pause(0.001)
  except(Exception, KeyboardInterrupt) as e:
    print(e)                     # Exiting the program due to exception
  finally:
    comms.send_message("sleep")  # stop sending data
    comms.close()
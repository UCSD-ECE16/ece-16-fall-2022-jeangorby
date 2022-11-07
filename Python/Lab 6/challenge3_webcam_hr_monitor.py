from ECE16Lib.Communication import Communication
from ECE16Lib.CircularList import CircularList
from ECE16Lib.HRMonitor import HRMonitor
import numpy as np
import cv2
import time

if __name__ == "__main__":
  fs = 50                                        # sampling rate
  num_samples = 500                              # 5 seconds of data @ 50Hz
  refresh_time = 1                               # update heartrate every second

  times = CircularList([], num_samples)          # to store times
  ppg = CircularList([], num_samples)            # to store ppg

  comms = Communication("COM4", 115200)
  comms.clear()                                  # just in case any junk is in the pipes
  # comms.send_message("wearable")                 # begin sending data

  hrmon = HRMonitor(500, 50)
  cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)       # For Windows Users

  try:
    previous_time = time.time()
    sample_start_time = time.time_ns() / (10**9)
    while(True):
      # Initializing OpenCV
      _, frame = cap.read()
      # Retrieving data from the webcam
      new_sample = frame.mean(axis=0).mean(axis=0)
      new_sample = new_sample[2]  # focusing on the RED channel


      sample_time = time.time_ns()
      sample_time = sample_time / (10 ** 9)

      times.add(sample_time - sample_start_time)
      ppg.add(new_sample)
      

      # if enough time has elapsed, update the LED display with the current heartrate
      current_time = time.time()
      if (current_time - previous_time > refresh_time):
        previous_time = current_time

        data = np.column_stack([times, ppg])
        data_t = data[:, 0]
        data_t = (data_t - data_t[0])
        data_ppg = data[:, 1]

        hrmon.add(data_t, data_ppg)
        hr, peaks, filtered = hrmon.process()

        hr_round = round(hr, 3)
        hr_str = str(hr_round)
        print(hr_str)
        comms.send_message(hr_str)

      cv2.imshow('Input', frame)

      if cv2.waitKey(1) & 0xFF == ord('q'):
        break

  except(Exception, KeyboardInterrupt) as e:
    cap.release()
    cv2.destroyAllWindows()
    print(e) # exiting the program due to exception
  finally:
    cap.release()
    cv2.destroyAllWindows()

    print("Closing connection.")
    comms.send_message("sleep")  # stop sending data
    comms.close()
import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

ppg = []

# cap = cv2.VideoCapture(0) # choose your appropriate camera!
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
while(True):
  _, frame = cap.read() 

  new_sample = frame.mean(axis=0).mean(axis=0)
  new_sample = new_sample[0] # replace the ? with index of the RED channel
  ppg.append(new_sample) # append new_sample to ppg

  cv2.imshow('Input', frame)
  c = cv2.waitKey(1)
  if c == 27:
    break
cap.release()
cv2.destroyAllWindows()

fig = plt.figure()
ax = plt.axes()

p = ppg[10:] # remove the first few points because of auto-exposure

x = np.linspace(0, 1, len(p))
ax.plot(x, p)
plt.show()

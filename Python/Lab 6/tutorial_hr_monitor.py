from ECE16Lib.HRMonitor import HRMonitor
import numpy as np
import matplotlib.pyplot as plt

# Load the data as a 500x2 ndarray and extract the 2 arrays
data = np.genfromtxt("./data/A15955623/A15955623_04_75.csv", delimiter=",")
t = data[:,0]
t = (t - t[0])/1e3
ppg = data[:,1]

# Test the Heart Rate Monitor with offline data
hr_monitor = HRMonitor(3000, 50)
hr_monitor.add(t, ppg)
hr, peaks, filtered = hr_monitor.process()

# Plot the results
plt.plot(t, filtered)
plt.title("Estimated Heart Rate: {:.2f} bpm".format(hr))
plt.plot(t[peaks], filtered[peaks], 'rx')
plt.plot(t, [0.5]*len(filtered), "b--")
plt.show()
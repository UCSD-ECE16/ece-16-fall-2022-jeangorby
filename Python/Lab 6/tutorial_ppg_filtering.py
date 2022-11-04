from math import inf
import ECE16Lib.DSP as filt
from matplotlib import pyplot as plt
import numpy as np
import scipy.signal as sig

# Load the data as a 500x2 ndarray and extract the 2 arrays
data = np.genfromtxt("./data/A15955623/A15955623_08_114.csv", delimiter=",")
t = data[:,0]
t = (t - t[0])/1e3
ppg = data[:,1]

# Detrend the signal and plot the result
dt = filt.detrend(ppg, 25)

plt.subplot(211)
plt.title("Detrend")
plt.plot(t, ppg)
plt.subplot(212)
plt.plot(t, dt)
plt.show()

# Smooth the signal with a small moving average
ma = filt.moving_average(dt, 5)

plt.subplot(211)
plt.title("Moving Average")
plt.plot(t, ppg)
plt.subplot(212)
plt.plot(t, ma)
plt.show()

# Highlight the peaks with the derivative
grad = filt.gradient(ma)

plt.subplot(211)
plt.title("Gradient")
plt.plot(t, ppg)
plt.subplot(212)
plt.plot(t, grad)
plt.show()

# Normalize the signal
norm = filt.normalize(grad)

plt.subplot(211)
plt.title("Normalize")
plt.plot(t, ppg)
plt.subplot(212)
plt.plot(t, norm)
plt.show()

# Count the peaks
thresh = 0.6
count, peaks = filt.count_peaks(norm, thresh, 1)

plt.plot(t, norm)
plt.title("Detected Peaks = %d" % count)
plt.plot(t[peaks], norm[peaks], 'rx')
plt.plot(t, [thresh]*len(norm), "b--")
plt.show()

freqs, power = filt.psd(norm, len(norm), 50)

peaks, _ = sig.find_peaks(power)                # finding the peak of power distribution
loc = []
max_peak = 0
max_peak_loc = 0
nearest_min = 0

for peak in peaks:
  if(power[peak] > max_peak):
    max_peak = power[peak]
    max_peak_loc = peak

for i in range(len(freqs)):
    try:
        if(power[i+max_peak_loc] < 0.001):
            nearest_min = i + max_peak_loc
            break
    except IndexError:
        break


plt.plot(freqs, power)
plt.title("Power Spectral Density")
plt.plot(freqs[max_peak_loc], power[max_peak_loc], 'rx')
plt.plot(freqs[nearest_min], power[nearest_min], 'bx')
plt.show()

cutoff = freqs[nearest_min]
b, a = filt.create_filter(3, cutoff, "lowpass", 50)
hp = filt.filter(b, a, norm) 

plt.plot(hp)
plt.show()


# Compute the heart rate
avg_beat_time = np.mean(np.diff(t[peaks]))
bpm = 60/avg_beat_time
print("Estimated heart rate: {:.2f} bpm".format(bpm))

# Estimated heart rate: 74.37 bpm
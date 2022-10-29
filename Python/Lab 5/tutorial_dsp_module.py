import ECE16Lib.DSP as filt
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig

fs = 50      # sampling rate
t_low = 75   # lower peak threshold
t_high = 220 # upper peak threshold

def load_data(filename):
  return np.genfromtxt(filename, delimiter=",")

# Load the data as a 500x4 ndarray
# data = load_data("./data/8steps_10s_50hz.csv")
data = load_data("./data/jump_test3.csv")
t = data[:,0]
t = (t - t[0])/1e3
ax = data[:,1]
ay = data[:,2]
az = data[:,3]

l1 = filt.l1_norm(ax, ay, az)                      # Compute the L1-Norm
ma = filt.moving_average(l1, 15)                   # Compute Moving Average
dt = filt.detrend(ma)                              # Detrend the Signal
# grad = filt.gradient(dt)                           # Compute the Gradient
freqs, power = filt.psd(az, len(az), 50)           # Power Spectral Density
peaks, _ = sig.find_peaks(power)

max_peak = 0
max_peak_loc = 0

for peak in peaks:
  if(power[peak] > max_peak):
    max_peak = power[peak]
    max_peak_loc = peak

cutoff = freqs[max_peak_loc] + 0.1*freqs[max_peak_loc]

bl, al = filt.create_filter(3, cutoff, "lowpass", fs)   # Low-pass Filter Design
lp = filt.filter(bl, al, dt)                       # Low-pass Filter Signal

grad = filt.gradient(dt)
ma2 = filt.moving_average(grad, 15)               # Moving Average
x = filt.detrend(ma2, 15)                       # Detrend

x = 10*x 

count, peaks = filt.count_peaks(lp, t_low, t_high) # Find & Count the Peaks

# Plot the results
plt.plot(t, lp)
plt.title("Detected Peaks = %d" % count)
plt.plot(t[peaks], lp[peaks], 'rx')
plt.plot(t, [t_low]*len(lp), "b--")
plt.plot(t, [t_high]*len(lp), "b--")
plt.show()

data = load_data("./data/test2.csv")
t = data[:,0]
t = (t - t[0])/1e3
ax = data[:,1]
ay = data[:,2]
az = data[:,3]

l1 = filt.l1_norm(ax, ay, az)                      # Compute the L1-Norm
ma = filt.moving_average(l1, 15)                   # Compute Moving Average
dt = filt.detrend(ma)                              # Detrend the Signal
# grad = filt.gradient(dt)                           # Compute the Gradient
freqs, power = filt.psd(az, len(az), 50)           # Power Spectral Density
peaks, _ = sig.find_peaks(power)

max_peak = 0
max_peak_loc = 0

for peak in peaks:
  if(power[peak] > max_peak):
    max_peak = power[peak]
    max_peak_loc = peak

cutoff = freqs[max_peak_loc] + 0.1*freqs[max_peak_loc]

bl, al = filt.create_filter(3, cutoff, "lowpass", fs)   # Low-pass Filter Design
lp = filt.filter(bl, al, dt)                       # Low-pass Filter Signal

grad = filt.gradient(dt)
ma2 = filt.moving_average(grad, 15)               # Moving Average
x = filt.detrend(ma2, 15)                       # Detrend

x = 10*x 

count, peaks = filt.count_peaks(lp, 7, 60) # Find & Count the Peaks

# Plot the results
plt.plot(t, lp)
plt.title("Detected Peaks = %d" % count)
plt.plot(t[peaks], lp[peaks], 'rx')
plt.plot(t, [7]*len(lp), "b--")
plt.plot(t, [60]*len(lp), "b--")
plt.show()
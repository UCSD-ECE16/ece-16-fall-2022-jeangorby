import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from ECE16Lib.HRMonitor import HRMonitor

"""
Function defined to get the heart rate using the heart rate monitor class
by passing in data
"""
def eval_hr_monitor(data):
    hr_monitor = HRMonitor(3000, 50)
    t = data[:,0]
    t = (t - t[0])/1e3
    ppg = data[:,1]

    hr_monitor.add(t, ppg)
    hr, peaks, filtered = hr_monitor.process()
    return hr


# retrieving all the data from the saved csv files
data1 = np.genfromtxt("./data/A15955623/A15955623_01_75.csv", delimiter=",")
data2 = np.genfromtxt("./data/A15955623/A15955623_04_75.csv", delimiter=",")
data3 = np.genfromtxt("./data/A15955623/A15955623_06_80.csv", delimiter=",")
data4 = np.genfromtxt("./data/A15955623/A15955623_08_102.csv", delimiter=",")
data5 = np.genfromtxt("./data/A15955623/A15955623_10_87.csv", delimiter=",")

# evaluating the heart rate
hr1 = eval_hr_monitor(data1)
hr2 = eval_hr_monitor(data2)
hr3 = eval_hr_monitor(data3)
hr4 = eval_hr_monitor(data4)
hr5 = eval_hr_monitor(data5)

# creating the ground truth and estimates array
ground_truth = np.array([75,75,80,114,87])      # reference heart rates
estimates =  np.array([hr1,hr2,hr3,hr4,hr5])    # estimated heart rates from your algorithm


[R,p] = stats.pearsonr(ground_truth, estimates) # correlation coefficient

plt.figure(1)
plt.clf()

# Correlation Plot
plt.subplot(211)
plt.plot(estimates, estimates)
plt.scatter(ground_truth, estimates)

plt.ylabel("Estimated HR (BPM)")
plt.xlabel("Reference HR (BPM)")
plt.title("Correlation Plot: Coefficient (R) = {:.2f}".format(R))

# Bland-Altman Plot
avg =  ground_truth + estimates / 2     # take the average between each element of the ground_truth and
                                                        # estimates arrays and you should end up with another array
dif = ground_truth - estimates                 # take the difference between ground_truth and estimates
std = np.std(dif)                                       # get the standard deviation of the difference (using np.std)
bias = np.mean(dif)                                     # get the mean value of the difference
upper_std = bias + 1.96*std                             # the bias plus 1.96 times the std
lower_std = bias - 1.96*std                             # the bias minus 1.96 times the std

plt.subplot(212)
plt.scatter(avg, dif)

plt.plot(avg, len(avg)*[bias])
plt.plot(avg, len(avg)*[upper_std])
plt.plot(avg, len(avg)*[lower_std])

plt.legend(["Mean Value: {:.2f}".format(bias),
  "Upper bound (+1.96*STD): {:.2f}".format(upper_std),
  "Lower bound (-1.96*STD): {:.2f}".format(lower_std)
])

plt.ylabel("Difference between estimates and ground_truth (BPM)")
plt.xlabel("Average of estimates and ground_truth (BPM)")
plt.title("Bland-Altman Plot")
plt.show()
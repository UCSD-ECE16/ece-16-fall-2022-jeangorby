import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4]  # x data vector (as a list)
y = [1,4,9,16] # y data vector (as a list)
# plt.clf()      # clear any existing plot
# plt.plot(x,y)  # write the data onto the figure buffer
# plt.show()     # show the figure

# This prints 4 different lines where the first row values are taken
# as the start point and the second row values are the end points
a = np.array([[1,2,3,4],[1,4,9,16]])
# plt.clf()
# plt.plot(a)
# plt.show()

a = np.array([[1,2,3,4],[1,4,9,16]])
x = a[0,:] #index from a to get [1,2,3,4]
y = a[1,:] #index from a to get [1,4,9,16]
plt.title("First plot!")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,x)
plt.plot(x,y)
plt.show()

plt.clf()
plt.subplot(211)
plt.plot([1,2,3,4],[1,4,9,16])
plt.subplot(212)
plt.plot([1,2,3,4],[4,2,1,6])
plt.show()
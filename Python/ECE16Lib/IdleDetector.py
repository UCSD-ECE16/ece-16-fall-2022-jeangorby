"""
A class to provide a self-contained idle detector
"""
from ECE16Lib.Communication import Communication
from ECE16Lib.CircularList import CircularList
from matplotlib import pyplot as plt
from time import time
import numpy as np

class IdleDetector():

    def __init__(self):
        self.num_samples = 100               # 2 seconds of data @ 50Hz
        self.refresh_time = 0.1              # update the plot every 0.1s (10 FPS)
        self.on = True

        self.az = CircularList([], self.num_samples)
        self.ax = CircularList([], self.num_samples)
        self.average_x = CircularList([], self.num_samples)
        self.N = 70

        self.delta_z = CircularList([], self.num_samples)
    
    def run(self):
        comms = self.startCommunication()
        try:
            previous_time = 0
            time_inactive = 0
            while(True):
                self.collectData(comms)
                current_time = time()
                if (current_time - previous_time > self.refresh_time):
                    # self.plotData()
                    previous_time = current_time

                    inactivity = current_time - time_inactive
                    print(inactivity)

                    if(self.checkButtonPress()):
                        time_inactive = current_time

                    time_inactive = self.evaluateData(inactivity, current_time, time_inactive, comms)
            
        except(Exception, KeyboardInterrupt) as e:
            print(e)                     # Exiting the program due to exception
        finally:
            self.closeCommunication(comms)
    
    def startCommunication(self):
        comms = Communication("COM4", 115200)
        comms.clear()                   # just in case any junk is in the pipes
        comms.send_message("off")  # begin sending data
        return comms

    def closeCommunication(self, comms):
        comms.send_message("sleep")  # stop sending data
        comms.close()

    def collectData(self, comms):
        message = comms.receive_message()
        if(message != None):
            try:
                (m1, m2, m3, m4) = message.split(',')
            except ValueError:        # if corrupted data, skip the sample
                return

            # add the new values to the circular lists
            self.ax.add(int(m2))
            self.az.add(int(m4))

            self.average_x.add(np.mean(self.ax[:self.N]))
            self.delta_z.add(int(m4) - self.az[self.num_samples - 2])

    def checkButtonPress(self):
        # Checking if the button is pressed
        if(any(i>100 for i in self.delta_z)):
            self.on = not self.on
            self.delta_z.clear()
            return True

    def evaluateData(self, inactivity, current_time, time_inactive, comms):
        if(any(i>1940 for i in self.average_x) and self.on == True):
            comms.clear()
            comms.send_message("active")
            time_inactive = current_time
            return time_inactive
        elif(inactivity > 5 and inactivity < 10 and self.on == True):
            comms.clear()
            comms.send_message("inactive_5")
        elif(inactivity > 10 and self.on == True):
            comms.clear()
            comms.send_message("inactive_10")
        elif(self.on == False):
            comms.clear()
            comms.send_message("off")
        elif(self.on == True):
            comms.clear()
            comms.send_message("on")

        return time_inactive

    def plotData(self):
        plt.subplot(211)
        plt.cla()
        plt.plot(self.delta_z)
        plt.title("Check Button Press")

        plt.subplot(212)
        plt.cla()
        plt.plot(self.average_x)
        plt.title("Check Activity")

        plt.show(block=False)
        plt.pause(0.001)
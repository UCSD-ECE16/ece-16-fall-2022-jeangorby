Jean Gorby Calicdan
A15955623

# Lab #7

# Tutorial Review
## Tutorial 1: ML Data Preparation
After the pressure of the hardest tutorial from lab 6, it is finally time to look at the data submitted by everyone in the class and prepare to feed it into our model. <br>

Glob makes its first ever appearance in an ECE 16 lab in order to allow us to easily access files and read from them. The way it works is that instead of hardcoding the path for every folder and file we are interested in, Glob allows for the retrieval of all the files within a folder as long as the proper filepath is provided. <br>

In order to actually extract information from these files, there are two things that are in play. The values within the actual ```.csv``` files and the the name of the file. The name of the file provides the subject name (PID number), trial number, as well as the ground truth heart rate established by the owner of the data. Using the the ground truth heart rate, we can even estimate the sampling rate of the file which can be indicative of bad data. <br>

We can even go as far as visualizing this data by applying the same filtering techiniques we have seen before and then plotting them. When plotting the data, a lot of obstacles were encountered such as incorrect naming conventions, not the same amount of trial numbers as provided in the code, and some data which were inherently bad. To counteract some of these issues, it was necessary to implement a try-except clause to skip some of them in order to view all of the data for verification. <br>

## Tutorial 2: GMM HR Monitor
Now that we have all of our data gathered, we will now put together an actual machine learning model. <br>

We will be using the Gausen Mixture Training method provided by ```scikit-learn``` which was introduced in the lecture videos. The actual code that we will be using from this library can be condensed into initializing the gmm, training it, and then getting predictions out of it. <br> 

In order to get familiar with this model and its capabilities, we will be using Ramsin's data as a test subject. For this test, we will simply use this data as both the training and test subject in order to see that this isn't good practice at all. It is obvious that the fitting as a result of this test is too good to be true because it absolutely is, and predicting on other data will probably not end well. <br>

In order to accompany the model with some visuals, the histogram distribution can be verified to see that the model is doing a great job of actually fitting the training data. As we know from the lecture videos, this is a Gaussian Mixture Model which uses two gaussians of separation between the data in order to predict probabalistically whether a spike in the data is a heart beat or not. We will borrow ```SciPy```'s ```norm``` modeule in order to plot these gaussians. In analyzing this visual, we can see just by looking at the plot where most no heartbeat events and heartbeat events occur, and even a potential threshold to differentiate between the two. <br>

Finally, we can use everything so far in order to finally estimate heart rates. We do this by taking the labels predicted by the GMM and using the ```np.diff()``` function in order to detect when these labels transition from 0 to 1 which will be indicated by a difference of 1 rather than a negative 1. <br>

In order to better train the model, we will employ a strategy called the Leave-One-Subject-Out-Validation (LOSOV) which as the name suggests revolves around leaving one subject out. The essence behind the method is that every time we train the model, we leave one subject out (PID Number) and then do the testing on this subject. We shall repeat this cycle until every possible subject is left out. This should hopefully make for a more robust model.

# Challenges

## Challenge 1: GMM Performance

### Task Description
Now that we have created an actual machine learning model using a Gaussian Mixture Model, it is now time for us to evaluate its performance. In order to do just that, we must establish evaluation measures which allows us to objectively assess the model and find its failure points. As discussed in the previous lab, we plan to create the correlation plot and the correlation coefficient relative to the models predictions and the ground truths provided in the data. We will also create a Bland-Altman plot in order to get a different visual of the relationship between the predictions and the ground truths. Most importantly, we will evaluate the **Root Mean Square Error** on the ground truths and the predicted values as this will be used as a one-number evaluation of the whole model. <br>
All these evaluation methods give us a bigger picture of how great the model is doing but we wanted to introduce a different evaluation method in order to analyze the model from a data quality perspective. This method is defined by taking the difference between the ground truth and the prediction during the testing phase of the model training. <br>

### Model Evaluation

#### Correlation Plot, Bland-Altman Plot, RMSE
![correlation](./images/correlation_ba_plot.png)
> In this image, we are subplotting the correlation plot to the top and the Bland-Altman plot to the bottom. In the title, one can see the calculated RMSE value. <br>

At a quick glance, it is easy to see from the correlation plot and the correlation coefficient that the model isn't doing the greatest. This comes from the fact that some predictions ended up predicting double the value of the ground truth value. It is still notable, however, that it did do a great job of predicting a lot of the values. This gives us an initial hunch that maybe some data are worse than others. The Bland-Altman plot provides a similar evaluation with a different visual as the data is now plotted relative to the mean value and an upper and lower bound relative to the standard deviation. Similar conclusions can be made with the BA plot but now it is more obvious which points of data actually drive the model down.

#### Per Subject Difference Evaluation
As we study the results of the model as well as the evaluation methods as shown below, it became apparent that there are inherently some data which perform worse than others. Not only does it result in worse readings, but often its readings are magnitudes away from the ground truth. In order to isolate these pieces of data as well as to visualize what is really happening, we came up with a way to see the difference between ground truths and predictions for each each subject that it is tested on. Here are a few examples of plots and our observations for it. 

Good Data #1           |      Good Data #2     |          Good Data #3 
:-------------------------:|:-------------------------:|:-----------:
![A16896384](./images/difference_A16896384.png) | ![A15870301](./images/difference_A15870301.png)| ![A17204443](./images/difference_A17204443.png)

> In these sets of images, one can see that the difference between the predictions made by the model and the ground truth established when the data was created are almost identical, with some even being perfect. These are the data that will be kept as the plots indicate that the data is good.

Bad Data #1           |      Bad Data #2     |          Bad Data #3 
:-------------------------:|:-------------------------:|:-----------:
![A15955623](./images/difference_A15955623.png) | ![A16167148](./images/difference_A16167148.png)| ![A16659711](./images/difference_A16659711.png)

> In these sets of images, it is clear that there are one or more pieces of data which throw the model off and are given predictions that are way more than the ground truth provided by the user. These are the data in which a long line is drawn between the ground truth and the prediction. These data pieces will also be discarded as it can be concluded that these are bad data which throw off the entire model.

Edge Data #1           |      Edge Data #2     |          Edge Data #3 
:-------------------------:|:-------------------------:|:-----------:
![A16136224](./images/difference_A16136224.png) | ![A16674050](./images/difference_A16674050.png)| ![A16821776](./images/difference_A16821776.png)

> In these sets of images, the data is relatively good and not as bad as some of the other ones. It is also important to note the scale of the images. Despite there being a long looking line between two points, it is still important to see the value of the difference as some of these may just be zoomed in. With these pieces of data, there is a noticeable error between the ground truth and the predictions but there comes a point in which we decided how much data to discard. For testing purposes, we decided to cut off data whose difference was greater than or equal to 20 in magnitude. 

#### Results of Discarding Some Data
![newcorrelation](./images/correlation_ba_plot_without_bad_data.png)
It can now be seen that the RMSE has been reduced significantly, and the correlation increased by a great amount. It is also nice to see the Bland Altman plot showing the values much more tight nit. The removal of deemed "bad data" has drastically improved the quality of the model. 


## Challenge 2: GMM HR Monitor

### Task Description
In this challenge, we must incorporate the machine learning model which we have been training into the same logic flow of measuring heart rate as with previous labs. The goal is to finally use the model in order to get predictions and output that as our official reading of the heart rate. <br>

In order to do this, the ```HRMonitor.py``` class must be revised in order to account for the model. The first revision comes from introducing new methods, train() and predict(), which will be used to train the model and make predictions about the heart rate. These functions will have their own helper functions introduced in the previous tutorials which will also be implemented within the class itself. Most of these functions will come with the keyword ```@staticmethod``` because these are methods that will only be used within the class itself. There may be multiple ways to implement them within the class but this was the first one that came to mind. <br>

In order to handle data which are either inadequate or of poor quality, we have implemented a few try-except clauses to keep track of this. Oftentimes, bad data leads to ValueErrors which are thrown and ends the program. This allows us to use these classes to keep track of them and make sure that the program continues even after bad data. The program will send a command of **"-1"** to be displayed on the OLED screen. This was done for the convenience of the challenge but can obviously changed to show something like "bad data". This feature is showcased in the video. <br>

### Improving on the Model
As discussed in the previous challenge, we explored the idea of discarding data whose ground truth difference from the estimate reached a certain number. For the challenge, we decided to reduce that difference down to 10 so any data whose absolute value of the error is greater than or equal to 10 was discarded. This resulted in much smaller RMSE for the model<br>

We also explored the idea of utilizing the processing that we used in the previous lab and incorporate it into this one. This means that the data that we use to fit the GMM goes through the pre-processing that we defined in the previous lab. This is crucial because it is important that the data is trained on is processed the same as the data that it is predicting on. We initially had used the the most basic processing provided in the tutorial but realized that we were processing the data coming in from the MCU entirely differently. This was changed in the final build. <br>

### YouTube Video Links

Here is the video showcasing the program with a slightly elevated heart rate: https://youtu.be/5WKDBYbydfc

Here is a video with a more rested heart rate: https://youtube.com/shorts/ch0Yo5p_ECA?feature=share

## Challenge 3: Complete Wearable

### YouTube Video Link:
v1: https://youtu.be/jCX08KPpZVE <br>
v2: https://youtu.be/UhR2pMChgsc

### Finite State Machine
![heartrate](./images/ECE%2016%20Lab%207%20Challenge%203%20State%20Diagram.jpg)

### Mode Features
Pedometer: <br> 
Works as a step counter. Will keep track of steps according to internal thresholds set by the team in order to only account for relevant walking frequencies. This mode updates the step count on the OLED display.<br>

Heartrate Monitor:<br>
As the name of the mode suggests, it will display the heartrate of the user as soon as they place their finger on the photodetector. If no finger is detected, the heart rate monitor will simply output 0. It is important that the heart rate monitor gets a few seconds to stablize and output the correct heart rate.<br>

Weather Watch: <br>
This mode will divide up the OLED to display time, data, current weather in San Diego, and finally the location, San Diego<br>

Idle Detector:<br>
This mode acts as an idle detector. It will display the message "Great Job" and ON when there is motion detected within the last second (Note that the activity must be at least a second). If the mode detects idleness for 5s, an LED will blink and the a message will display "Idle 5s". After 10 seconds of cumulative idleness, the buzzer will buzz for a second and the OLED will display "Idle 10s". If activity is detected, then the Idle Detector will return to its origianl state and the cycle begins again, however, anytime during the cycle a button can be clicked which restarts the Idle Detector mode. Note that this is a separate buton which moves the watch from mode to mode.  


### Task Descriptions:
The final challenge of the final lab tasks us build a complete weable watch which encompasses all the skills that we have learned throughout the quarter. This includes the pedometer, the heart rate monitor, idle detector, and the weather wathc. For the hardware side of things, all pieces of hardware used in those respective labs make an appearance in this lab. For software, the ever growing ```ECE16Lib``` is being used to access all the classes established over the course of this course.<br>

In order to accomplish this task, let's first take a look at the arduino side of things. The arduino progressively gets a command from Python in the form of comma separated commands which correspond to the different modes and their relevant values. This comma separated commands are then split into sub commands which the MCU is built to interpret in order to do its tasks and understand what kinda data to be sending back to Python. In order to make this slightly easier for the MCU, there is a local variable representing the state so that it is always aware what state it is in. In order to move from state to state, a new button is added into the circuitry. This button moves from mode to mode according to the state diagram. Note that the other button is only used for the Idle Detector as it was intended for in the previous lab.<br>

On the Python side of things, it also receives a comma separated message but this time they are a separated values relevant to each mode such as the acceleration provided by the accelerometer or the PPG values. Python parses through all of this data and uses many of the previously built classes and logic in order to analyze the data and produce something out of it. After processing all the data, Python sends back a message relevant to the mode in order to update the OLED screen. <br>
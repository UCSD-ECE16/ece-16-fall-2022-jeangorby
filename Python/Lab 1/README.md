Jean Gorby Calicdan
A15955623

# Lab #1

# Tutorial Review
## Tutorial 1: Python Install & Setup
Prior to this lab, I had already installed Python from previous classes that I have taken, so there wasn't much to learn for this tutorial. For what its worth, I went through the "Install Python Directly" route.

## Tutorial 2: Python Basics
Given that I have had plenty of experience with Python, this tutorial serves as a really good practice to review and revisit my abilities. Running Python code is always good practice to start out but is something that eventually becomes second nature as it has for me. Using VScode has made it easier as well with good user interface. Python lists are one of the most important elements of Python as it allows for many versatile functions. Operating on these lists creates skills and abilities that are also useful for string processing as strings in Python are essentially just a list of characters. List comprehension is a new operation that I learned in greater detail in this tutorial and is something that I will try to use more often in the future as it allows for convenient one-liners. Looping in Python is a useful complementary technique to learn as it it can be very useful in processing these lists. Similarly, functions are there to complete operations that may be used many times so its functionality is equally important.

## Tutorial 3: NumPy
## Tutorial 1: Numpy
Numpy is one of the most powerful libraries in all of Python especially when it comes to several tasks such as image processing and data analysis in conjunction with other libraries. Since I had already used Numpy before the installation process was not new and therefore not needed. There are several other information, however, which I still found very useful to know and understand. These came in handy when applying the skills within the Testing Your Knowledge section.
### Testing Your Knowledge
1. **Question 1** <br>
    Subtracting 20 from the entire array subtracts 20 from each element in the array <br>
    ```array1 - 20 =  [-20 -10  24  -8]```
2. **Question 2** <br>
    Using methods such as reshape to conver the array from a 2x4 matrix to a 4x2 matrix and using proper slicing combined with vstack, the new array was created.
    ```
    Original Array:
    [[ 0 10  4 12] 
     [ 1 20  3 41]] 
    
    New Array:
     [[ 4 12] 
      [ 1 20]]
    ```
3. **Question 3** <br>
    In order to create this array:  
    ```
    [[ 0 10 44 12  0 10 44 12]
     [ 0 10 44 12  0 10 44 12]
     [ 0 10 44 12  0 10 44 12]
     [ 0 10 44 12  0 10 44 12]]
    ```
    it was necessary to first initiate an array which contained the first 4 elements.
    ```random_list = [0, 10, 44, 12]```<br>
    To utilize this list, it must first be converted into a Numpy array and then with the use of hstack() and vstack(), the desired array was created.
4. **Question 4** <br>
   In order to create the array needed question 4, it is necessary to understand the pattern which each array had. The first array were simply numbers starting from -3 ending at 15 with a increments of 3. The second array were numbers starting from -7 to -19 with increments of -2. The way to make these arrays possible with just one line of code is to use np.arrange() with appropriate parameters from each respective array.
5. **Question 5** <br>
   By using linspace() that goes from 0 to 100 in 49 steps, the following array was created:
   ```
   [  0.        2.08333333   4.16666667   6.25         8.33333333
   10.41666667  12.5         14.58333333  16.66666667  18.75
   20.83333333  22.91666667  25.          27.08333333  29.16666667
   31.25        33.33333333  35.41666667  37.5         39.58333333
   41.66666667  43.75        45.83333333  47.91666667  50.
   52.08333333  54.16666667  56.25        58.33333333  60.41666667
   62.5         64.58333333  66.66666667  68.75        70.83333333
   72.91666667  75.          77.08333333  79.16666667  81.25
   83.33333333  85.41666667  87.5         89.58333333  91.66666667
   93.75        95.83333333  97.91666667 100.        ]
   ```
   This differs from arange() because the only control here is the number of steps between the start point and the endpoint whereas in arange(), the increments between start point and endpoint was the controlled value. arange() is best used for an array of integers while linspace() isn't.
6. **Question 6** <br>
   By drawing out each print statements on my own, I was able to find the necessary array to be created. The array must look like this:
   ```
   # 12 3 1 2
   # 0  0 1 2
   # 4  2 3 1
   ```
   In order to create this array, proper slicing was used to create the first and last row as well as the last two elements within the second row.
7. **Question 7** <br>
   Using the original ```string7 = "1,2,3,4"```, I began by turning this string into a list of numbers using proper list comprehension as can be seen in the code. I then turned this into a NumPy array and then used a for loop and vstack() to create the needed result.

# Challenges

## Challenge 1: Python Worksheet
This worksheet consists of multiple problems which tests the Python techniques that we have learned in the previous tutorials. The first set of problems allows us to work with more lists, particularly lists that involve different data types such as string, int, and floats. The most common approach I used in these problems involve list slicing and and certain methods in order create new lists out of old ones. The next set of problems involve the use of loops in order to fully understand how they can be used in Python. For and while loops are used in similar scenarios at different times but this challenge illustrates how both loops can be so different and similar. Different comparisons are also used in this challenge which all seem very similar but all have the same purpose for instance, keyword ```in``` and ```==``` do completely different things. ```in``` checks if the first string or character exists in the second string while ```==``` checks if the first string is the same as the second string. In the last set of exercises, the try-except clase is put to test. There are many errors that can be thrown when programming with Python and catching these errors are important in order to ensure full understanding of the code's limits and general maintenance. This exercise explores a UnicodeDecodeError and catching it. 

## Challenge 2: Stock Simulator
In this challenge, we create a simulator which buys and sells stocks for us for ultimate stonks. The strategy provided by this challenge essentially takes the average over the last 3 days and compares it to the current stock. If this average is lower, then we sell on that day. If it is higher then we buy on that day, otherwise we don't do anything. We do this by first creating a NumPy array of all the stock prices within a certain time period. <br>
!["ndarray"](images\1.2.1.png)<br>

We then loop through all of the prices and take the average of the last 3 days and comparing it to the current days price as discussed in the current strategy. These comparisons and its results are stored in another NumPy array with the convention of ```1 == buy, 0 == do nothing, -1 == sell```. <br>
!["strategy"](images\1.2.2.png)<br>

At the end of it all, we update the number of shares at the end and compute the overall profit that has come out of using this strategy. <br>
!["shares"](images\1.2.3.png) <br>

Although this strategy has proven to give us profit at the end of the day, there are definitely multiple ways to improve this strategy even more. Within the code, I experimented with waiting for a much longer turn around time for selling the stocks. Instead of comparing it for the last 3 days, I tried to compare it to the last 5 days instead. This has led to more profits as I had expected. <br>
!["NewStrategy"](images\1.2.4.png) <br>

Another strategy which could be explore would be to continue the current strategy of buying on lows by comparing the last 3 days with the current day. This time, we can keep track of the the all time low. We can set a threshold close to this all time low price and that we can only finally sell when we hit this threshold. But instead of selling only one stock, we sell all of our stocks at once. The ultimate HODL strategy.

## Challenge 3: Pig Latin Translator


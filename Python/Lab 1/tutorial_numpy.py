import numpy as np

# 1-Dimensional Arrays
a = np.array([1, 2, 3])

# 2-Dimensional Arrays
a = np.array([(1,2,3),(4,5,6)])

# 3-Dimensional Arrays
a = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

#Converting an arbitrary list to numpy arrays
myList = [1,2,9,8]
a = np.array(myList)

# Initializing without lists
a = np.zeros((2,2))
a = np.ones((3,3))

# Restructuring arrays
a = np.array([(1,2,3),(4,5,6)])
a.reshape(3,2)

a = np.array([(1,2,3),(4,5,6)])
b = a.flatten()
b.shape # (6,) NOT (6,1)!

# Resizing Arrays
a = np.array([1,2,3,4,5,6,7])
b = np.resize(a, (1,4)) # array([[1, 2, 3, 4]])

a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.hstack((a,b)) #horizontally stack

a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.vstack((a,b)) #vertically stack

# Creating Indexing Arrays
a = np.arange(1,11,1)

a = np.linspace(1.0,5.0,10, False) #start at 1.0 and end at 5.0, provide 10 samples, False means dont include end point

# Indexing and Slicing Arrays
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
a[0] # This gives us the first row of a
a[2] # This gives us the third row of a
a[:,1] # this gives us the second column of a
a[2][2] # this gives us the value of a(2,2), which is 9 here

#slices in NumPy act like pointers
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
c = a[1] # This gives us the 2nd row of a ([4,5,6])
c[2] = 0 # This assigns the 3rd element to 0 in c, but ALSO in a!
a        # [[1,2,3],[4,5,0],[7,8,9]] – NOTICE THE ZERO!!!

def question1():
    random_list = [0, 10, 4, 12]
    array1 = np.array(random_list)

    # print("array1 - 20 = ", array1 - 20)
    # print("shape = ", np.shape(array1 - 20))
    # Subtracting 20 from the entire array subtracts 20 from every element in the array

question1()

def question2():
    array2 = np.array([[0, 10, 4, 12], [1, 20, 3, 41]])
    #print(array2)
    temp = array2.reshape(4, 2)
    array2_new = np.vstack((temp[1],temp[2]))
    #print(array2_new)
    
question2()

def question3():
    random_list = [0, 10, 44, 12]
    
    array1 = np.array(random_list)

    array3_row = np.hstack((array1, array1))
    array3 = np.vstack((array3_row,array3_row,array3_row,array3_row))
    #print(array3)

question3()

def question4():
    array4a = np.arange(-3, 16, 6)
    # print(array4a)
    array4b = np.arange(-7, -20, -2)
    # print(array4b)

question4()

def question5():
    array5 = np.linspace(0, 100, 49)
    #print("array5: ", array5)

question5()

def question6():
    array6 = np.zeros((3, 4))
    #print(array6)
    array6[0] = [12, 3,1,2]
    array6[1, 2:] = [1 , 2]
    array6[2] = [4, 2, 3, 1]
    #print(array6)
    
    # print(array6[0])     # [12 3 1 2]
    # print(array6[1, 0])  # 0
    # print(array6[:, 1])  # [3 0 2]
    # print(array6[2, :2]) # [4 2] go to the third row, and print the first 2 elements
    # print(array6[2, 2:]) # [3 1] go to the third row, then print ever element from 2 onward
    # print(array6[:, 2])  # [1 1 3] 
    # print(array6[1, 3])  # 2

question6()
# 12 3 1 2
# 0  0 1 2
# 4  2 3 1

def question7():
    string7 = "1,2,3,4"
    numbers = [float(n) for n in string7.split(',')]

    # print(numbers)

    array7 = np.array(numbers)
    for x in range(99):
        array7 = np.vstack((array7, numbers))

    # print(array7)
    # print(np.shape(array7))

question7()
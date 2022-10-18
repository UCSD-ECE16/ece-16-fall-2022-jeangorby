Jean Gorby Calicdan
A15955623

# Lab #4

# Tutorial Review
## Tutorial 1: Object-Oriented Python

### Testing Your Knowledge

1. **Question 1** <br>
What is the output of the print(scout) statement? Explain it.
- ```print(scout)``` returns ```<__main__.Dog object at 0x00000261A49435E0>```
- This print statement tells us that ```scout``` is an instantiation of the class ```Dog``` as well as its location in memory. 

2. **Question 2** <br>
What would happen if we were to change the second print statement to print out the breed with print(scout.__breed)? Explain this result. What does this mean in terms of the Dog class and Object-Oriented Programming?
- If ```print(scout.__breed)```  were to be added, the program will throw an ```AttributeError``` telling us that ```AttributeError: 'Dog' object has no attribute '__breed'```
- The reason this error is thrown is because the ```__breed``` attribute is purposely encapsulated by the programmer. Encapsulation is a way for programmers to hide certain attributes within classes, for instance the ```Dog``` class, for several different purposes. 

3. **Question 3** <br>
At the end of the Python file, add a second Dog object named **skippy** and make **scout** and **skippy** buddies. Then use **scout** to print out **skippy’s** description.
```
skippy = Dog("Skippy", 3, "Poodle")
scout.define_buddy(skippy)
scout.buddy.description()

// prints: Skippy is a 3 year old Poodle
```

## Tutorial 2: Python Plotting


## Tutorial 3: Live Plotting


# Challenges

## Challenge 1: Sensing the Sensor


## Challenge 2: Idle Detector


## Challenge 3: OOP Idle Detector


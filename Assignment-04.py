"""
###Assignment Questions###
##Topic 1: Functions and Modules
Question 1: Simple Function with Parameters
Write a function named calculate_area that takes the length and width of a rectangle as parameters and returns its area.
Call the function with length = 5 and width = 4, and print the result.

##Question 2: Greeting Function with Default Parameter
Write a function named greet that takes a name and an optional parameter greeting (default value should be "Hello").
If no greeting is passed, it should print "Hello, [Name]!". If a greeting is passed, it should use that instead.

##Question 3: Using Built-in Module
Import Python's built-in math module.
Use math.sqrt() to calculate the square root of 25 and math.pow() to calculate 2 raised to the power 3 (2^3).
Print both results clearly.


###Topic 2: File Handling and OOP Basics

##Question 4: File Handling (Write and Read)
Write a Python script that:
Creates and opens a text file named sample.txt in write mode ("w").
Write the sentence "Welcome to Python Programming!" inside it and closes the file.
Then, opens the same file in read mode ("r"), reads the content, and prints it on the screen.

##Question 5: OOP Basics (Class and Object)
Create a class named Student with:
An init method that accepts name and marks.
A method named display_info() that prints the student's name and marks.
Create an object (instance) of the Student class with name "Ayesha" and marks 92, then call display_info().
"""

           ###Answer###
#Topic 1: Functions and Modules
def calculate_area(length, width):
  area = length * width
  print("Area of rectangle: ", area)
calculate_area(5,4) #Area of rectangle:  20


#Question 2: Greeting Function with Default Parameter
def greet(name, gretting = "Hello"): #default assign = Hello
  print(f"{gretting}, {name}")
greet("Shehab") #Hello, Shehab
greet("Shehab","Welcome") #Welcome, Shehab


#Question 3: Using Built-in Module
import math
x = 25
square_root = math.sqrt(x)
print("The square root of 25 is:", square_root) #The square root of 25 is: 5.0

y=2
z=3
pow = math.pow(y,z)
print("2 to the power of 3 (2^3) is:", pow) #2 to the power of 3 (2^3) is: 8.0


##Topic 2: File Handling and OOP Basics

#Question 4: File Handling (Write and Read)

#create file here by using Write(w)
file = open("/content/drive/MyDrive/Ostad/sample.txt", "w")
file.write("Welcome to Python Programming!")
file.close()

#read here using(r)
file = open("/content/drive/MyDrive/Ostad/sample.txt", "r")
content = file.read()
file.close()
print(content) #Welcome to Python Programming!


#Question 5: OOP Basics (Class and Object)
class Student:
    def __init__(self, name, marks): #attributes initialize here
        self.name = name
        self.marks = marks

    def display_info(self): #will print student info
        print(f"Student Name:{self.name}")
        print(f"Marks:{self.marks}")

student1 = Student("Ayesha", 92) #Create an object
student1.display_info() #call display_info().
#Student Name:Ayesha
#Marks:92




          ##End of this assignment##
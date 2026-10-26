# Question 1: Variable Assignment and String Manipulation

# TODO: Ask the user for their name and store it in a variable
name = input("what is your name: ")
# TODO: Ask the user for their age and store it in a variable
age = int(input("What is your age"))
# TODO: Print a greeting using the name and age variables
print(name + " is " + str(age))
#------------------------------------------------------------------------------------
# Question 2: Integer Operations

# TODO: Ask the user for the length of a rectangle and store it as an integer
length = int(input("What is the length"))
# TODO: Ask the user for the width of a rectangle and store it as an integer
width = int(input("what is the width"))
# TODO: Calculate the area of the rectangle
area = length*width               
# TODO: Print the result
print(area)
#------------------------------------------------------------------------------------
# Question 3: Working with Floats

# TODO: Ask the user for a temperature in Celsius and store it as a float
temp = float(input("What is the temerature"))
# TODO: Convert the temperature to Fahrenheit using the formula: (C * 9/5) + 32
fahren = (temp*9/5) + 32
# TODO: Print the result rounded to two decimal places
print("The tempereture is " + str(round(fahren,2)))
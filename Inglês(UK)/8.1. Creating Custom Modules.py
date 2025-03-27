# 8.1. Creating Custom Modules

# In addition to using Python's standard modules, we can also create our own modules to organize and reuse our code.

# Creating and using custom modules
# To create a custom module, simply create a new Python file with the desired name and define the functions, classes, and variables we want to include in the module. For example, we create a file (in the same directory where we are running Python) called my_module.py with the following content:

# my_module.py
def greet(name):
    print(f"Hello, {name}!")

def calculate_sum(a, b):
    return a + b
# Then, we can import and use the functions defined in my_module.py in another Python file.

import my_module

my_module.greet("John")  # Prints "Hello, John!"
result = my_module.calculate_sum(5, 3)
print(result)  # Prints 8
# In this example, the my_module module is imported, and the functions greet() and calculate_sum() defined in it are used.

# Organizing code into modules
# As our programs grow in size and complexity, it is good practice to organize our code into separate modules according to their functionality. This allows us to maintain more readable, grouped, and maintainable code.

# For example, we can have a module operations.py that contains functions related to mathematical operations, and another module utilities.py that contains general-purpose functions.

# operations.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# utilities.py
def print_message(message):
    print(message)

def get_user_name():
    return input("Enter your name: ")
# Then, we can import and use these functions in our main program.

import operations
import utilities

result = operations.add(5, 3)
utilities.print_message(f"The result of the sum is: {result}")

name = utilities.get_user_name()
utilities.print_message(f"Hello, {name}!")
# By organizing our code into modules, we can reuse functions and maintain more structured and grouped code.
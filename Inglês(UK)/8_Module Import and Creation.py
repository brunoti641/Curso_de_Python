# 8. Module Import and Creation

# In Python, a module is a file that contains definitions of functions, classes, and variables that can be used in other programs. Importing modules allows us to access functionality defined in other files and reuse code efficiently. Additionally, we can create our own modules to organize and modularize our code.

# Keep in mind
# Python comes with a wide standard library of modules that provide additional functionality. These modules are available without the need to install them separately.

# Importing modules
# To use a module in our program, we must import it using the import statement. We can import an entire module or specific functions from a module.

import math

result = math.sqrt(25)
print(result)  # Prints 5.0
# In this example, the math module is imported using the import statement. Then, the sqrt() function from the math module is used to calculate the square root of 25.

# We can also import specific functions from a module using the syntax from module import function.

from math import sqrt

result = sqrt(25)
print(result)  # Prints 5.0
# In this case, only the sqrt() function from the math module is imported, allowing us to use it directly without prefixing it with the module name.

# Functions and classes from standard modules
# Python's standard library offers a wide range of modules with useful functions and classes. Some common examples include:

import random
import datetime

random_number = random.randint(1, 10)
print(random_number)  # Prints a random integer between 1 and 10

current_date = datetime.datetime.now()
print(current_date)  # Prints the current date and time
# These are just a few examples of the many modules available in Python's standard library. You can consult the official Python documentation for more information on the modules and their functionalities.
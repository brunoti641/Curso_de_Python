# 5. Functions
# Functions are reusable blocks of code that allow us to encapsulate specific tasks and execute them when needed. Functions help us organize our code, avoid repetition, and make our programs more modular and easier to maintain.

# Definition and calling of functions
# To define a function in Python, we use the def keyword followed by the function name and parentheses. Optionally, we can specify parameters inside the parentheses. The function's code block is indented after the colon.

# To call a function, simply write the function name followed by parentheses:

def greeting():
    print("Hello, world!")

greeting()  # Prints "Hello, world!"

# Parameters and arguments
# Functions can accept parameters, which are values passed to the function when it is called. Parameters are specified inside the parentheses in the function definition.

def greeting(name):
    print(f"Hello, {name}!")
# When calling the function, we provide the arguments corresponding to the parameters:

greeting("John")  # Prints "Hello, John!"
greeting("Mary")  # Prints "Hello, Mary!"

# Return values
# Functions can return values using the return keyword. The return value can be used by the code that calls the function.

def add(a, b):
    return a + b

result = add(3, 4)
print(result)  # Prints 7

# Anonymous functions (lambda)
# Python allows creating anonymous functions or lambda functions, which are nameless functions defined in a single line. They are commonly used for small and concise functions.

square = lambda x: x ** 2
print(square(5))  # Prints 25

# Variable scope (local vs. global)
# Variables defined inside a function have a local scope, meaning they are only accessible within the function. On the other hand, variables defined outside any function have a global scope and can be accessed from anywhere in the program.

def function():
    local_variable = 10
    print(local_variable)  # Accessible inside the function

global_variable = 20

def function2():
    print(global_variable)  # Accessible from anywhere

function()  # Prints 10
function2()  # Prints 20
print(global_variable)  # Prints 20
print(local_variable)  # Raises an error, the variable is not defined in this scope.

# User-defined functions

# Function documentation (docstrings)
# It is good practice to document our functions using docstrings. Docstrings are text strings that describe the purpose, parameters, and return value of a function. They are placed immediately after the function definition and enclosed in triple double quotes.

def rectangle_area(base, height):
    """
    Calculates the area of a rectangle.

    Args:
        base (float): The base of the rectangle.
        height (float): The height of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return base * height

# Functions with a variable number of arguments
# Python allows defining functions that accept a variable number of arguments. This is done using the * operator before the parameter name.

def variable_sum(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(variable_sum(1, 2, 3))  # Prints 6
print(variable_sum(4, 5, 6, 7))  # Prints 22
# Functions are a fundamental tool in programming and allow us to structure and modularize our code. With the ability to define custom functions, we can encapsulate specific tasks and reuse them in different parts of our program.

# In addition to user-defined functions, Python also provides a wide range of built-in functions that we can use directly, such as print(), len(), range(), among others.
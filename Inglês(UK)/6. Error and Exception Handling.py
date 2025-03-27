# 6. Error and Exception Handling
# When writing programs, it is common to encounter unexpected situations or errors during execution. Python provides a mechanism to handle these errors in a controlled manner using exception handling. This allows us to catch and handle specific errors without the program stopping abruptly.

# Common errors in Python
# Before diving into exception handling, let's look at some common errors you might encounter in Python.

# Occurs when the code does not follow Python's syntax rules, such as forgetting a colon after a function declaration or a loop.

def my_function() # Missing colon
    print("Hello")
    
# Occurs when referencing a variable or function that has not been defined.

print(undefined_variable)

# Occurs when performing an operation with incompatible data types, such as trying to add a number and a string.
result = 5 + "10"

# Occurs when trying to access an index outside the valid range of a list or sequence.

my_list = [1, 2, 3]
print(my_list[3])  # Index 3 is out of range

# These are just a few examples of common errors. When an error occurs, Python raises an exception and displays an error message that includes the type of exception and a description of the problem.
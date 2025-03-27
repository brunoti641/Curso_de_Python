# 8.2. Packages

# A package is a way of organizing related modules into a hierarchical directory structure. Packages allow us to group related modules and avoid name conflicts between modules.

# Creating and using packages
# To create a package, we create a directory with the desired name and add a special file called __init__.py inside the directory. This file can be empty or contain package initialization code.

# For example, we create a directory called my_package with the following structure:

my_package/
    __init__.py
    module1.py
    module2.py
# Then, we can import and use the modules from the package in our program.

from my_package import module1, module2

module1.function1()
module2.function2()
# In this example, the modules module1 and module2 are imported from the my_package package, and the functions defined in them are used.

# Importing and creating modules and packages in Python allows us to organize and reuse our code efficiently. By modularizing our code, we can maintain more readable, structured, and maintainable code.

# Remember to explore Python's standard library and take advantage of existing modules, which can simplify many common tasks. Also, don't hesitate to create your own modules and packages to organize and reuse your code effectively.
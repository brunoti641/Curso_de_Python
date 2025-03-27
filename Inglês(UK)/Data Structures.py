# Data structures allow us to organize and store data efficiently in our programs. Python provides several built-in data structures, such as lists, tuples, dictionaries, and sets, each with its own characteristics and uses.

# Lists
# A list is a mutable and ordered data structure that allows storing a collection of elements. The elements of a list can be of different data types and are enclosed in square brackets [], separated by commas.

# Creation and access
# To create a list, simply enclose the elements in square brackets:

fruits = ["apple", "banana", "orange"]
# To access the elements of a list, use the index of the element in square brackets. Indices start from 0.

print(fruits[0])  # Prints "apple"
print(fruits[1])  # Prints "banana"
print(fruits[2])  # Prints "orange"

# You can also access elements from the end of the list using negative indices. The index -1 represents the last element, -2 the second last, and so on.

print(fruits[-1])  # Prints "orange"
print(fruits[-2])  # Prints "banana"
print(fruits[-3])  # Prints "apple"

# List methods
# Lists in Python have several built-in methods that allow us to manipulate and modify the elements of the list. Some common methods are:

# append(element): adds an element to the end of the list.
# insert(index, element): inserts an element at a specific position in the list.
# remove(element): removes the first occurrence of an element in the list.
# pop(index): removes and returns the element at a specific position in the list.
# sort(): sorts the elements of the list in ascending order.
# reverse(): reverses the order of the elements in the list.
# Example:

fruits = ["apple", "banana", "orange"]

fruits.append("pear")
print(fruits)  # Prints ["apple", "banana", "orange", "pear"]

fruits.insert(1, "grape")
print(fruits)  # Prints ["apple", "grape", "banana", "orange", "pear"]

fruits.remove("banana")
print(fruits)  # Prints ["apple", "grape", "orange", "pear"]

removed_fruit = fruits.pop(2)
print(fruits)  # Prints ["apple", "grape", "pear"]
print(removed_fruit)  # Prints "orange"

fruits.sort()
print(fruits)  # Prints ["apple", "grape", "pear"]

fruits.reverse()
print(fruits)  # Prints ["pear", "grape", "apple"]

# List comprehensions
# List comprehensions are a concise way to create new lists based on an existing sequence. They allow filtering and transforming the elements of a list in a single line of code.

# new_list = [expression for element in sequence if condition]
# Example:

numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers if x % 2 == 0]
print(squares)  # Prints [4, 16]

# In this example, a new list called squares is created, which contains the squares of the even numbers from the numbers list. The expression x ** 2 squares each element, and the condition if x % 2 == 0 filters only the even numbers.
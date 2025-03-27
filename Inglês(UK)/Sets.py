# A set is a mutable and unordered data structure that allows storing a collection of unique elements. Sets are enclosed in curly braces {} or created using the set() function.

# Creation and basic operations
# To create a set, use curly braces or the set() function:

fruits = {"apple", "banana", "orange"}
numbers = set([1, 2, 3, 4, 5])
# Sets support mathematical set operations such as union (|), intersection (&), difference (-), and symmetric difference (^).

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union = set1 | set2
print(union)  # Prints {1, 2, 3, 4, 5}

intersection = set1 & set2
print(intersection)  # Prints {3}

difference = set1 - set2
print(difference)  # Prints {1, 2}

symmetric_difference = set1 ^ set2
print(symmetric_difference)  # Prints {1, 2, 4, 5}

# Set methods
# Sets in Python have several built-in methods for manipulating and accessing elements. Some common methods are:

# add(element): adds an element to the set.
# remove(element): removes an element from the set. If the element does not exist, it raises an error.
# discard(element): removes an element from the set if it is present. If the element does not exist, it does nothing.
# clear(): removes all elements from the set.
# Example:

fruits = {"apple", "banana", "orange"}

fruits.add("pear")
print(fruits)  # Prints {"apple", "banana", "orange", "pear"}

fruits.remove("banana")
print(fruits)  # Prints {"apple", "orange", "pear"}

fruits.discard("grape")
print(fruits)  # Prints {"apple", "orange", "pear"}

fruits.clear()
print(fruits)  # Prints set()

# Data structures in Python offer great flexibility and power for storing and manipulating data in our programs. Lists are useful for ordered and mutable collections, tuples for ordered and immutable collections, dictionaries for storing key-value pairs, and sets for unordered collections of unique elements.
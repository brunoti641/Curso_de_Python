# 4.2. Dictionaries
# A dictionary is a mutable and unordered data structure that allows storing key-value pairs. Each element in a dictionary consists of a unique key and its corresponding value. Dictionaries are enclosed in curly braces {}, and key-value pairs are separated by commas.

# Creation and access
# To create a dictionary, use curly braces and separate keys and values with colons.

person = {"name": "John", "age": 25, "city": "Madrid"}

# To access the values of a dictionary, use the corresponding key in square brackets:

print(person["name"])  # Prints "John"
print(person["age"])    # Prints 25
print(person["city"])  # Prints "Madrid"
# You can also use the get() method to get the value of a key. If the key does not exist, it returns a default value (by default, None).

# Dictionary methods
# Dictionaries in Python have several built-in methods for manipulating and accessing elements. Some common methods are:

# keys(): returns a view of all the keys in the dictionary.
# values(): returns a view of all the values in the dictionary.
# items(): returns a view of all the key-value pairs in the dictionary.
# update(other_dictionary): updates the dictionary with the key-value pairs from another dictionary.
# Example:

person = {"name": "John", "age": 25, "city": "Madrid"}

print(person.keys())    # Prints dict_keys(["name", "age", "city"])
print(person.values())  # Prints dict_values(["John", 25, "Madrid"])
print(person.items())   # Prints dict_items([("name", "John"), ("age", 25), ("city", "Madrid")])

person.update({"profession": "Engineer"})
print(person)  # Prints {"name": "John", "age": 25, "city": "Madrid", "profession": "Engineer"}
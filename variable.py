# lesson by the Apsan 
# data type in the python 

# Numeric Types
# In Python, there are several numeric types: int, float, and complex.
 #eg:
x = 10        # int
y = 3.14      # float
z = 1 + 2j    # complex


# String Type
# Strings in Python are sequences of characters enclosed in single or double quotes.    
# eg:
name = "John Doe"
greeting = 'Hello, World!'

# Boolean Type
# The boolean type in Python has two values: True and False.    
# eg:
is_active = True    
is_admin = False
# List Type
# Lists are ordered collections of items that can be of different types.        
# eg:
fruits = ["apple", "banana", "cherry"]  
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "two", 3.0, True]
# Tuple Type
# Tuples are similar to lists but are immutable (cannot be changed after creation). 
# eg:
point = (10, 20)    
coordinates = (1.0, 2.0, 3.0)
# Dictionary Type
# Dictionaries are unordered collections of key-value pairs.
# eg:
person = {"name": "Alice", "age": 30, "is_student": False}
settings = {"theme": "dark", "notifications": True}
# Set Type
# Sets are unordered collections of unique items.
# eg:
fruits_set = {"apple", "banana", "cherry"}
numbers_set = {1, 2, 3, 4, 5}
# None Type     
# The None type represents the absence of a value or a null value.
# eg:       
result = None
data = None
# You can check the type of a variable using the type() function:
print(type(x))          # <class 'int'> 
print(type(name))       # <class 'str'>
print(type(is_active))  # <class 'bool'>    
print(type(fruits))     # <class 'list'>
print(type(point))      # <class 'tuple'>

print(type(person))     # <class 'dict'>
print(type(fruits_set)) # <class 'set'> 
print(type(result))     # <class 'NoneType'>
# Python is a dynamically typed language, so you don't need to declare the type of a variable explicitly. The interpreter infers the type based on the assigned value.

# lesson by the Apsan
# types of function in python
# 1. Built-in Functions
# Python provides a variety of built-in functions that are always available for use. Some common built-in functions include:
# eg:   
print("Hello, World!")  # Prints a message to the console
length = len("Hello")    # Returns the length of a string           
print(length)            # Output: 5
absolute_value = abs(-10) # Returns the absolute value of a number  
print(absolute_value)    # Output: 10   
maximum = max(1, 2, 3)   # Returns the maximum value among the arguments
print(maximum)          # Output: 3 
minimum = min(1, 2, 3)   # Returns the minimum value among the arguments
print(minimum)          # Output: 1 
rounded_value = round(3.14159, 2) # Rounds a number to a specified number of decimal places
print(rounded_value)     # Output: 3.14
# 2. User-Defined Functions
# You can create your own functions using the def keyword. User-defined functions allow you to encapsulate reusable code blocks.
# eg:   
def greet(name):
    return f"Hello, {name}!"    
message = greet("Alice")
print(message)           # Output: Hello, Alice!
def add(a, b):
    return a + b    
result = add(5, 3)
print(result)           # Output: 8 
def factorial(n):
    if n == 0 or n == 1: # == looks for equality
        return 1
    else:
        return n * factorial(n - 1)    
print(factorial(5))     # Output: 120
# 3. Lambda Functions   
# Lambda functions are small anonymous functions defined using the lambda keyword. They can take any number of arguments but can only have a single expression.
# eg:
square = lambda x: x ** 2 # ** is the exponentiation operator meaning x raised to the power of 2
print(square(5))        # Output: 25 
add = lambda a, b: a + b
print(add(3, 4))       # Output: 7
multiply = lambda a, b: a * b
print(multiply(3, 4))  # Output: 12
# You can use lambda functions in higher-order functions like map(), filter(), and reduce().
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)   # Output: [1, 4, 9, 16, 25]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) # % is the modulus operator that returns the remainder of a division operation lets say the even  numbers are divided by 2 the remainder will be 0
print(even_numbers)      # Output: [2, 4]
# In summary, Python provides built-in functions for common tasks, allows you to define your own
# functions, and supports lambda functions for creating small, anonymous functions. It is mainly used for short-term use. The map() function is part of the functional programming design pattern, and the filter() function is used to filter out elements from a list based on a condition provided in the lambda function.
# functions that can be reused throughout your code.
# Python functions can return values using the return statement. If no return statement is provided, the function returns None by default.
# You can also define functions with default parameter values, variable-length arguments, and keyword arguments for more flexibility.
# Functions can also be nested, meaning you can define a function inside another function.
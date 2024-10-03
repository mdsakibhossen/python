# Part 1: Normal Functions

# 1. Defining a Function
print("1. Defining a Function")


# Example 1: Simple greeting function
def greet(name):
    return f"Hello, {name}!"


result = greet("Alice")
print(result)  # Output: Hello, Alice!
print()  # Blank line for spacing

# 2. Calling a Function
print("2. Calling a Function")

# Example 2: Calling the greet function
print(greet("Bob"))  # Output: Hello, Bob!
print(greet("Charlie"))  # Output: Hello, Charlie!
print()  # Blank line for spacing

# 3. Function Parameters
print("3. Function Parameters")


# Example 3: Function with multiple parameters
def add_numbers(a, b):
    return a + b


result = add_numbers(5, 3)
print(result)  # Output: 8
print()  # Blank line for spacing

# 4. Return Statement
print("4. Return Statement")


# Example 4: Function that returns a value
def multiply(a, b):
    return a * b


result = multiply(4, 5)
print(result)  # Output: 20
print()  # Blank line for spacing

# 5. Default Parameters
print("5. Default Parameters")


# Example 5: Function with default parameter
def greet(name="Guest"):
    return f"Hello, {name}!"


result1 = greet()
result2 = greet("Boss")
print(result1)  # Output: Hello, Guest!
print(result2)  # Output: Hello, Boss!
print()  # Blank line for spacing

# 6. Variable-Length Arguments
print("6. Variable-Length Arguments")


# Example 6: Function with variable-length arguments
def calculate_total(*args):
    return sum(args)


result = calculate_total(10, 20, 30)
print(result)  # Output: 60
print()  # Blank line for spacing

# 7. Scope of Variables
print("7. Scope of Variables")


# Example 7: Function demonstrating variable scope
def outer_function():
    outer_var = "I'm outside!"

    def inner_function():
        inner_var = "I'm inside!"
        return inner_var

    print(inner_function())  # Output: I'm inside!
    return outer_var


result = outer_function()
print(result)  # Output: I'm outside!
print()  # Blank line for spacing

# 8. Nested Functions
print("8. Nested Functions")


# Example 8: Function with nested functions
def outer_function(x):
    def inner_function(y):
        print(f"x: {x}, y: {y}")
        return x + y

    return inner_function


add_five = outer_function(5)
result = add_five(10)
print(result)  # Output: 15
print()  # Blank line for spacing


# Part 2: Lambda Functions

# 9. Anonymous (Lambda) Functions
print("9. Anonymous (Lambda) Functions")

# 1. Simple lambda function
print("1. Simple lambda function")
add = lambda x, y: x + y
result = add(5, 3)
print(result)  # Output: 8
print()  # Blank line for spacing

# 2. Lambda function for squaring a number
print("2. Lambda function for squaring a number")
square = lambda x: x**2
result = square(4)
print(result)  # Output: 16
print()  # Blank line for spacing

# 3. Lambda function to check if a number is even
print("3. Lambda function to check if a number is even")
is_even = lambda x: x % 2 == 0
result = is_even(10)
print(result)  # Output: True
print()  # Blank line for spacing

# 4. Lambda function to concatenate two strings
print("4. Lambda function to concatenate two strings")
concat = lambda a, b: a + b
result = concat("Hello, ", "world!")
print(result)  # Output: Hello, world!
print()  # Blank line for spacing

# 5. Lambda function for maximum of two numbers
print("5. Lambda function for maximum of two numbers")
maximum = lambda x, y: x if x > y else y
result = maximum(10, 20)
print(result)  # Output: 20
print()  # Blank line for spacing

# 6. Lambda with map()
print("6. Lambda with map()")
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
print()  # Blank line for spacing

# 7. Using Lambda with filter()
print("7. Using Lambda with filter()")
# Example: Filter out even numbers from a list
numbers = [1, 2, 3, 4, 5]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)  # Output: [1, 3, 5]
print()  # Blank line for spacing

# 8. Using Lambda with sorted()
print("8. Using Lambda with sorted()")
# Example: Sort a list of tuples based on the second element
data = [(1, "one"), (3, "three"), (2, "two")]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)  # Output: [(1, 'one'), (3, 'three'), (2, 'two')]
print()  # Blank line for spacing

# 9. Using Lambda with reduce()
print("9. Using Lambda with reduce()")
from functools import reduce

# Example: Calculate the product of all numbers in a list
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24
print()  # Blank line for spacing

# 10. Using Lambda with list comprehension
print("10. Using Lambda with list comprehension")
# Example: Create a list of cubes using a lambda function in a list comprehension
numbers = [1, 2, 3, 4]
cubes = [(lambda x: x**3)(x) for x in numbers]
print(cubes)  # Output: [1, 8, 27, 64]
print()  # Blank line for spacing

# Functions in Python

Functions are reusable blocks of code that perform a specific task. They help organize code, promote reusability, and make programs easier to read and maintain.

---

## 1. Defining a Function

You define a function using the `def` keyword followed by the function name and parentheses.

### Syntax:

```python
def function_name(parameters):
    # Block of code
    return result
```

## 2. Calling a Function

To execute a function, you call it by its name followed by parentheses.

### Example:

```python
def greet():
    print("Hello, World!")

greet()  # Output: Hello, World!
```

## 3. Function Parameters

Functions can accept parameters, allowing you to pass values to them. These parameters act as placeholders for the values you provide.

### Example:

```python
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)  # Output: 8
print(result)
```

## 4. Return Statement

The `return` statement is used to exit a function and send a value back to the caller. If no value is specified, the function returns `None`.

### Example:

```python
def multiply_numbers(a, b):
    return a * b

result = multiply_numbers(4, 5)  # Output: 20
print(result)
```

## 5. Default Parameters

Default parameters allow you to define a function with default values for one or more parameters. If no argument is provided for those parameters when the function is called, the default values are used.

### Example:

```python
def greet(name="Guest"):
    return f"Hello, {name}!"

# Calling the function without an argument
print(greet())          # Output: Hello, Guest!

# Calling the function with an argument
print(greet("Alice"))  # Output: Hello, Alice!
```

## 6. Variable-Length Arguments

In Python, you can define functions that accept a variable number of arguments. This is useful when you are unsure how many arguments will be passed to your function. There are two ways to handle variable-length arguments: using `*args` and `**kwargs`.

### Using `*args`

The `*args` parameter allows you to pass a variable number of non-keyword arguments to a function.

#### Example:

```python
def add_numbers(*args):
    return sum(args)

# Calling the function with multiple arguments
print(add_numbers(1, 2, 3))         # Output: 6
print(add_numbers(5, 10, 15, 20))   # Output: 50
```

## 8. Nested Functions

Nested functions are functions defined within other functions. The inner function can access variables from the outer function's scope, which can be useful for creating closures and encapsulating functionality.

### Defining a Nested Function

You can define a function inside another function just like any other function. The inner function can be called only within the outer function.

#### Example:

```python
def outer_function():
    def inner_function():
        print("This is the inner function.")

    print("This is the outer function.")
    inner_function()  # Calling the inner function

outer_function()
# Output:
# This is the outer function.
# This is the inner function.
```

## 9. Anonymous (Lambda) Functions

### Lambda Functions

Lambda functions are small, anonymous functions defined using the `lambda` keyword. They can take any number of arguments but can only have one expression. Lambda functions are often used for short, throwaway functions where a full function definition would be too verbose.

#### Syntax:

```python
lambda arguments: expression
```

## Example: Basic Lambda Function

```python
# A simple lambda function that adds two numbers
add = lambda x, y: x + y
result = add(5, 3)
print(result)  # Output: 8
```

## Using Lambda Functions

Lambda functions can be used with several built-in functions such as `map`, `filter`, `sorted`, and `reduce`.

### 1. Using `map()`

The `map()` function applies a specified function to every item in an iterable (e.g., list) and returns a map object (which is an iterator). You can use a lambda function as the specified function.

#### Example:

```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))  # Squaring each number
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
```

### 2. Using `filter()`

The `filter()` function creates a list of elements for which a function returns true. You can use a lambda function to define the filtering condition.

#### Example:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # Filtering even numbers
print(even_numbers)  # Output: [2, 4, 6, 8, 10]
```

### 3. Using `sorted()`

The `sorted()` function returns a new sorted list from the elements of any iterable. You can use a lambda function to define custom sorting criteria.

#### Example:

```python
# List of tuples (name, age)
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]

# Sort by age using a lambda function
sorted_people = sorted(people, key=lambda x: x[1])  # Sorting by the second element (age)
print(sorted_people)  # Output: [('Bob', 25), ('Alice', 30), ('Charlie', 35)]
```

### 4. Using `reduce()`

The `reduce()` function from the `functools` module reduces a list of elements to a single value by applying a specified function cumulatively. Lambda functions can be used for the reduction operation.

#### Example:

```python
from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Reduce to find the product of all numbers using a lambda function
product = reduce(lambda x, y: x * y, numbers)  # Applying multiplication cumulatively
print(product)  # Output: 120
```

### Conclusion

Functions are essential in Python for code organization and reuse. Understanding how to define and use them effectively will greatly enhance your programming skills.

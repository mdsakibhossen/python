# Using 'is' Operator
print("1. Using 'is' Operator")

# Example 1: Check if two variables point to the same object
a = [1, 2, 3]
b = a
if a is b:
    print("a and b point to the same object.")  # This will be printed
else:
    print("a and b do not point to the same object.")

print()  # Blank line for spacing

# Using 'in' Operator
print("2. Using 'in' Operator")

# Example 2: Check if a value exists in a list
my_list = [1, 2, 3, 4]
if 3 in my_list:
    print("3 is in the list.")  # This will be printed
else:
    print("3 is not in the list.")

print()  # Blank line for spacing

# Using 'not in' Operator
print("3. Using 'not in' Operator")

# Example 3: Check if a value does not exist in a string
my_string = "Hello, World!"
if "Python" not in my_string:
    print("Python is not in the string.")  # This will be printed
else:
    print("Python is in the string.")

print()  # Blank line for spacing

# Using '==' Operator
print("4. Using '==' Operator")

# Example 4: Check for equality
x = 5
if x == 5:
    print("x is equal to 5.")  # This will be printed
else:
    print("x is not equal to 5.")

print()  # Blank line for spacing

# Using '!=' Operator
print("5. Using '!=' Operator")

# Example 5: Check if two values are not equal
y = 10
if y != 5:
    print("y is not equal to 5.")  # This will be printed
else:
    print("y is equal to 5.")

print()  # Blank line for spacing

# Using Comparison Operators
print("6. Using Comparison Operators")

# Example 6: Check if age is eligible to vote
age = 18
if age >= 18:
    print("You are eligible to vote.")  # This will be printed
else:
    print("You are not eligible to vote.")

print()  # Blank line for spacing

# Combining Conditions with Logical Operators
print("7. Combining Conditions with Logical Operators")

# Example 7: Check multiple conditions
age = 20
if age >= 18 and age < 65:
    # This will be printed
    print("You are an adult and not a senior citizen.")
else:
    print("You are either a minor or a senior citizen.")

print()  # Blank line for spacing

# Nested if Statements
print("8. Nested if Statements")

# Example 8: Using nested if statements
x = 10
if x > 5:
    print("x is greater than 5.")  # This will be printed
    if x < 15:
        print("x is also less than 15.")  # This will be printed
else:
    print("x is not greater than 5.")

print()  # Blank line for spacing

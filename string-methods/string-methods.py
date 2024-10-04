# Using 'upper' Method
print("Using 'upper' Method:")

# Example 1: Convert a string to uppercase
my_string = "hello, world!"
print("1.", my_string.upper())  # This will print: HELLO, WORLD!

print()  # Blank line for spacing

# Using 'lower' Method
print("Using 'lower' Method:")

# Example 2: Convert a string to lowercase
my_string = "HELLO, WORLD!"
print("2.", my_string.lower())  # This will print: hello, world!

print()  # Blank line for spacing

# Using 'title' Method
print("Using 'title' Method:")

# Example 3: Convert a string to title case
my_string = "hello, world!"
print("3.", my_string.title())  # This will print: Hello, World!

print()  # Blank line for spacing

# Using 'strip' Method
print("Using 'strip' Method:")

# Example 4: Remove leading and trailing whitespace
my_string = "   Hello, World!   "
print("4.", my_string.strip())  # This will print: Hello, World!

print()  # Blank line for spacing

# Using 'replace' Method
print("Using 'replace' Method:")

# Example 5: Replace a substring with another substring
my_string = "Hello, World!"
print("5.", my_string.replace("World", "Python"))  # This will print: Hello, Python!

print()  # Blank line for spacing

# Using 'find' Method
print("Using 'find' Method:")

# Example 6: Find the index of a substring
my_string = "Hello, World!"
index = my_string.find("World")
print("6. 'World' found at index:", index)  # This will print: 7

print()  # Blank line for spacing

# Using 'startswith' Method
print("Using 'startswith' Method:")

# Example 7: Check if a string starts with a specified prefix
my_string = "Hello, World!"
if my_string.startswith("Hello"):
    print("7. The string starts with 'Hello'.")  # This will be printed

print()  # Blank line for spacing

# Using 'endswith' Method
print("Using 'endswith' Method:")

# Example 8: Check if a string ends with a specified suffix
my_string = "Hello, World!"
if my_string.endswith("!"):
    print("8. The string ends with '!'")  # This will be printed

print()  # Blank line for spacing

# Using 'split' Method
print("Using 'split' Method:")

# Example 9: Split a string into a list of substrings
my_string = "Hello, World!"
print("9.", my_string.split(", "))  # This will print: ['Hello', 'World!']

print()  # Blank line for spacing

# Using 'join' Method
print("Using 'join' Method:")

# Example 10: Join a list of strings into a single string
my_list = ["Hello", "World!"]
print("10.", " ".join(my_list))  # This will print: Hello World!

print()  # Blank line for spacing

# Using 'isdigit' Method
print("Using 'isdigit' Method:")

# Example 11: Check if all characters in the string are digits
my_string = "12345"
if my_string.isdigit():
    print("11. The string contains only digits.")  # This will be printed

print()  # Blank line for spacing

# Using 'isalpha' Method
print("Using 'isalpha' Method:")

# Example 12: Check if all characters in the string are alphabetic
my_string = "Hello"
if my_string.isalpha():
    print("12. The string contains only alphabetic characters.")  # This will be printed

print()  # Blank line for spacing

# Using 'isalnum' Method
print("Using 'isalnum' Method:")

# Example 13: Check if all characters in the string are alphanumeric
my_string = "Hello123"
if my_string.isalnum():
    print(
        "13. The string contains only alphanumeric characters."
    )  # This will be printed

print()  # Blank line for spacing

# Using 'startswith' Method
print("Using 'startswith' Method:")

# Example 14: Check if the string starts with a specific substring
my_string = "Hello, World!"
if my_string.startswith("Hello"):
    print("14. The string starts with 'Hello'.")  # This will be printed

print()  # Blank line for spacing

# Using 'endswith' Method
print("Using 'endswith' Method:")

# Example 15: Check if the string ends with a specific substring
my_string = "Hello, World!"
if my_string.endswith("World!"):
    print("15. The string ends with 'World!'.")  # This will be printed

print()  # Blank line for spacing

# Using 'count' Method
print("Using 'count' Method:")

# Example 16: Count occurrences of a substring in a string
my_string = "Hello, Hello, Hello!"
count = my_string.count("Hello")
print("16. 'Hello' appears", count, "times.")  # This will print: 3

print()  # Blank line for spacing

# Using 'capitalize' Method
print("Using 'capitalize' Method:")

# Example 17: Capitalize the first character of the string
my_string = "hello, world!"
print("17.", my_string.capitalize())  # This will print: Hello, world!

print()  # Blank line for spacing

# Using 'swapcase' Method
print("Using 'swapcase' Method:")

# Example 18: Swap the case of each character in the string
my_string = "Hello, World!"
print("18.", my_string.swapcase())  # This will print: hELLO, wORLD!

print()  # Blank line for spacing

# Using 'zfill' Method
print("Using 'zfill' Method:")

# Example 19: Pad the string on the left with zeros
my_string = "42"
print("19.", my_string.zfill(5))  # This will print: 00042

print()  # Blank line for spacing

# Using 'find' Method
print("Using 'find' Method:")

# Example 20: Find the index of a substring
my_string = "Hello, World!"
index = my_string.find("World")
print("20. 'World' found at index:", index)  # This will print: 7

print()  # Blank line for spacing

# Using 'replace' Method
print("Using 'replace' Method:")

# Example 21: Replace a substring with another substring
my_string = "Hello, World!"
print("21.", my_string.replace("World", "Python"))  # This will print: Hello, Python!

print()  # Blank line for spacing

# Using 'split' Method
print("Using 'split' Method:")

# Example 22: Split a string into a list of substrings
my_string = "Hello, World!"
print("22.", my_string.split(", "))  # This will print: ['Hello', 'World!']

print()  # Blank line for spacing

# Using 'join' Method
print("Using 'join' Method:")

# Example 23: Join a list of strings into a single string
my_list = ["Hello", "World!"]
print("23.", " ".join(my_list))  # This will print: Hello World!

print()  # Blank line for spacing

# Using 'strip' Method
print("Using 'strip' Method:")

# Example 24: Remove leading and trailing whitespace
my_string = "   Hello, World!   "
print("24.", my_string.strip())  # This will print: Hello, World!

print()  # Blank line for spacing

# Using 'lstrip' Method
print("Using 'lstrip' Method:")

# Example 25: Remove leading whitespace
my_string = "   Hello, World!"
print("25.", my_string.lstrip())  # This will print: Hello, World!

print()  # Blank line for spacing

# Using 'rstrip' Method
print("Using 'rstrip' Method:")

# Example 26: Remove trailing whitespace
my_string = "Hello, World!   "
print("26.", my_string.rstrip())  # This will print: Hello, World!

print()  # Blank line for spacing

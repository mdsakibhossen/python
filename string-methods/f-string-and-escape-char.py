# Using f-strings
print("Using f-strings\n")

# Example 1: Basic f-string formatting
name = "Alice"
age = 30
print(f"1. My name is {name} and I am {age} years old.")  # This will be printed

print()  # Blank line for spacing

# Example 2: f-string with expressions
a = 5
b = 10
print(f"2. The sum of {a} and {b} is {a + b}.")  # This will be printed

print()  # Blank line for spacing

# Example 3: f-string with floating-point precision
pi = 3.14159
print(f"3. Pi rounded to 2 decimal places is {pi:.2f}.")  # This will be printed

print()  # Blank line for spacing

# Example 4: f-string with dictionaries
person = {"name": "Bob", "age": 25}
print(
    f"4. My name is {person['name']} and I am {person['age']} years old."
)  # This will be printed

print()  # Blank line for spacing

# Example 5: f-string with list indexing
fruits = ["apple", "banana", "cherry"]
print(f"5. The first fruit is {fruits[0]}.")  # This will be printed

print()  # Blank line for spacing

# Using Escape Characters
print("Using Escape Characters\n")

# Example 6: Newline escape character
print("6. First line.\nSecond line.")  # This will be printed on two lines

print()  # Blank line for spacing

# Example 7: Tab escape character
print(
    "7. First column\tSecond column"
)  # This will print with a tab space between columns

print()  # Blank line for spacing

# Example 8: Backslash escape character
print("8. This is a backslash: \\")  # This will be printed: This is a backslash: \

print()  # Blank line for spacing

# Example 9: Single quote escape character
print("9. It's a sunny day.")  # This will be printed: It's a sunny day.

print()  # Blank line for spacing

# Example 10: Double quote escape character
print('10. She said, "Hello!"')  # This will be printed: She said, "Hello!"

print()  # Blank line for spacing

# Example 11: Multi-line string with triple quotes
print(
    """11. This is a multi-line string.
It can span multiple lines."""
)  # This will be printed as two lines

print()  # Blank line for spacing

# Example 12: Using escape characters in f-strings
name = "Charlie"
print(f'12. This is {name}, who said: "I love programming!"')  # This will be printed

print()  # Blank line for spacing

# Using f-strings
print("Using f-strings\n")

# Example 13: f-string with multiple types
temperature = 25.6789
humidity = 60
print(
    f"13. The temperature is {temperature:.1f}°C with {humidity}% humidity."
)  # This will be printed

print()  # Blank line for spacing

# Example 14: Formatting date and time
from datetime import datetime

now = datetime.now()
print(
    f"14. Current date and time: {now:%Y-%m-%d %H:%M:%S}"
)  # This will print the current date and time

print()  # Blank line for spacing

# Example 15: Nested f-strings
name = "David"
age = 22
print(f"15. {f'{name} is {age} years old.'}")  # This will be printed

print()  # Blank line for spacing


# Example 16: Using f-strings with function calls
def greet(name):
    return f"Hello, {name}!"


print(f"16. {greet('Emma')}")  # This will be printed

print()  # Blank line for spacing

# Using Escape Characters
print("Using Escape Characters\n")

# Example 17: Escape character in f-strings
favorite_quote = "To be or not to be"
author = "Shakespeare"
print(
    f'17. My favorite quote is: "{favorite_quote}" - {author}'
)  # This will be printed

print()  # Blank line for spacing

# Example 18: Including special characters in strings
special_string = "Price: $12.50"
print(f"18. {special_string}")  # This will be printed

print()  # Blank line for spacing

# Example 19: Escape characters with file paths
file_path = "C:\\Users\\Username\\Documents\\file.txt"
print(f"19. File path: {file_path}")  # This will be printed

print()  # Blank line for spacing

# Example 20: Raw string to avoid escape characters
raw_string = r"C:\Users\Username\Documents\file.txt"
print(f"20. Raw file path: {raw_string}")  # This will be printed

print()  # Blank line for spacing

# Example 21: f-string with conditional expressions
a = 8
b = 3
print(f"21. The larger number is: {a if a > b else b}.")  # This will be printed

print()  # Blank line for spacing

# Example 22: Formatting with scientific notation
large_number = 1234567890
print(f"22. Large number in scientific notation: {large_number:.2e}")  # This will be printed

print()  # Blank line for spacing

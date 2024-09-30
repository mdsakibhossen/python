# Identity Operators
print("Identity Operators")

# Is (True if both variables point to the same object)
# Example with integers
a = [1, 2, 3]
b = a  # b points to the same object as a
print("Is (True if both variables point to the same object)")
print("a is b:", a is b)                     # True
print("a is [1, 2, 3]:", a is [1, 2, 3])     # False (different objects)
print()  # Blank line for spacing

# Example with strings
str1 = "Hello"
str2 = "Hello"
# True (same value, same object in memory)
print("str1 is str2:", str1 is str2)
print("str1 is 'Hello':", str1 is 'Hello')    # True
print()  # Blank line for spacing

# Is Not (True if both variables do not point to the same object)
print("Is Not (True if both variables do not point to the same object)")
# False (they point to the same object)
print("a is not b:", a is not b)
print("a is not [1, 2, 3]:", a is not [1, 2, 3])  # True (different objects)
# False (they point to the same object)
print("str1 is not str2:", str1 is not str2)
print()  # Blank line for spacing

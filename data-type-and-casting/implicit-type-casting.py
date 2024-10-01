# Implicit Type Casting
print("Implicit Type Casting\n")

# Example 1: Implicit casting from int to float
print("1. Implicit Casting from int to float")
x = 5   # int
y = 2.5  # float
z = x + y  # Python implicitly converts x to float
print(f"{x} + {y} = {z} --> Type: {type(z)}\n")  # Output: 7.5 (float)

# Example 2: Implicit casting from int to float during division
print("2. Implicit Casting during Division")
a = 10   # int
b = 4  # float
result = a / b  # Python implicitly converts a to float
# Output: 2.5 (float)
print(f"{a} / {b} = {result} --> Type: {type(result)}\n")

# Example 3: Implicit casting from int to float during multiplication
print("3. Implicit Casting during Multiplication")
a = 10   # int
b = 4.0  # float
result = a * b  # Python implicitly converts a to float
# Output: 40.0 (float)
print(f"{a} * {b} = {result} --> Type: {type(result)}\n")



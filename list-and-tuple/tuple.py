# Tuple Methods Examples

# Example 1: count()
t = (1, 2, 2, 3, 4)
count_of_2 = t.count(2)
print(f"1. Count of 2 in tuple: {count_of_2}")  # Output: 2

print()  # Blank line for spacing

# Example 2: index()
t = (1, 2, 3, 4, 5)
index_of_3 = t.index(3)
print(f"2. Index of 3: {index_of_3}")  # Output: 2

print()  # Blank line for spacing

# Example 3: index() with start and end parameters
t = (10, 20, 30, 10, 40, 10)
index_of_10 = t.index(10, 1, 5)
print(f"3. Index of 10 between index 1 and 5: {index_of_10}")  # Output: 3

print()  # Blank line for spacing

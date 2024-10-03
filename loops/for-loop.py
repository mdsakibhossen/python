# Using 'for' Loops
print("Using 'for' Loops")

# Example 1: Iterating Over a List
print("Example 1: Iterating Over a List")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # Prints each fruit in the list
print()  # Blank line for spacing

# Example 2: Using 'range()' Function
print("Example 2: Using 'range()' Function")
for i in range(5):
    print(i)  # Prints numbers from 0 to 4
print()  # Blank line for spacing

# Example 3: Iterating Over a String
print("Example 3: Iterating Over a String")
word = "Python"
for letter in word:
    print(letter)  # Prints each letter in the string
print()  # Blank line for spacing

# Example 4: Iterating Over a Dictionary
print("Example 4: Iterating Over a Dictionary")
person = {"name": "John", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")  # Prints each key-value pair
print()  # Blank line for spacing

# Example 5: Nested 'for' Loops
print("Example 5: Nested 'for' Loops")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for num in row:
        print(num, end=" ")  # Prints each number in the matrix
    print()  # Prints a new line after each row
print()  # Blank line for spacing

# Example 6: 'for' Loop with 'else'
print("Example 6: 'for' Loop with 'else'")
numbers = [1, 2, 3, 4]
for num in numbers:
    print(num)  # Prints each number in the list
else:
    print("Loop finished")  # Prints after the loop completes
print()  # Blank line for spacing


# Example 7: Iterating Over a List with Indexes
print("Example 7: Iterating Over a List with Indexes")
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")  # Prints index and corresponding fruit
print()  # Blank line for spacing

# Example 8: Iterating Over a String with Indexes
print("Example 8: Iterating Over a String with Indexes")
word = "Python"
for index, letter in enumerate(word):
    print(f"Index {index}: {letter}")  # Prints index and corresponding letter
print()  # Blank line for spacing

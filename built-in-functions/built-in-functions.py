# Built-in Functions Examples

# Example 1: abs() - Absolute Value
number = -10
absolute_value = abs(number)
print(f"1. Absolute value of {number}:\n{absolute_value}")

print()  # Blank line for spacing

# Example 2: len() - Length of a String
my_string = "Hello, World!"
length_of_string = len(my_string)
print(f"2. Length of the string '{my_string}':\n{length_of_string}")

print()  # Blank line for spacing

# Example 3: sum() - Sum of a List
numbers = [1, 2, 3, 4, 5]
total_sum = sum(numbers)
print(f"3. Sum of {numbers}:\n{total_sum}")

print()  # Blank line for spacing

# Example 4: max() - Maximum Value
maximum_value = max(numbers)
print(f"4. Maximum value in {numbers}:\n{maximum_value}")

print()  # Blank line for spacing

# Example 5: min() - Minimum Value
minimum_value = min(numbers)
print(f"5. Minimum value in {numbers}:\n{minimum_value}")

print()  # Blank line for spacing

# Example 6: round() - Rounding a Number
pi_value = 3.14159
rounded_value = round(pi_value, 2)
print(f"6. Rounded value of {pi_value} to 2 decimal places:\n{rounded_value}")

print()  # Blank line for spacing

# Example 7: sorted() - Sorting a List
unsorted_numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(unsorted_numbers)
print(f"7. Sorted version of {unsorted_numbers}:\n{sorted_numbers}")

print()  # Blank line for spacing

# Example 8: str() - Convert to String
number = 100
string_value = str(number)
print(f"8. String representation of {number}:\n'{string_value}'")

print()  # Blank line for spacing

# Example 9: type() - Get the Type of an Object
object_type = type(string_value)
print(f"9. Type of the object '{string_value}':\n{object_type}")

print()  # Blank line for spacing

# Example 10: list() - Convert to List
my_tuple = (1, 2, 3)
converted_list = list(my_tuple)
print(f"10. Converted list from tuple {my_tuple}:\n{converted_list}")

print()  # Blank line for spacing

# Example 11: dict() - Create a Dictionary
my_dict = dict(name="Alice", age=30)
print(f"11. Created dictionary:\n{my_dict}")

print()  # Blank line for spacing

# Example 12: all() - Check if All Elements are True
boolean_list = [True, True, False]
all_true = all(boolean_list)
print(f"12. All elements in {boolean_list} are true:\n{all_true}")

print()  # Blank line for spacing

# Example 13: any() - Check if Any Element is True
any_true = any(boolean_list)
print(f"13. Any element in {boolean_list} is true:\n{any_true}")

print()  # Blank line for spacing

# Example 14: enumerate() - Enumerate a List
enumerated_list = list(enumerate(["a", "b", "c"]))
print(f"14. Enumerated list:\n{enumerated_list}")

print()  # Blank line for spacing

# Example 15: zip() - Combine Two Lists
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
zipped = list(zip(list1, list2))
print(f"15. Zipped list from {list1} and {list2}:\n{zipped}")

print()  # Blank line for spacing

# Example 16: input() - User Input
# Uncomment the next line to test user input
# user_input = input("Enter something: ")
# print(f"16. User input received:\n{user_input}")

print()  # Blank line for spacing

# Example 17: map() - Apply a Function to Each Element
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"17. Squared values of {numbers}:\n{squared_numbers}")

print()  # Blank line for spacing

# Example 18: filter() - Filter Elements
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"18. Even numbers from {numbers}:\n{even_numbers}")

print()  # Blank line for spacing

# Example 19: isinstance() - Check Instance Type
is_string = isinstance(my_string, str)
print(f"19. Is '{my_string}' a string?:\n{is_string}")

print()  # Blank line for spacing

# Example 20: sum() - Sum with Initial Value
initial_sum = sum(numbers, 10)
print(f"20. Sum of {numbers} with initial value 10:\n{initial_sum}")

print()  # Blank line for spacing

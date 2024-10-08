# Dictionary Examples

# Example 1: Creating a Dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}
print(f"1. Created dictionary:\n{my_dict}")

print()  # Blank line for spacing

# Example 2: Accessing Dictionary Values
name = my_dict["name"]
print(f"2. Name from dictionary: {name}")

print()  # Blank line for spacing

# Example 3: Adding a Key-Value Pair
my_dict["job"] = "Engineer"
print(f"3. Dictionary after adding job:\n{my_dict}")

print()  # Blank line for spacing

# Example 4: Updating a Value
my_dict["age"] = 31
print(f"4. Dictionary after updating age:\n{my_dict}")

print()  # Blank line for spacing

# Example 5: Removing a Key-Value Pair
del my_dict["city"]
print(f"5. Dictionary after removing city:\n{my_dict}")

print()  # Blank line for spacing

# Example 6: Using get() to Access Values
job = my_dict.get("job", "Not Found")
print(f"6. Job in dictionary: {job}")

print()  # Blank line for spacing

# Example 7: Checking if Key Exists
if "name" in my_dict:
    print("7. 'name' key exists in the dictionary.")
else:
    print("7. 'name' key does not exist.")

print()  # Blank line for spacing

# Example 8: Looping Through Keys and Values
for key, value in my_dict.items():
    print(f"8. Key: {key}, Value: {value}")

print()  # Blank line for spacing

# Example 9: Length of a Dictionary
dict_length = len(my_dict)
print(f"9. Length of dictionary: {dict_length}")

print()  # Blank line for spacing

# Example 10: Copying a Dictionary
copy_dict = my_dict.copy()
print(f"10. Copy of dictionary:\n{copy_dict}")

print()  # Blank line for spacing

# Example 11: Clearing a Dictionary
my_dict.clear()
print(f"11. Dictionary after clearing:\n{my_dict}")

print()  # Blank line for spacing

# Example 12: Getting All Keys
keys = copy_dict.keys()
print(f"12. Keys in the dictionary: {list(keys)}")

print()  # Blank line for spacing

# Example 13: Getting All Values
values = copy_dict.values()
print(f"13. Values in the dictionary: {list(values)}")

print()  # Blank line for spacing

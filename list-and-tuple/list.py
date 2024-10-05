# List Methods Examples

# Example 1: append()
my_list = [1, 2, 3]
my_list.append(4)
print(f"1. After appending 4: {my_list}")  # Output: [1, 2, 3, 4]

print()  # Blank line for spacing

# Example 2: extend()
my_list = [1, 2, 3]
my_list.extend([4, 5])
print(f"2. After extending with [4, 5]: {my_list}")  # Output: [1, 2, 3, 4, 5]

print()  # Blank line for spacing

# Example 3: insert()
my_list = [1, 2, 4]
my_list.insert(2, 3)
print(f"3. After inserting 3 at index 2: {my_list}")  # Output: [1, 2, 3, 4]

print()  # Blank line for spacing

# Example 4: remove()
my_list = [1, 2, 3, 4]
my_list.remove(3)
print(f"4. After removing 3: {my_list}")  # Output: [1, 2, 4]

print()  # Blank line for spacing

# Example 5: pop()
my_list = [1, 2, 3, 4]
popped_item1 = my_list.pop()
popped_item2 = my_list.pop(1)
print(
    f"5. Popped last item {popped_item1} & popped index-1 item: {popped_item2}. My List: {my_list}"
)  # Output: 4, [1, 2, 3]

print()  # Blank line for spacing

# Example 6: clear()
my_list = [1, 2, 3, 4]
my_list.clear()
print(f"6. After clearing: {my_list}")  # Output: []

print()  # Blank line for spacing

# Example 7: index()
my_list = [1, 2, 3, 4]
index_of_3 = my_list.index(3)
print(f"7. Index of 3: {index_of_3}")  # Output: 2

print()  # Blank line for spacing

# Example 8: count()
my_list = [1, 2, 2, 3, 4]
count_of_2 = my_list.count(2)
print(f"8. Count of 2: {count_of_2}")  # Output: 2

print()  # Blank line for spacing

# Example 9: sort()
my_list = [3, 1, 4, 2]
my_list.sort()
print(f"9. After sorting: {my_list}")  # Output: [1, 2, 3, 4]

print()  # Blank line for spacing

# Example 10: reverse()
my_list = [1, 2, 3, 4]
my_list.reverse()
print(f"10. After reversing: {my_list}")  # Output: [4, 3, 2, 1]

print()  # Blank line for spacing

# Example 11: copy()
my_list = [1, 2, 3, 4]
copied_list = my_list.copy()
print(f"11. Copied list: {copied_list}")  # Output: [1, 2, 3, 4]
print(f"my_list id: {id(my_list)}")
print(f"copied_list id: {id(copied_list)}")

print()  # Blank line for spacing

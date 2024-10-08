# Set Examples

# Example 1: Creating a Set
my_set = {1, 2, 3, 4, 5}
print(f"1. Created set:\n{my_set}")

print()  # Blank line for spacing

# Example 2: Adding an Element to a Set
my_set.add(6)
print(f"2. Set after adding 6:\n{my_set}")

print()  # Blank line for spacing

# Example 3: Removing an Element from a Set
my_set.remove(3)
print(f"3. Set after removing 3:\n{my_set}")

print()  # Blank line for spacing

# Example 4: Using discard() to Remove an Element
my_set.discard(7)  # Does not raise an error if 7 is not in the set
print(f"4. Set after discarding 7 (no error even if 7 is not present):\n{my_set}")

print()  # Blank line for spacing

# Example 5: Checking if an Element Exists in a Set
if 4 in my_set:
    print("5. 4 is present in the set.")
else:
    print("5. 4 is not present in the set.")

print()  # Blank line for spacing

# Example 6: Looping Through a Set
for item in my_set:
    print(f"6. Set item: {item}")

print()  # Blank line for spacing

# Example 7: Set Union
set_a = {1, 2, 3}
set_b = {3, 4, 5}
# union_set = set_a.union(set_b)
union_set = set_a | set_b
print(f"7. Union of set_a and set_b:\n{union_set}")

print()  # Blank line for spacing

# Example 8: Set Intersection
# intersection_set = set_a.intersection(set_b)
intersection_set = set_a & set_b
print(f"8. Intersection of set_a and set_b:\n{intersection_set}")

print()  # Blank line for spacing

# Example 9: Set Difference
# difference_set = set_a.difference(set_b)
difference_set = set_a - set_b
print(f"9. Difference of set_a - set_b:\n{difference_set}")

print()  # Blank line for spacing

# Example 10: Set Symmetric Difference
symmetric_difference_set = set_a.symmetric_difference(set_b)
print(f"10. Symmetric difference of set_a and set_b:\n{symmetric_difference_set}")

print()  # Blank line for spacing

# Example 11: Checking Subset
if {1, 2}.issubset(set_a):
    print("11. {1, 2} is a subset of set_a.")
else:
    print("11. {1, 2} is not a subset of set_a.")

print()  # Blank line for spacing

# Example 12: Checking Superset
if set_a.issuperset({1, 2}):
    print("12. set_a is a superset of {1, 2}.")
else:
    print("12. set_a is not a superset of {1, 2}.")

print()  # Blank line for spacing

# Example 13: Clearing a Set
set_a.clear()
print(f"13. Set after clearing:\n{set_a}")

print()  # Blank line for spacing

# Example 14: Copying a Set
copied_set = my_set.copy()
print(f"14. Copied set:\n{copied_set}")

print()  # Blank line for spacing

# Example 15: Length of a Set
set_length = len(my_set)
print(f"15. Length of the set:\n{set_length}")

# Using 'while' Loop
print("Using 'while' Loop")

# Example 1: Basic while loop
print("Example 1: Basic while Loop")
count = 0
while count < 5:
    print(f"Count is {count}")  # Prints count from 0 to 4
    count += 1
print()  # Blank line for spacing

# Example 2: Using while loop with a condition
print("Example 2: Using while Loop with a Condition")
number = 10
while number > 0:
    print(f"Number is {number}")  # Prints number starting from 10 down to 1
    number -= 2
print()  # Blank line for spacing

# Example 3: while loop with break statement
print("Example 3: while Loop with 'break'")
i = 1
while i <= 10:
    if i == 5:
        print("Breaking the loop at 5")
        break  # Exits the loop when i is 5
    print(f"i is {i}")  # Prints i from 1 to 4
    i += 1
print()  # Blank line for spacing

# Example 4: while loop with continue statement
print("Example 4: while Loop with 'continue'")
j = 0
while j < 5:
    j += 1
    if j == 3:
        print("Skipping the value 3")
        continue  # Skips the rest of the loop when j is 3
    print(f"j is {j}")  # Prints j except 3
print()  # Blank line for spacing

# Example 5: Infinite loop (with break to prevent infinite run)
print("Example 5: Infinite Loop with 'break'")
k = 0
while True:
    print(f"Infinite loop iteration: {k}")
    k += 1
    if k >= 3:
        print("Breaking the infinite loop after 3 iterations")
        break  # Breaks the infinite loop after 3 iterations
print()  # Blank line for spacing

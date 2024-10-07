# File Handling and OS Module Examples

# Example 1: Reading a file
with open("input.txt", "r") as file:
    content = file.read()
print(f"1. Content of input.txt:\n{content}")

print()  # Blank line for spacing

# Example 2: Writing to a file
with open("output.txt", "w") as file:
    file.write("Hello, World!")
print(f"2. 'Hello, World!' written to output.txt")

print()  # Blank line for spacing

# Example 3: Appending to a file
with open("output.txt", "a") as file:
    file.write("\nAppended line.")
print(f"3. Line appended to output.txt")

print()  # Blank line for spacing

# Example 4: Reading a file line by line
with open("input.txt", "r") as file:
    lines = file.readlines()
print(f"4. Lines in input.txt:\n{lines}")

print()  # Blank line for spacing

# Example 5: Writing multiple lines to a file
lines_to_write = ["Line 1", "Line 2", "Line 3"]
with open("output.txt", "w") as file:
    file.writelines([line + "\n" for line in lines_to_write])
print(f"5. Multiple lines written to output.txt")

print()  # Blank line for spacing

# Example 6: Using 'with' for safe file handling
try:
    with open("input.txt", "r") as file:
        data = file.read()
    print(f"6. File read successfully:\n{data}")
except FileNotFoundError:
    print("6. input.txt not found.")

print()  # Blank line for spacing

# Example 7: Checking if file exists before reading
import os

if os.path.exists("input.txt"):
    with open("input.txt", "r") as file:
        content = file.read()
    print(f"7. File content:\n{content}")
else:
    print("7. input.txt does not exist.")

print()  # Blank line for spacing

# Example 8: Get Current Working Directory
current_directory = os.getcwd()
print(f"8. Current working directory: {current_directory}")

print()  # Blank line for spacing

# Example 9: Change Current Working Directory
os.chdir("/path/to/directory")  # Update this with a real path
print(f"9. Changed working directory to: {os.getcwd()}")

print()  # Blank line for spacing

# Example 10: List Files in a Directory
files = os.listdir(".")
print(f"10. Files and directories in current directory: {files}")

print()  # Blank line for spacing

# Example 11: Create a Directory
os.mkdir("new_folder")
print("11. 'new_folder' created successfully.")

print()  # Blank line for spacing

# Example 12: Remove a Directory
os.rmdir("new_folder")
print("12. 'new_folder' removed successfully.")

print()  # Blank line for spacing

# Example 13: Rename a File or Directory
os.rename("old_name.txt", "new_name.txt")  # Ensure 'old_name.txt' exists
print("13. File renamed from 'old_name.txt' to 'new_name.txt'.")

print()  # Blank line for spacing

# Example 14: Check if a File Exists
if os.path.exists("input.txt"):
    print("14. 'input.txt' exists.")
else:
    print("14. 'input.txt' does not exist.")

print()  # Blank line for spacing

# Example 15: Get File Size
file_size = os.path.getsize("input.txt")
print(f"15. Size of 'input.txt': {file_size} bytes")

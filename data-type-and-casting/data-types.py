# Data Types
print("Data Types\n")

# String type
print("1. String Type")
text = "Hello"
print(f"{text} --> Type: {type(text)}\n")  # Output: <class 'str'>

# Integer type
print("2. Integer Type")
integer_num = 42
# Output: <class 'int'>
print(f"{integer_num} --> Type: {type(integer_num)}\n")

# Float type
print("3. Float Type")
float_num = 3.14
print(f"{float_num} --> Type: {type(float_num)}\n")  # Output: <class 'float'>

# Complex type
print("4. Complex Type")
complex_num = 2 + 3j
# Output: <class 'complex'>
print(f"{complex_num} --> Type: {type(complex_num)}\n")

# Boolean type
print("5. Boolean Type")
boolean_true = True
boolean_false = False
# Output: <class 'bool'>
print(f"{boolean_true} --> Type: {type(boolean_true)}")
# Output: <class 'bool'>
print(f"{boolean_false} --> Type: {type(boolean_false)}\n")

# List type
print("6. List Type")
my_list = [1, 2, 3, 4, 5]
print(f"{my_list} --> Type: {type(my_list)}\n")  # Output: <class 'list'>

# Tuple type
print("7. Tuple Type")
my_tuple = (1, 2, 3)
print(f"{my_tuple} --> Type: {type(my_tuple)}\n")  # Output: <class 'tuple'>

# Dictionary type
print("8. Dictionary Type")
my_dict = {"name": "Alice", "age": 30}
print(f"{my_dict} --> Type: {type(my_dict)}\n")  # Output: <class 'dict'>

# Set type
print("9. Set Type")
my_set = {1, 2, 3}
print(f"{my_set} --> Type: {type(my_set)}\n")  # Output: <class 'set'>

# Frozenset type
print("10. Frozenset Type")
my_frozenset = frozenset([1, 2, 3])
# Output: <class 'frozenset'>
print(f"{my_frozenset} --> Type: {type(my_frozenset)}\n")

# Bytes type
print("11. Bytes Type")
my_bytes = bytes([50, 100, 76])
print(f"{my_bytes} --> Type: {type(my_bytes)}\n")  # Output: <class 'bytes'>

# Bytearray type
print("12. Bytearray Type")
my_bytearray = bytearray([50, 100, 76])
# Output: <class 'bytearray'>
print(f"{my_bytearray} --> Type: {type(my_bytearray)}\n")

# Memoryview type
print("13. Memoryview Type")
my_memoryview = memoryview(my_bytes)
# Output: <class 'memoryview'>
print(f"{my_memoryview} --> Type: {type(my_memoryview)}\n")

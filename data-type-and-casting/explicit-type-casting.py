# Explicit Type Casting
print("Explicit Type Casting\n")

# Example 1: Casting float to int
print("1. Explicit Casting from float to int")
float_num = 7.8  # float
int_num = int(float_num)  # explicit conversion to int
# Output: 7 (int)
print(f"int({float_num}) = {int_num} --> Type: {type(int_num)}\n")

# Example 2: Casting string to int
print("2. Explicit Casting from string to int")
str_num = "42"  # string
converted_int = int(str_num)  # explicit conversion to int
# Output: 42 (int)
print(f"int({str_num}) = {converted_int} --> Type: {type(converted_int)}\n")

# Example 3: Casting string to float
print("3. Explicit Casting from string to float")
str_float = "3.14"  # string
converted_float = float(str_float)  # explicit conversion to float
print(f"float({str_float}) = {converted_float} --> Type: {type(converted_float)}\n")  # Output: 3.14 (float)

# Example 4: Casting int to string
print("4. Explicit Casting from int to string")
number = 100  # int
converted_str = str(number)  # explicit conversion to string
# Output: '100' (str)
print(f"str({number}) = '{converted_str}' --> Type: {type(converted_str)}\n")

# Example 5: Casting float to complex
print("5. Explicit Casting from float to complex")
real_num = 5.5  # float
complex_num = complex(real_num)  # explicit conversion to complex
# Output: (5.5+0j)
print(f"complex({real_num}) = {complex_num} --> Type: {type(complex_num)}\n")

# Example 6: Multiple explicit conversions
print("6. Multiple Explicit Conversions")
original_value = "12.34"  # string
float_value = float(original_value)  # convert to float
int_value = int(float_value)  # convert to int
print(f"Original value: '{original_value}' --> Float: {float_value} --> Int: {int_value} --> Type of int_value: {type(int_value)}\n")  # Output: 12 (int)

print()  # Blank line for spacing

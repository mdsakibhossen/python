# Python Data Types and Casting

## Data Types in Python

### 1. Numeric Types
- **int**: Integer values, e.g., `5`, `-10`
- **float**: Floating-point numbers (decimals), e.g., `5.7`, `-3.14`
- **complex**: Complex numbers, e.g., `3 + 2j`

### 2. Text Type
- **str**: Strings represent sequences of characters, e.g., `"Hello, World!"`

### 3. Boolean Type
- **bool**: Represents truth values, `True` or `False`

### 4. Sequence Types
- **list**: A mutable collection of items, e.g., `[1, 2, 3]`
- **tuple**: An immutable collection of items, e.g., `(1, 2, 3)`
- **range**: Represents a sequence of numbers, e.g., `range(6)` (which gives `0, 1, 2, 3, 4, 5`)

### 5. Mapping Type
- **dict**: A collection of key-value pairs, e.g., `{"name": "Alice", "age": 25}`

### 6. Set Types
- **set**: An unordered collection of unique items, e.g., `{1, 2, 3}`
- **frozenset**: Immutable version of a set

### 7. Binary Types
- **bytes**: Immutable sequences of bytes
- **bytearray**: Mutable sequences of bytes
- **memoryview**: Memory views of another object

---

# Type Casting in Python

In Python, **type casting** refers to converting one data type to another. Type casting can be classified into two types:

---

## 1. Implicit Type Casting

In **implicit type casting**, Python automatically converts one data type into another without the need for explicit instructions. Python handles the conversion when it encounters different data types in an expression.

---

### 1.1 Implicit Casting with Numeric Types

When performing operations between different numeric types (`int`, `float`, `complex`), Python automatically promotes the lower precision type to the higher precision type.

#### Example (int and float):
```python
x = 5   # int
y = 2.5 # float
z = x + y  # Python implicitly converts x to float
print(z)  # Output: 7.5 (float)
```
## 2. Explicit Type Casting

In explicit type casting, the user manually converts one data type into another using Python's built-in functions. This is useful when Python cannot automatically convert data types or when you need precise control over the conversion.

### Common Explicit Type Casting Functions

#### 2.1 Casting to Integer (`int()`)

Converts a floating-point number or a string (if it contains digits) to an integer.

##### Example:
```python
x = 4.7
y = int(x)  # Converts float to int, removes the decimal part
print(y)  # Output: 4
```
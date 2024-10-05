# Tuple Methods

Tuples are immutable sequences in Python, meaning they cannot be changed after they are created. They are very similar to lists but with fewer available methods due to their immutability.

## 1. `count()`

The `count()` method returns the number of occurrences of a specified value in a tuple.

**Syntax:**

```python
tuple.count(value)
```

**Example:**

```python
t = (1, 2, 3, 1, 1)
print(t.count(1))  # Output: 3
```

## 2. `index()`

The `index()` method returns the first index of a specified value in a tuple. If the value is not found, it raises a `ValueError`.

**Syntax:**

```python
tuple.index(value, start, end)
```

- `value`: The element to be searched.
- `start` (optional): The starting position to search from.
- `end` (optional): The ending position to stop the search.

**Example:**

```python
t = (1, 2, 3, 4, 5)
print(t.index(3))  # Output: 2
```

## Tuple Operations

Since tuples are immutable, you cannot modify them directly. However, you can perform operations like concatenation, slicing, etc.

## 1. Tuple Concatenation

You can concatenate two tuples using the `+` operator.

**Example:**

```python
t1 = (1, 2, 3)
t2 = (4, 5, 6)
result = t1 + t2
print(result)  # Output: (1, 2, 3, 4, 5, 6)
```

## 2. Tuple Repetition

You can repeat a tuple using the `*` operator.

**Example:**

```python
t = (1, 2, 3)
print(t * 3)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)
```

## 3. Tuple Slicing

You can slice a tuple similar to a list.

**Example:**

```python
t = (1, 2, 3, 4, 5)
print(t[1:3])  # Output: (2, 3)
```

## 4. Checking Membership

You can check if an element exists in a tuple using the `in` keyword.

**Example:**

```python
t = (1, 2, 3, 4)
print(3 in t)  # Output: True
```

## 5. Length of Tuple

You can find the length of a tuple using the `len()` function.

**Example:**

```python
t = (1, 2, 3)
print(len(t))  # Output: 3
```

## 6. Minimum and Maximum

You can find the minimum and maximum values in a tuple using the `min()` and `max()` functions.

**Example:**

```python
t = (3, 1, 4, 2)
print(min(t))  # Output: 1
print(max(t))  # Output: 4
```

## 7. Tuple Conversion

You can convert other data types to tuples using the `tuple()` function.

**Example:**

```python
lst = [1, 2, 3]
t = tuple(lst)
print(t)  # Output: (1, 2, 3)
```

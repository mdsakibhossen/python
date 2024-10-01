# Python Operators:

## Arithmetic Operators
These are used for basic mathematical operations:
- `+` (Addition)
- `-` (Subtraction)
- `*` (Multiplication)
- `/` (Division)
- `%` (Modulus)
- `**` (Exponentiation)
- `//` (Floor division)

## Comparison (Relational) Operators
These compare two values:
- `==` (Equal)
- `!=` (Not equal)
- `>` (Greater than)
- `<` (Less than)
- `>=` (Greater than or equal to)
- `<=` (Less than or equal to)

## Assignment Operators
These assign values to variables:
- `=` (Assign)
- `+=` (Add and assign)
- `-=` (Subtract and assign)
- `*=` (Multiply and assign)
- `/=` (Divide and assign)
- `%=` (Modulus and assign)
- `**=` (Exponentiation and assign)
- `//=` (Floor division and assign)

## Logical Operators
These are used to combine conditional statements:
- `and` (Returns True if both statements are true)
- `or` (Returns True if one of the statements is true)
- `not` (Reverses the result)

## Bitwise Operators
These work on bits and perform bit-by-bit operations:
- `&` (AND)
- `|` (OR)
- `^` (XOR)
- `~` (NOT)
- `<<` (Left shift)
- `>>` (Right shift)

## Membership Operators
These test if a sequence contains an object:
- `in` (True if the value is found in the sequence)
- `not in` (True if the value is not found in the sequence)

## Identity Operators
These compare the memory location of two objects:
- `is` (True if both variables point to the same object)
- `is not` (True if both variables do not point to the same object)




# Operator Precedence in Python

Operator precedence determines the order in which operators are evaluated in an expression. Operators with higher precedence are evaluated before operators with lower precedence. In cases where operators have the same precedence, the associativity (left-to-right or right-to-left) is applied.

## Precedence Levels

1. **Parentheses**: `()` 
   - Highest precedence. Expressions inside parentheses are evaluated first.

2. **Exponentiation**: `**`
   - Right-to-left associativity.

3. **Unary Plus and Minus**: `+x`, `-x`
   - Applies to a single operand.

4. **Multiplication, Division, Floor Division, Modulus**: `*`, `/`, `//`, `%`
   - Left-to-right associativity.

5. **Addition and Subtraction**: `+`, `-`
   - Left-to-right associativity.

6. **Bitwise Shift Operators**: `<<`, `>>`
   - Left-to-right associativity.

7. **Bitwise AND**: `&`
   - Left-to-right associativity.

8. **Bitwise XOR**: `^`
   - Left-to-right associativity.

9. **Bitwise OR**: `|`
   - Left-to-right associativity.

10. **Comparison Operators**: `==`, `!=`, `>`, `<`, `>=`, `<=`
    - Left-to-right associativity.

11. **Identity Operators**: `is`, `is not`
    - Left-to-right associativity.

12. **Membership Operators**: `in`, `not in`
    - Left-to-right associativity.

13. **Logical NOT**: `not`
    - Highest precedence among logical operators.

14. **Logical AND**: `and`
    - Lower precedence than `not`.

15. **Logical OR**: `or`
    - Lowest precedence among logical operators.


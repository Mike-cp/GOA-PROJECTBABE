# 1) Counting sheep...
def count_sheep(num):
    return ''.join(f"{i} sheep..." for i in range(1, num+1))

# 2) Sum of positive
def positive_sum(arr):
    return sum(x for x in arr if x > 0)

# 3) Find the first non-consecutive number
def first_non_consecutive(arr):
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1] + 1:
            return arr[i]
    return None

# 4) Basic Mathematical Operations
def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2

# 5) Convert boolean values to strings 'Yes' or 'No'
def bool_to_word(b):
    return "Yes" if b else "No"

# 6) Multiplying two numbers
def multiply(a, b):
    return a * b

# 7) Remove First and Last Character
def remove_char(s):
    return s[1:-1]

# 8) Is this a triangle?
def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

# 9) Convert a Number to a String!
def number_to_string(num):
    return str(num)

# 10) Remove String Spaces
def no_space(x):
    return x.replace(" ", "")

# 11) Beginner - Reduce but Grow
from functools import reduce
def grow(arr):
    return reduce(lambda x, y: x * y, arr, 1)

# 12) Sum of two lowest positive integers
def sum_two_smallest_numbers(numbers):
    a, b = sorted(numbers)[:2]
    return a + b

# 13) Opposite number
def opposite(number):
    return -number

# 14) Disemvowel Trolls
def disemvowel(string_):
    return ''.join(c for c in string_ if c.lower() not in 'aeiou')

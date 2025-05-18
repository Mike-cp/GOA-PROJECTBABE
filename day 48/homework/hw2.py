# 2) Sum without highest and lowest number
def sum_array(arr):
    if not arr or len(arr) <= 2:
        return 0
    return sum(arr) - max(arr) - min(arr)

# 3) Convert a string to an array
def string_to_array(s):
    return s.split()

# 4) Count the number of cubes with paint on
def count_visible_cubes(n):
    if n == 1:
        return 1
    return 6 * n * n - 12 * n + 8

# 5) MakeUpperCase
def make_upper_case(s):
    return s.upper()

# 6) Quarter of the year
def quarter_of(month):
    return (month - 1) // 3 + 1

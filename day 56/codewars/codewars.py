def first_non_consecutive(arr):
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1] + 1:
            return arr[i]
    return None

def to_alternating_case(string):
    return string.swapcase()

def correct(s):
    s = s.replace('5', 'S')
    s = s.replace('0', 'O')
    s = s.replace('1', 'I')
    return s

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

def bonus_time(salary, bonus):
    if bonus:
        return f"${salary * 10}"
    else:
        return f"${salary}"

def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else:
        return 0

def sum_str(a, b):
    a = int(a) if a else 0
    b = int(b) if b else 0
    return str(a + b)

# The following function had syntax errors, corrected for completeness
def expression_matter(a, b, c):
    return max(a + b + c, a * b * c, (a + b) * c, a * (b + c))

def how_much_i_love_you(nb_petals):
    num = nb_petals % 6
    if num == 0: return "not at all"
    elif num == 1: return "I love you"
    elif num == 2: return "a little"
    elif num == 3: return "a lot"
    elif num == 4: return "passionately"
    elif num == 5: return "madly"

def reverse_list(l):
    return l[::-1]

def odd_count(n):
    return n // 2

def reverse_list(l):
    l.reverse()
    return l

def find_difference(a, b):
    v_a = a[0] * a[1] * a[2]
    v_b = b[0] * b[1] * b[2]
    return abs(v_a - v_b)

def greet(language):
    all_lang = [ 
        ("english", "Welcome"), ("czech", "Vitejte"), ("danish", "Velkomst"),
        ("dutch", "Welkom"), ("estonian", "Tere tulemast"), ("finnish", "Tervetuloa"),
        ("flemish", "Welgekomen"), ("french", "Bienvenue"), ("german", "Willkommen"),
        ("irish", "Failte"), ("italian", "Benvenuto"), ("latvian", "Gaidits"),
        ("lithuanian", "Laukiamas"), ("polish", "Witamy"), ("spanish", "Bienvenido"),
        ("swedish", "Valkommen"), ("welsh", "Croeso")
    ]
    for key in all_lang:
        if key[0] == language:
            return key[1]
    return "Welcome"

def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif age < 18:
        return "drink coke"
    elif age < 21:
        return "drink beer"
    else:
        return "drink whisky"

def two_sort(lst):
    return '***'.join(sorted(lst)[0])

la_liga_goals = 43
champions_league_goals = 10
copa_del_rey_goals = 5
total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals

def solution(a, b):
    if len(a) > len(b):
        return b + a + b
    else:
        return a + b + a

def fix_the_meerkat(arr):
    arr.reverse()
    return arr


# Printing a name
print("mika")

# Printing a string
print("idk321")

# Printing multiple lines of text
print("poem1")
print("poem2")
print("poem3")

# Printing numbers and patterns
print(2 + 3)
print("#")
print("###")
print("######")

# Performing arithmetic operations with integers and floats
num1 = int("42")
num2 = float(3.5)
num3 = float(2.5)
print(num2 + num3)

# Concatenating strings and checking variable types
hello = "hello"
world = "world"
print(hello + " " + world)
a = "hi"
b = 42
c = 3.14
print(type(a))
print(type(b))
print(type(c))

# Taking user input and performing operations
age = int(input("enter your age: "))
print(age + 1)

name = str(input("enter your name: "))
print("hello", name)

num1 = int(input("first number: "))
num2 = int(input("second number: "))
print(num1 + num2)

color = str(input("what is your favorite color?: "))
print("your favorite color is", color)

# Conditional statement to check height
height = int(input("enter your height in cm: "))
if height > 180:
    print("you are very tall")
else:
    print("you are short")

# Using a for loop to iterate through a range
for i in range(1, 6):
    print(i)

# Summing numbers using a for loop
sum_numbers = 0
for i in range(1, 11):
    sum_numbers += i
print(sum_numbers)

# Printing multiplication table using a for loop
for i in range(1, 6):
    print(f"2 x {i} = {2 * i}")

# Using a while loop with a break condition
num1 = 1
while True:
    if num1 == 6:
        break
    else:
        print(num1)
    num1 += 1

# Countdown using a while loop
num = 10
while num > 0:
    print(num)
    num -= 1

# Printing odd numbers using a while loop
num = 1
while num <= 10:
    if num % 2 != 0:
        print(num)
    num += 1

# Password validation using a while loop
password = "exit"
while True:
    user = input("enter your password: ")
    if user == password:
        print("correct password")
        break
    else:
        print("try again")

# Iterating through a list and printing its elements
list1 = ["apple", True, 3.14, 7]
for i in list1:
    print(i)

# Printing the length of a list
list1 = [10, 20, 30, 40, 50]
print("The length of the list is:", len(list1))

# Accessing elements in a list by index
list1 = ["index1", "index2"]
print(list1[1])

# Adding and removing elements from a list
list1 = ["apple", "banana", "cherry"]
list1.append("grape")
print(list1)

list1.remove("banana")
print(list1)

# Using list comprehensions for various operations
squares = [x**2 for x in range(1, 6)]
print(squares)

even_numbers = [x for x in range(2, 11) if x % 2 == 0]
print(even_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = [x for x in numbers if x % 2 != 0]
print(odd_numbers)

list1 = ["apple", "banana", "cherry"]
upper = [x.upper() for x in list1]
print(upper)

squared_if_divisible_by_2 = [x**2 for x in numbers if x % 2 == 0]
print(squared_if_divisible_by_2)

# Defining and using functions
def greet(name):
    return f"hello {name}"

print(greet("cotne"))

def calculate(num1, num2):
    return num1 + num2

print(calculate(2, 5))

def even_or_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

def area(length, width):
    return length * width

def reverse(string):
    return string[::-1]

# Working with tuples
tuple1 = (1, "hello", 3.14)
print(tuple1)

print(tuple1[1])

print(len(tuple1))

tuple2 = ("a", "b", "c")
result = tuple1 + tuple2
print(result)

element_to_check = "hello"
if element_to_check in tuple1:
    print("Found")
else:
    print("Not found")

# Working with sets
my_set = {1, "hello", 3.14}
print(my_set)

if "hello" in my_set:
    print("Yes")
else:
    print("No")

my_set.add("new_element")
print(my_set)

my_set.remove("hello")
print(my_set)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print(union_set)

#codewars

a = "code"
b = "wa.rs"
name = a + b

def get_char(c):
    return chr(c)

print(get_char(65))
print(get_char(97))
print(get_char(48))
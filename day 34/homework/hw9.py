#10) Write a function that iterates through a range of numbers (e.g., 1 to 100) and sums up all the numbers divisible by 3. Return the total sum.

def all_numbers_3(numbers):
    non_divisable = []
    divisable = []
    for num in numbers:
        if num % 3 != 0:
            non_divisable.append(num)
        else:
            divisable.append(num)
    return non_divisable,divisable

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
non_divisable, divisable = all_numbers_3(list)
print("Non divisable: ",non_divisable)
print("divisable: ",divisable)
    
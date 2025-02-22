def maximum_number(number=0):
    max_number = number[0]
    for num in number[1:]:
        if num > max_number:
            max_number = num
    return max_number
        

number = [10, 25, 8, 99, 32, 5]
print(maximum_number(number))

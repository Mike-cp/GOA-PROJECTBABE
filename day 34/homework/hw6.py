def checker(numbers):
    results = []
    for num in numbers:
        if num % 2 == 0:
            results.append(f"{num} is even")
        else:
            results.append(f"{num} is odd")
    return results  

number_list = [15, 65, 78, 432, 234, 54, 123, 43, 78, 10]
print(checker(number_list))

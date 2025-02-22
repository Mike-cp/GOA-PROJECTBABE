def anti_negatives(numbers):
    negative_list = []
    positive_list = []

    for num in numbers:
        if num > 0:
            positive_list.append(num)  
        elif num < 0:
            negative_list.append(num)

    
    return positive_list, negative_list



numbers = [-10, 25, -8, 99, -32, 5]
positive, negative = anti_negatives(numbers)

print("Positive numbers:", positive)  
print("Negative numbers:", negative)  


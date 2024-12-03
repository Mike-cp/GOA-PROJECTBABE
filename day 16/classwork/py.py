
whole_number = input("Please enter a whole number: ")


number = int(whole_number)


total_sum = 0

for i in range(0, number + 1):
    total_sum += i  

print("The sum of numbes from 0", number, "is:", total_sum)

correct_number= 12
counter= 0
enter_your_number = int(input("enter your number: "))
while correct_number != enter_your_number: 
    enter_your_number = int(input("enter ur number: "))
    counter= counter + 1
print("Accses granted")
print("attempts", int(counter))


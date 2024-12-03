correct_password = "MIKA"
Enter_your_password = str(input("enter_your_password:"))
counter= 0
while correct_password != Enter_your_password:
    correct_password = input(input("enter_your_password:"))
    counter = counter + 1
print("accses")
print( "atteps", int(counter))

    
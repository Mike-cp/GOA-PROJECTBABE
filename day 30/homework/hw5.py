def cap(frist, second, third):
    if second == second.capitalize():
        print(second)
    else:
        if second != second.capitalize():
            new = second.capitalize()
            print(new)
            
    if third == third.capitalize():
        print(frist)
    else:
        if third != third.capitalize():
            new = third.capitalize()
            print(new)

    if frist == frist.capitalize():
        print(frist)
    else:
        if frist != frist.capitalize():
            new = frist.capitalize()
            print(new)




frist1 = input("Enter frist string: ")
frist2 = input("Enter second string: ")
frist3 = input("Enter third string: ")

cap(frist1, frist2, frist3)
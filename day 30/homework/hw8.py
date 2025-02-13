def finder(string, Findword):
    
    index = string.find(Findword)

    if Findword != -1:
        print("the character",Findword, "was found at", index)

    else:
        if Findword == -1:
            print("the character", Findword,"was not found")

string1 = input("Enter your string: ")
find = input("Enter your character: ")
finder(string1,find)
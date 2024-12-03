password = "password"
Enter_password = str(input("enter your password:"))
count = 0

while password != Enter_password:
    Enter_password = str(input("Enter your password:"))
    count = count+1
print("counts",int(count))


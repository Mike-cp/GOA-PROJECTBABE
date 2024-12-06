username = str(input("ENTER YOUR USERNAME:"))
PASSWORDs = (input("ENTER YOUR PASSWORD:"))

Enter_USERNAME = str(input("ENTER YOUR USERNAME:"))
Enter_PASSWORD = (input("ENTER YOUR PASSWORD:"))

count = 0

while username != Enter_USERNAME and Enter_PASSWORD != PASSWORDs:
    Enter_USERNAME = str(input("ENTER YOUR USERNAME:"))
    Enter_PASSWORDs = (input("ENTER YOUR PASSWORD:"))
    count = count +1
    print("password or name is inncorect")

print("your count",int(count))
print("ACCSES GRANTED")


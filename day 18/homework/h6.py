password = "Goa has the worst coin system"
Enter_your_number = str(input("Enter your password:"))
count = 0

while password != Enter_your_number:
    Enter_your_number = str(input("Enter your password"))
    count = count + 1
print("attempts:", int(count))
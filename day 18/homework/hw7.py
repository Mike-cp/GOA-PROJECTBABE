Enter_Your_number=int(input("Enter your number:"))
Enter_your_number2 = int(input("Enter your second number:"))
operator = input("enter your operator(+, -, *, /):")
operator2 = "+, -, *, /"

if operator == "+":
    result = Enter_Your_number + Enter_your_number2
    print(result)
if operator == "-":
    result = Enter_Your_number - Enter_your_number2
    print(result)
if operator == "*":
    result = Enter_Your_number * Enter_your_number2
    print(result)
if operator == "/":
    if Enter_Your_number %2 == 0:
       result = Enter_Your_number / Enter_your_number2
       print(result)
    else:
       print("division by 0 is inncorect")


    











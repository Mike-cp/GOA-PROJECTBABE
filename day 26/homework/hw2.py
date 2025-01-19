def Odd_or_even(num1,num2):
    if num1 % 2 == 0:
        print(num1,"Is even")
    else:
        print(num2,"Is odd")

    if num2 % 2 == 0:
        print(num1,"is even")
    else:
        print(num2,"is odd")
   
num1 = float(input("Enter your number"))
num2 = float(input("Enter your second number:"))
Odd_or_even(num1,num2)
    
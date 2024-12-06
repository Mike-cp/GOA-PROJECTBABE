
num1 = int(input("enter your number:"))
num2 = int(input("enter your number:"))


if num1 > num2:
    for i in range(num2, num1 + 1):
        if i % 2 == 0:
            print(i, "ლუწი")


if num2 > num1:
    for i in range(num1, num2 + 1):
        if i % 2 != 0:
            print(i, "კენტი")


if num1 == num2:
    print("რიცხვები თანაბარია")

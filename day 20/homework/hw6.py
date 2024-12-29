num1 = int(input("Enter your number: "))


if num1 <= 1:
    print("This number is not prime.")

elif num1 == 2:
    print("This number is prime.")
else:

    for i in range(2, int(num1 ** 0.5) + 1):
        if num1 % i == 0:
            print("This number is not prime.")
            break
    else:
        print("This number is prime.")


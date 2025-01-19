name = input("Enter your name: ")
choose = input("Please choose 'u' or 'L': ")

if choose == 'u':
    print(name.upper())
elif choose == 'L':
    print(name.lower())
else:
    print("It's incorrect")

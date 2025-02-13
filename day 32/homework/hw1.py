def welcomer(name,age):
    return f"Welcome {name}! You are {age} years old."

age = int(input("Enter your age:  "))
name = str(input("Enter your name:  "))
print(welcomer(name,age))
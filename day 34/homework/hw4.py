def greetings(name="Guest"):
    return f"hello {name}"

name = input("enter yo name: ")
print(greetings(name))
print(greetings())
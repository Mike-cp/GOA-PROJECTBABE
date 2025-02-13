#4) Write a function that takes a first name and last name, capitalizes them, and formats them into a single string.

def captilazor(frist_name,last_name):
    new_name_1 = frist_name.capitalize()
    new_name_2 = last_name.capitalize()
    return f"{new_name_1} {new_name_2}"

frist_name1 = (input("Enter your frist name:  "))
last_name2 = (input("Enter your last name:  "))
print(captilazor(frist_name1,last_name2))
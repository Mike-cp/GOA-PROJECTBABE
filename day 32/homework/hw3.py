# 5) Create a function that takes a string, reverses it, and formats it within a sentence.

def reverser(String):
    string1 = String[::-1]
    return f"your reversed string is: {string1}"

Strings = input("Enter your string to be reversed:")
print(reverser(Strings))
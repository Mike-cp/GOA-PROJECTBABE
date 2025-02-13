# 9) Write a function that takes a paragraph and splits it into sentences based on periods.
def spliter(text):
    spliterer = text.split(".")
    return spliterer

text1 = input("Enter yo text here bbg: ")
print(spliter(text1))
Text = input("Enter the value: ")
Sentence = "i love programming in python!"

positions = Sentence.find(Text)

if positions != -1:
    print("your text position is at", positions)
else:
    print("your provided value",Text, "has not been found")
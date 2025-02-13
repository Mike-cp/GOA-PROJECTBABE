text = "the thing is that the Eminemce in shadow is the best anime in the world! isekai prob"
word = input("Enter character(word): ")
word_appear = text.count(word)

if word_appear != -1:
    print("the word appeared in your text",word_appear,"times")
else:
    print("The word has not been apeared in the text")
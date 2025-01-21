def count(text,word):
    appeared = text.count(word)

    if appeared != -1:
        print("your word appeared in text",appeared,'Times!')
    else:
        print('your word has not been apeared in your text')

text = "the thing is that the Eminemce in shadow is the best anime in the world! isekai prob"
word = input("Enter character to be found: ")
count(text,word)
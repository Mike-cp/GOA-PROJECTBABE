def indexer(text,word):
    index = text.index("Hello")

    if index != -1:
        print("the index is provided ",index)
    else:
        print("The index could not be found! PLEASE TRY AGAIN")

text = "Hellow world! and hi everyone Hello!"
word = input("Enter your index that has to be found!:  ")
indexer(text,word)

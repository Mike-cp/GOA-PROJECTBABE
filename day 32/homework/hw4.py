def insert_word(sentence, word, index):
    words = sentence.split()
    words.insert(index, word)
    
    return ' '.join(words)


sentence = input("Enter a sentence: ")
word = input("Enter a word to insert: ")
index = int(input("Enter the index where the word should be inserted: "))

print(insert_word(sentence, word, index))

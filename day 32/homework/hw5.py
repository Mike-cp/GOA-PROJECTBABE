def sentence_to_words(sentence):
    return sentence.split()


sentence = input("Enter a sentence: ")
words_list = sentence_to_words(sentence)
print(words_list)

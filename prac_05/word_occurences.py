WORD_OCCURENCES = {}

sentence = input("Text : ")
words = sentence.split()
for word in words:
    frequency = WORD_OCCURENCES.get(word, 0)
    WORD_OCCURENCES[word] = frequency + 1

words = list(WORD_OCCURENCES.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, WORD_OCCURENCES[word]))


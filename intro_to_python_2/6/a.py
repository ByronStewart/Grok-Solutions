# create a dictionary with the key as english word and value as indigenous word
dictionary = {}
with open('dictionary.txt') as file:
    for line in file:
        # split the string on the comma, english will be index 0 and indigenous index 1
        # we need to strip first to remove whitespace and newlines
        words = line.strip().split(',')
        english_word = words[0]
        indigenous_word = words[1]

        # check to ensure the key is not already there
        if not english_word in dictionary:
            dictionary[english_word] = indigenous_word


# now we have our dictionary to use, create the translator
# input an english sentence
english_sentence = input("English: ")

while english_sentence != "":

    # create a list to build the indigenous sentence with
    indigenous_sentence = []

    # split the sentence and look up each word in the dictionary, appending to the indigenous list
    for word in english_sentence.split():
        # if the word is not in the dictionary just provide None
        i_word = dictionary.get(word, None)
        indigenous_sentence.append(i_word)

    # convert the list to string separated on space and
    # print the indigenous sentence
    print(" ".join(indigenous_sentence))

    # ask the user for another sentence
    english_sentence = input("English: ")

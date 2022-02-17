# create a list to store the words
words = []

# ask the user for a word
word = input("Word: ")

# break the loop on an empty string input
while word != "":
    # check to see if the new word is already in the list
    if word not in words:
        # if not we will add it to the list
        words.append(word)
    # else do not add the word

    # ask the user for a word
    word = input("Word: ")

# the number of unique words must be the length of words because we did not add the duplicates in
total_unique_words = len(words)
# print out the answer message
print("You know", total_unique_words, "unique word(s)!")

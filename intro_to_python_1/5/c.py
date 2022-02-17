# ask the user for a sentence
sentence = input("Line: ")

# initialize the backwards text to an empty string
backwards_sentence = ""

# calculate the length of the sentence
sentence_length = len(sentence)

# loop from the end of the sentence to the start
for idx in range(sentence_length - 1, -1, -1):
    # find the character at the index
    char = sentence[idx]

    # add the char to the backwards sentence
    backwards_sentence = backwards_sentence + char

# print the backwards sentence
print(backwards_sentence)

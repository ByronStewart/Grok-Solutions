# a dictionary to hold the bigrams as keys and the counts as values
bigram_counts = {}

# ask the user for a sentence
sentence = input("Line: ")

# repeat so long as sentence is not empty
while sentence != "":
    # convert to a list of the words
    sentence = sentence.split()
    # loop from the start of the sentence to the second last word
    # it must be the second last word because we will use i and i+1 in loop
    for i in range(0, len(sentence) - 1):
        # create the bigram string from word at i and i + 1 converting each to lowercase
        bigram = sentence[i].lower() + " " + sentence[i+1].lower()

        # check if the bigram in the dictionary
        if bigram in bigram_counts:
            # increment by 1
            bigram_counts[bigram] += 1
        else:  # set to 1
            bigram_counts[bigram] = 1

    # ask the user for another sentence
    sentence = input("Line: ")

# loop through the dictionary
for name, count in bigram_counts.items():
    # only want to print if count > 1
    if count > 1:
        print(f"{name}: {count}")

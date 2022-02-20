# create a dictionary of words,
# the key will be the word
# and the value will be the number of times it has been seen
word_counts = {}

# ask the user for a line
line = input("Enter line: ")

# so long as line is not an empty string repeat
while line != "":
    # create a list of words from the line
    line = line.split()
    # loop through the words
    for word in line:
        # check if the word is in the dictionary,
        # if it is then we increase the value by 1
        # if not we will add it and set the value as 1
        if word_counts.get(word):
            # it does exist so increment counter by 1
            word_counts[word] += 1
        else:
            # it does not, assign it to 1
            word_counts[word] = 1

    # ask the user for another line because we are not done
    line = input("Enter line: ")

# now that we have the words and counts
# we have to display in alphabetical order based on the word (key)
# so we make a list of the words to lookup the keys in
word_list = sorted(word_counts)

# loop through and print out the results
for word in word_list:
    # notice we refer to word_counts and not word_list to find the count
    print(word, word_counts[word])

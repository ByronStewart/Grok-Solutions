# dictionary will hold the names as key and the count as values
counts = {}

# get the word counts from the file
with open("novel.txt") as file:
    # loop over each line
    for line in file:
        # split the line into a list of words
        line = line.split()
        for word in line:
            # check if the word starts with an uppercase
            if word[0].isupper():
                # check if word in dictionary
                if word in counts:
                    # increment the count
                    counts[word] += 1
                else:
                    # set the count to 1
                    counts[word] = 1
            # if it isnt capitalised do nothing

# we need to sort based on the count to get the top 3 results

# create a list to store the key value pairs in the dictionary
# it is important to have the tuple as count first for the sort function or it will sort by the word
by_count = [(count, word) for word, count in counts.items()]

# sort the list in descending order
by_count.sort(reverse=True)


# print the top 3
for count, word in by_count[:3]:
    print(count, word)

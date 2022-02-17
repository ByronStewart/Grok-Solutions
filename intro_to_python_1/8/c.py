# ask the user for the code
coded_message = input('code: ')

# change the string to a list separated on space
coded_message = coded_message.split()

# reverse the order of the list
coded_message.reverse()

# create a list to store the decoded message
decoded_message = []

# loop through the coded message
for word in coded_message:
    # check that the word starts with a capital letter
    if word[0].isupper():
        # if it does it needs to be appended to the decoded message list
        # convert it to lower case
        word = word.lower()
        # append it
        decoded_message.append(word)

    # else do not include it

# create the message to read to the user
# this will put a space between each word and concatenate them to a string
message = "says: " + " ".join(decoded_message)

print(message)

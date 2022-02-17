# ask the user for a coded message
coded_message = input("Message? ")

# calculate the length of the message
length = len(coded_message)

# initialise the decoded message with the first character of the coded message
# eg. if coded message is "abc", decoded message is now "a"
decoded_message = coded_message[0]

# loop from 3 to the end of the message increasing by 3 each time
# i will be 3, 6, 9, ...
for i in range(3, length, 3):
    # get the char at index i
    char = coded_message[i]
    # add a space and then the char to the decoded message
    decoded_message = decoded_message + " " + char

# print the decoded message
print(decoded_message)

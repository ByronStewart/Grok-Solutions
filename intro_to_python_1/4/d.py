# ask the user for their name
name = input('Enter your name: ')

# compute the length of the name
length = len(name)

# create the message start
message_start = "Hi "

# initialise the message end to an empty string which we will fill depending on the length of the name
message_end = ""

# check the length
if length <= 3:
    # name is short
    # create the short message
    message_end = ", you have a short name."

elif length <= 8:
    # medium length name
    # create the medium length message
    message_end = ", nice to meet you."

else:
    # long length name
    # create the long length message
    message_end = ", you have a long name."

# join the messages together
message = message_start + name + message_end

# print the message
print(message)

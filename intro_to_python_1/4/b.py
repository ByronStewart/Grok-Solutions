# ask the user for a sentence
loud_sentence = input("Loud: ")

# convert the sentence to lower case letters
soft_sentence = loud_sentence.lower()

# create the start of the message
message_start = "Quiet: "

# concatenate the message start with the soft sentence
message = message_start + soft_sentence

# print the soft sentence
print(message)

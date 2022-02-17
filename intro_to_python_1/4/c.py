text = input("What did she say? ")

# replace the ### with o
text = text.replace("###", "o")

# replace the ## with e
text = text.replace("##", "e")

# replace the %% with a
text = text.replace("%%", "a")

# create the message starter
message_start = "She meant to say: "

# create the message
message = message_start + text

# print the message
print(message)

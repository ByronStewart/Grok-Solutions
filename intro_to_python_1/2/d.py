# get the text from the user and store it in a variable
text = input("What do you want me to say? ")

# get the user to say how many times it should be said
number = input("How many times do you want me to say it? ")

# convert the number to an integer
number = int(number)

# multiply the text by the number stated by the user
text = text * number

# print the result
print(text)

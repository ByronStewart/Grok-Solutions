# ask the user for a cheer
cheer = input("Cheer: ")

# loop through the characters in the cheer
for char in cheer:
    # create the message
    message = "Give me a " + char + ", " + char + "!"
    # print the message
    print(message)

# print the inbetween messsage
print("What does it spell?")

# convert the cheer to uppercase
loud_cheer = cheer.upper()

# print the loud cheer
print(loud_cheer)

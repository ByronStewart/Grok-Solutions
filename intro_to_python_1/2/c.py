# get the number from the user
n = input("Enter a number: ")

# convert the input to an integer
n = int(n)

# create a variable to hold the ends of the string
end = "^"

# create the underscore variable
underscore = "_"

# multiply the underscore by the amount which the user input
underscores = underscore * n

# create the message to print to the screen
message = end + underscores + end

# print the message to the user
print(message)

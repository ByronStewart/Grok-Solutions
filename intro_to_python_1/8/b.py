# ask the user for the colours of cars
colours = input("Cars: ")

# change the string to a list separated by space
colours = colours.split()

# initialise a total for red and blue
total_red = 0
total_blue = 0

# loop through the colours list and increment the total red or blue when we see that colour
for word in colours:
    if word == 'red':
        total_red += 1

    if word == 'blue':
        total_blue += 1


# print the red car message
print("red:", total_red)


# print the blue car message
print('blue:', total_blue)

# create a dictionary to map the name to the colour
# key is name, value is colour
favourites = {}

# ask the user for a name colour pair till they provide an empty string
name_colour = input("Name and colour: ")
while name_colour != "":
    # split the string on space
    name_colour = name_colour.split()
    # store the name which is first and colour which is second in the dictionary
    name = name_colour[0]
    colour = name_colour[1]
    favourites[name] = colour

    # ask the user for more name colours
    name_colour = input("Name and colour: ")

# loop through the entries and print out each pair
for name, colour in favourites.items():
    print(name, colour)

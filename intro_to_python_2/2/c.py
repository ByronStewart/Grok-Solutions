# this dictionary will hold the colour as the key and the count as the value
car_counts = {}

colour = input("Car: ")
while colour != "":
    # we have to check if it exists because incrementing the value requires
    # there to be a value there already
    if colour not in car_counts:
        # does not exist so set to 1
        car_counts[colour] = 1
    else:
        # does exist so increase by 1
        car_counts[colour] += 1

    colour = input("Car: ")

# loop through each item in the dictionary printing its key and value
# note they may be in different order each time this is run
for colour, count in car_counts.items():
    print(f"Cars that are {colour}: {count}")

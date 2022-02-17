# ask the user for the rainy days
# expect a list of days eg. Monday Tuesday Wednesday
rainy_days = input("Which days had rain? ")

# split the string into a list, separated by a space
# it cannot be rainy_days.split(" ") because an input of "" would result in [""] which has length one
rainy_days = rainy_days.split()

# calculate how many elements in the list
number_of_rainy_days = len(rainy_days)

# there are 7 days in a week so there must be 7 - rainy days worth of sunny days.
number_of_sunny_days = 7 - number_of_rainy_days

# print the message and the number of rainy days
print("Number of days without rain:", number_of_sunny_days)

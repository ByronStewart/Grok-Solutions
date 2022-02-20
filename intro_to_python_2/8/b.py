# create 2 dictionaries to store the counts of packages and letters, both will have the name as the key
# use the defaultdict from the collections libary to initialise all values as 0
from collections import defaultdict

letter_counts = defaultdict(int)
package_counts = defaultdict(int)

# open the file
with open('mail.txt') as file:
    # loop through the lines and add each to the respective dictionary
    for line in file:
        # strip trailing whitespace and new lines and separate on the comma
        # name will be first and the type of delivery will be second
        line = line.strip().split(',')
        name = line[0]
        item = line[1]

        # increment the count for either the letter or package for the respective name
        if item == 'Package':
            package_counts[name] += 1
        else:  # must be a letter
            letter_counts[name] += 1

# ask the user for the name
name = input("Name: ")
# lookup the name, if not found return 0
num_letters = letter_counts.get(name, 0)
num_packages = package_counts.get(name, 0)
# print the respective messages
# 1st case there is 0 of each
if num_letters + num_packages == 0:
    print("No mail")
else:  # there must be at least a letter or package
    # letters message first
    if num_letters > 1:
        # plural
        print(f"{num_letters} Letters")
    elif num_letters == 1:
        # singular
        print(f"{num_letters} Letter")
    else:  # no letters
        print("No Letters")

    # package message second same logic as letters
    if num_packages > 1:
        print(f"{num_packages} Packages")
    elif num_packages == 1:
        print(f"{num_packages} Package")
    else:
        print("No Packages")

# this strange looking with statement ensures our program does not have a memory leak.
# the functionality is the same as file = open("orders.txt") but it will automatically close the file
with open("orders.txt") as file:
    # loop through the file
    for line in file:
        # print the line in uppercase
        # we need end="" to stop it printing a new line in between each line
        print(line.upper(), end="")

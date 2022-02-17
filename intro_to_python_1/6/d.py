# get a list of costs from the user
costs = input("Enter the expenses: ")

# convert the string into a list
costs = costs.split()

# initialise a total to 0
total = 0

# loop through each cost in the list:
for cost in costs:
    # convert each string in the list into a number
    # eg if input was 12 23, the list of costs would be ['12', '23']
    cost = int(cost)

    # add the cost to the total
    total += cost

# create the message to print
# we must convert total back to a string to join it to the message
message = "Total: $" + str(total)

# print the message
print(message)

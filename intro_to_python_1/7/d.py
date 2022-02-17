# ask the user for the number of steps
number_of_steps = input("How many steps? ")

# convert the string to an int
number_of_steps = int(number_of_steps)

# print the top of the stairs
print("__")

# initialise the current step to be printed as 1
current_step = 1

# loop while the current step is less than the number of steps
while current_step < number_of_steps:
    # there is two spaces for each level on the staircase
    spaces = "  "
    # multiply the spaces by the current_step to get the correct amount
    spaces = spaces * current_step
    # each step finishes with |_
    stair = spaces + "|_"

    # print the step
    print(stair)

    # increase the current_step by 1
    current_step += 1

# the last level is a special case where there are no spaces and only underscores
# there are 2 underscores for each level of step
underscores = "__"
# multiply the underscores by the current_step to get the correct amount
underscores = underscores * current_step
# bottom stair ends with |
bottom_stair = underscores + "|"
# print bottom stair
print(bottom_stair)

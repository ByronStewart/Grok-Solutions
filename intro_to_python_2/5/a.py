# ask the user for the size and convert to integer
size = int(input("Grid size: "))

# create the grid full of .
# it will be a list of lists of length which the user input
grid = [["." for _ in range(size)] for _ in range(size)]
# set the first to an x
grid[0][0] = 'x'
# track the player location in x and y coordinates
# note that we start in top left at 0, 0
x = 0
y = 0

# print the grid
for row in grid:
    for cell in row:
        # print the contents of each cell next to each other
        print(cell, end="")
    # print a new line after each row
    print()

# ask for a direction
# can expect direction to be 'up', 'down', 'left' or 'right'
direction = input("Direction: ")

while direction != "":
    # <extension> create a check that the direction is valid

    # update the location based on the direction
    # increment or decrement the relevant x or y coordinate
    if direction == 'up':
        y -= 1
    elif direction == 'down':
        y += 1
    elif direction == 'left':
        x -= 1
    elif direction == 'right':
        x += 1

    # update the grid to reflect the location of the player
    grid[y][x] = 'x'

    # print the grid
    for row in grid:
        for cell in row:
            # print the contents of each cell next to each other
            print(cell, end="")
        # print a new line after each row
        print()

    # ask the user for a new direction
    direction = input("Direction: ")

# create a set to store the co-ordinates
already_hit_squares = set()

# expect the input to be of type 'A1' etc
square = input("Guess: ")

while square != "":
    # check if the square is already hit
    if square in already_hit_squares:
        # if it has then print the error message
        print("You've chosen that square already")
    else:
        # if not then add it to the set of already hit squares
        already_hit_squares.add(square)
        # print success message
        print(f"Hit {square}")

    # ask the user for another square
    square = input("Guess: ")

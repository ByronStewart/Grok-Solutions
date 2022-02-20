# print the opening line
print("What is my favourite food?")

# ask the user for a guess
guess = input("Guess? ")

# we check to see if the guess is correct, if it is we break out of the loop
# or we will keep retrying the guess
while guess != 'electricity':
    # print the result of the guess
    print("Not even close.")
    # ask the user for another guess,
    # important, reassign the variable guess to the new input
    guess = input("Guess? ")

# if we break out of the loop then we have guessed it
print("You guessed it! Buzzzz")

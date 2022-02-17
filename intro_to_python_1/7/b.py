# print the opening message
print("What is my favourite food?")

# initialise the favourite as electricity
favourite = "electricity"

# ask the user for their initial guess
guess = input("Guess? ")

# loop while the guess is not equal to the favourite
while guess != favourite:

    # print the failure message
    print("Not even close.")

    # ask the user to guess again
    guess = input("Guess? ")

# if we have made it to here then the guess must be correct so print success message
print("You guessed it! Buzzzz")

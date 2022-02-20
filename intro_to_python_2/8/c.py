# track the number of guesses remaining
guesses_remaining = 10
# track the number of mistakes remaining
mistakes_remaining = 1
# variable to store correct guess
correct_guess = 42

# repeat forever, we will check break conditions inside the loop
while True:
    # ask for a guess and cast to integer
    guess = int(input("Guess a multiple of 7: "))

    # check to see if the guess is correct
    if guess == correct_guess:
        print("You won!")
        # break out of the loop
        break

    # check that the guess is a multiple of 7
    # the % operator takes the remainder after division, if it is a multiple then the remainder will be 0
    elif guess % 7 == 0:
        print("Nope!")

    # if we fail the first 2 conditions it must be a mistake
    # so we will check the mistakes remaining to see what to do
    elif mistakes_remaining == 0:
        # game over, too many mistakes
        print('Another mistake. Too bad.')
        break
    else:  # we have a mistake left so it is not game over
        print("Mistake! That number isn't a multiple of 7.")
        mistakes_remaining -= 1

    # we have made a guess in all cases so decrement the number of guesses remaining
    guesses_remaining -= 1

    # check if we have used up all our guesses
    if guesses_remaining == 0:
        print('No guesses left!')
        break

# outside of loop so game ends and we print end message
print("That was fun.")

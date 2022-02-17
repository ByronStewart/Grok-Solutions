# ask the user for the two words
words = input("Enter words: ")

# convert the string words to a list separated on a space
words = words.split()

# put the first and second words in their own variable
first_word = words[0]
second_word = words[1]

# both words must have the same letters to be an anagram
# make a list of the characters in each word and sort them
first_letters = list(first_word)
first_letters.sort()

second_letters = list(second_word)
second_letters.sort()


# if they are the same string when sorted they must have the same letters
if first_letters == second_letters:

    # now we need to check if the first and last letters of the word are the same
    if first_word[0] == second_word[0] and first_word[-1] == second_word[-1]:
        # here we know that all the letters are the same and the first and last letters are also the same
        # so we have a super anagram
        print("Super Anagram!")
    else:
        # failed the second check
        print("Huh?")


else:  # failed the first check
    print("Huh?")

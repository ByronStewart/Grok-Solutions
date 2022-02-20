# scores will hold the letter as the key and the score as the value
scores = {}

# collect the scores from the file
with open("scrabble_letters.txt") as file:
    for line in file:
        # strip and split on space to create list of word with score
        score_and_word = line.strip().split()
        score = score_and_word[0]

        # score is currently a string so it must be cast to an integer
        score = int(score)
        word = score_and_word[1]

        # add to the dictionary
        scores[word] = score

# get a word from the user
word = input("Word: ")

# create a variable to hold the total score
total = 0
# loop through each character in the word and lookup its score in the dictionary
for char in word:
    # dictionary is all uppercase so we must convert to uppercase
    char = char.upper()
    # increment the total by the character score
    total += scores[char]

# print out the total score message
print(total, "points")

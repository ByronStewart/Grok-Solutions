# A dictionary containing the letter to digit phone keypad mappings.
KEYPAD = {
    'A': '2', 'B': '2', 'C': '2', 'D': '3', 'E': '3',
    'F': '3', 'G': '4', 'H': '4', 'I': '4', 'J': '5',
    'K': '5', 'L': '5', 'M': '6', 'N': '6', 'O': '6',
    'P': '7', 'Q': '7', 'R': '7', 'S': '7', 'T': '8',
    'U': '8', 'V': '8', 'W': '9', 'X': '9', 'Y': '9',
    'Z': '9',
}
# ask the user for a word
word = input("Enter word: ")
# convert the word to uppercase so we can lookup the number
word = word.upper()

# initialise the message with an empty string
numbers = ""

# loop through each character in the word
for char in word:
    # look up the character in the dictionary
    # note that number in the dictionary is stored as a string
    number = KEYPAD[char]
    # append the number to the numbers string
    numbers += number

# print the result
print(numbers)

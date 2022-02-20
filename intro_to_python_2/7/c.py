# dictionary to map the word to the number word is key, number is value
replacements = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}


def words2number(string):
    # split the string on space
    string = string.split()

    # the answer will initially be a string so we can concatenate each digit,
    # we will convert back to an int before returning
    answer = ""
    for word in string:
        number = replacements[word]
        # concatenate the string version of the number
        answer += str(number)

    # return the int version of the number
    return int(answer)

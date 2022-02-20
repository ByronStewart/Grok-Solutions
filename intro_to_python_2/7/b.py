# a dictionary to hold the replacements the key is the english word and the value is the chef word
replacements = {
    'tion': 'shun',
    'an': 'un',
    'v': 'f',
    'w': 'v',
    'o': 'oo',
    'th': 'z',
    'i': 'ee',
    'c': 'k',
}


def eng2chef(string):
    # loop through the replacements dictionary and replace the english part with the chef part
    for english, chef in replacements.items():
        string = string.replace(english, chef)
    # check if it ends with an exclamation point
    if string.endswith('!'):
        # replace the ! with the other message
        string = string[:-1] + '. bork bork bork!!'
    return string

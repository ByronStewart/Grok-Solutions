# dictionary to map the replacements neccesary
replacements = {
    'y': 'z',
    'z': 'y',
    'Y': 'Z',
    'Z': 'Y',
}


def fix_yz(string):
    # will create a new string to return and build by looping through original string
    fixed = ""
    # loop through each char in the string and replace if needed
    for char in string:
        # check if the character needs to be replaced and replace with the correct letter if it does
        if char in replacements.keys():
            fixed += replacements[char]
        else:  # else just copy from the original string
            fixed += char
    return fixed

# open the file
with open("input.txt") as file:
    # each line must have the letters "aardvark" anywhere in the line to be an ardvark
    # so must have 3 a's, 2 r's etc.
    # we have to keep track of the line number so we use enumerate(file) here
    for line_number, line in enumerate(file):

        # we will create a list of the letters required and remove them as we loop through characters in the line
        # if we are able to remove all letters then we can say there is an ardvark
        letters = list('aardvark')
        # we need all letters to be lowercase
        for char in line.lower():

            if char in letters:
                letters.remove(char)

        if len(letters) == 0:
            # the answer is expecting the index to start as 1 so we need to add 1 here
            print('Aardvark on line', line_number + 1)

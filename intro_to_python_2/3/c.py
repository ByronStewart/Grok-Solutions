# ask the user for a word to look for
# expect the word to be in lowercase
query = input("Word to look for: ")

# set a variable to track if the query is found; false by default
is_query_found = False
# open the file
with open("book.txt") as file:
    # loop through each line
    for line in file:
        # convert the line to lowercase
        line = line.lower()
        # split the line to a list separated on space to ensure we don't match inner parts of words
        line = line.split()
        # check if the line contains the query
        if query in line:
            # set query found to true
            is_query_found = True
            # break out of the loop because we no longer need to do any more checking
            break

# check if the query was found and print the corresponding message
if is_query_found:
    # equivalent to is_query_found == True
    print(f"{query} was found in the book.")
else:
    print(f"{query} was not found in the book.")

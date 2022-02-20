# have a set of usernames to track unique usernames
usernames = set()
# read the file and print usernames as we go
with open('classlist.txt') as file:
    for name in file:
        # strip any whitespace or newlines, convert to lowercase and convert to list separated on whitespace
        names = name.strip().lower().split()

        # first choice is the first and middle names
        username = "".join(names[:-1])
        # check and add if it does not exist
        if not username in usernames:
            usernames.add(username)
            print(username)
            # disregard any code further and continue the loop
            continue

        # if the username exists go to the next criteria
        # append the first char of the last name
        username += names[-1][0]
        # check and add if it does not exist
        if not username in usernames:
            usernames.add(username)
            print(username)
            # disregard any code further and continue the loop
            continue

        # if this exists we will try numbers starting at one and incrementing from there
        # create an infinite loop which we will break out of on success
        counter = 1
        while True:
            # create a new variable for the username so we can reuse the old one
            # concat the counter cast to a string to the username
            potential_username = username + str(counter)
            # check and add if it does not exist
            if not potential_username in usernames:
                usernames.add(potential_username)
                print(potential_username)
                # break out of the loop
                break
            # increment the counter
            counter += 1

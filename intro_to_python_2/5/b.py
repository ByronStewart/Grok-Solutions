# votes will hold the dessert as a key and a list of names as the value
# this will ensure we keep the order of the votes and the names as they come in
# the number of votes will be the length of the names list
# example: votes = { 'ice-cream' : ['alice', bob'] }
votes = {}

name_vote = input("Name:vote ")

while name_vote != "":

    # split on the colon to separate the dessert and name
    name_vote = name_vote.split(":")
    # name comes first and dessert comes second
    name = name_vote[0]
    dessert = name_vote[1]

    # check if dessert exists in dictionary
    if dessert in votes:
        # add the name to the list
        votes[dessert].append(name)
    else:
        # create a list with the name
        votes[dessert] = [name]

    # ask the user for another vote
    name_vote = input("Name:vote ")

# print the results
for dessert, names in votes.items():
    # convert the names to a space separated string
    printable_names = " ".join(names)
    # print the formated message
    print(f"{dessert} {len(names)} vote(s): {printable_names}")

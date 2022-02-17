# ask the user if it is currently raining
# the program only expects "Yes" or "No" responses
is_raining = input("Is it currently raining? ")


# The first step in this decision is based on the weather.
# check if it is raining
if is_raining == "No":
    # if it is not raining then we need to know how far to travel

    # ask the user how far to travel
    distance_to_travel = input("How far in km do you need to travel? ")

    # convert the distance to an integer
    distance_to_travel = int(distance_to_travel)

    # check the distance travelled
    if distance_to_travel > 10:
        # take the bus when > 10
        print("You should take the bus.")

    elif distance_to_travel > 2:
        # ride the bike if greater than 2 and less than 10
        print("You should ride your bike.")

    else:
        # walk in all other cases
        print("You should walk.")

else:
    # it is raining you should take the bus
    print("You should take the bus.")

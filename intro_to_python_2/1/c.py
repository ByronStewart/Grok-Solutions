# ask the user for the current floor
current_floor = input("Current floor: ")
# convert to an integer
current_floor = int(current_floor)

# ask the user for their destination floor
destination_floor = input("Destination floor: ")
# convert to an integer
destination_floor = int(destination_floor)

# loop till the destination floor is the same as the current floor
# increase the current floor by 1 each round
while current_floor <= destination_floor:
    # print the message
    print("Level", current_floor)

    # increase the current floor by 1
    current_floor += 1

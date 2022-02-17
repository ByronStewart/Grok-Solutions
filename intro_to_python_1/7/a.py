# ask the user for the time to launch
time = input("Time to launch: ")

# convert the time to an integer
time = int(time)

# print starting message
print("Counting down ...")

# loop over and over decreasing time by 1 each pass till it reaches 0
while time > 0:
    # print the message
    print(time, "...")
    time = time - 1

# print the final message
print("Lift Off!")

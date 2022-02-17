# ask the user for a number
number = input('Enter a number: ')

# convert the number to an integer
number = int(number)

# loop from 1 to the number input by the user
for i in range(1, number + 1):
    # i will be 1, 2, 3, 4, ..., number
    # print i
    print(i)

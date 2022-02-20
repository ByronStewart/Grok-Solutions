# ask the user for the two numbers
x = input("Number 1: ")
y = input("Number 2: ")

# convert from string to integer
x = int(x)
y = int(y)


# print in the required format using fstring, plus is +, times is *
print(f"{x} plus {y} is {x + y}")
print(f"{x} times {y} is {x * y}")

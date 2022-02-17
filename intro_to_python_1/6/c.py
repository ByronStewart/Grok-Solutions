# ask the user for a list of students
students = input("Students: ")

# convert the string to a list separated on a space
students = students.split()

# sort the students in ascending order
students.sort()

# print the opening message
print("Class Roll")

# loop through each word in the list
for name in students:
    # print the name
    print(name)

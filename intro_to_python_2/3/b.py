# open both the write file and the read file
# the with statements must be nested so that both files are open at the same time
with open("letter.txt") as in_file:
    with open("fixed.txt", "w") as out_file:
        # loop through the lines
        for line in in_file:
            # check the first 5 characters in the line to see if it is "WOOF!"
            if line[0:5] != "WOOF!":
                # if it is not then we write the line to the out_file
                out_file.write(line)

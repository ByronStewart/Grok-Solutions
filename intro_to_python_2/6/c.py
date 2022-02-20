# import the csv library to use the csv reader
import csv

# ask for the title
title = input("Winning title: ")

# read the csv file
with open("nominees.csv", newline="") as file:
    # use the dictionary csv reader for ease of use
    # each cell of the row will be indexed by its heading
    for movie in csv.DictReader(file):
        if movie['title'] == title:
            # if the title is what was input we have found the movie we are looking for
            # print the congratulations message using the director
            director = movie['director(s)']
            print(f'Congratulations: {director}')
            # we are done so break out of the loop
            break

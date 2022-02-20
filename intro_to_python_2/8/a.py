# store the songs in a list
songs = []
with open('songlist.txt') as file:
    for line in file:
        songs.append(line.strip())

# ask the user how many more songs
num_songs_left = int(input("How many more songs? "))

for i in range(num_songs_left):
    # look up the list from the end
    # we have to add 1 to i because we want 0 to map to -1, 1 to -2, 2 to -3 and so on
    # print the song
    print(songs[-(i+1)])

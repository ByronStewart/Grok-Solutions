# we will use the punctuation helper from the string library to remove punctuation
from string import punctuation
# we will use a defaultdict from the collections libary for convenience
from collections import defaultdict

# save the count of hashtags in a dictionary, tag is key and count is value
counts = defaultdict(int)

# repeat and break on empty string
while True:
    tweet = input("Tweet: ")
    if tweet == "":
        break

    # split the tweet on space
    tweet = tweet.split()
    # loop over the words
    for word in tweet:
        # check that it starts with a #
        if word[0] == "#":
            # strip all punctuation from the right (not left so we keep the #) and convert to lowercase
            hashtag = word.lower().rstrip(punctuation)
            # add the hashtag to the dictionary or increase the count
            counts[hashtag] += 1


# print the results
for hashtag, count in counts.items():
    print(hashtag, count)

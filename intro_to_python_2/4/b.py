# create sets to hold the english and french words
# use sets because they do not allow for duplicates
english_words = set()
french_words = set()

with open("english.txt") as english:
    # the file has each word on a new line
    for word in english:
        # use strip() to remove any punctuation or line breaks
        english_words.add(word.strip())

with open("french.txt") as french:
    # the file has each word on a new line
    for word in french:
        # use strip() to remove any punctuation or line breaks
        french_words.add(word.strip())

# the common words will be the intersection of the two sets
common_words = english_words & french_words

# print the words
for word in common_words:
    print(word)

# ask the user for a sentence
sentence = input("Line: ")

# split the sentence into a list of words
words = sentence.split()
# split the sentence again to a lowercase version to use to check for rObOT cases
lower_words = sentence.lower().split()

# check if lowercase robot in words
if 'robot' in words:
    print('There is a small robot in the line.')

# check if uppercase robot in words
elif 'ROBOT' in words:
    print("There is a big robot in the line.")

# check if combination of of uppercase and lowercase in words
elif 'robot' in lower_words:
    print('There is a medium sized robot in the line.')

# all other cases
else:
    print("No robots here.")

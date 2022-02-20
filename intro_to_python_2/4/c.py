# we only have to consider english and other languages
# because the requirements state all users will speak english
english_speaking_names = set()
other_speaking_names = set()


# expect the input to be in the following order:
# language name name name...
language_followed_by_names = input("Line: ")

while language_followed_by_names != "":
    # convert to a list
    language_followed_by_names = language_followed_by_names.split()

    # first item is language
    language = language_followed_by_names[0]
    # names will be the slice from 1 to end
    names = language_followed_by_names[1:]

    # if the language is english add the names to english set; else other
    if language == 'English':
        for name in names:
            english_speaking_names.add(name)
    else:  # language not english
        for name in names:
            other_speaking_names.add(name)

    # ask for a new input
    language_followed_by_names = input("Line: ")

# the monolingual people will the difference between the two sets because everyone has to speak english
monolingual = english_speaking_names - other_speaking_names

# if there are any monolingual people then print them out; else print failure message
if len(monolingual) > 0:
    for name in monolingual:
        print(f"{name} is monolingual.")
else:  # no monolingual people
    print("Everyone is multilingual!")

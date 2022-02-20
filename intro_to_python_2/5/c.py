# create a dictionary of rules to hold the tuple of combinations as a key and the message as the value
# if the combination does not exist in the rules dictionary it is a tie
rules = {
    ('scissors', 'paper'): 'Scissors cut Paper',
    ('paper', 'rock'): 'Paper covers Rock',
    ('rock', 'lizard'): 'Rock crushes Lizard',
    ('lizard', 'spock'): 'Lizard poisons Spock',
    ('spock', 'scissors'): 'Spock melts Scissors',
    ('scissors', 'lizard'): 'Scissors decapitate Lizard',
    ('lizard', 'paper'): 'Lizard eats Paper',
    ('paper', 'spock'): 'Paper disproves Spock',
    ('spock', 'rock'): 'Spock vaporizes Rock',
    ('rock', 'scissors'): 'Rock breaks Scissors'
}

# ask the user for hand 1 and hand 2
hand1 = input('Hand 1: ')
hand2 = input('Hand 2: ')

# check the rules to see if hand1 and hand2 are in there if it does not exist then will be none
# must check both combinations
left = rules.get((hand1, hand2), None)
right = rules.get((hand2, hand1), None)

# if both return none then it must be a tie
if left == None and right == None:
    print("Tie")

# only one be the message so we can simply do an else if
elif left == None:
    print(right)
else:  # right == None
    print(left)

import random as rnd


class Player:

    def __init__(self, id_in_group):
        self.id_in_group = id_in_group
        self.contribution = rnd.randint(1, 100)
        self.payoff = 0
        self.treatment = None
        self.party = None

    def print_party(self):
        print(self.party)


NUM_PLAYERS = 4
ENDOWMENT = 100
MULTIPLIER = 2
TREATMENTS = ['C', 'T1']
PARTIES = ['Republicans', 'Democrats']
players = [Player(id_in_group=n) for n in range(1, NUM_PLAYERS + 1)]
rnd.shuffle(players)

# Exercise 0
# Loop through all the players and print their id_in_group
#for n in range(0, NUM_PLAYERS):
    #print(f'player{n}',player.id_in_group)

# Exercise 1
# Assign the treatment 'C' to players with an odd id_in_group

# Exercise 2
# Assign the treatment 'T' to players with an even id_in_group

for player in players:
    if player.id_in_group in range(1,NUM_PLAYERS+1,2):
        player.treatment = TREATMENTS[ 0 ]
    else:
        player.treatment = TREATMENTS[ 1 ]

    print( f'player{player.id_in_group}',player.id_in_group, player.treatment)

# Exercise 3
# Assign each party in the variable PARTIES to an equal number of players.
# NB: each player must have a party assigned.
for player in players:
    if player.id_in_group in range(1,3):
        player.party = PARTIES[ 0 ]
    else:
        player.party = PARTIES[ 1 ]

    print( f'player{player.id_in_group}',player.id_in_group, player.treatment, player.party)

 player.party
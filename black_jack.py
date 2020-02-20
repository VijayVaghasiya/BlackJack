
'''
Black Jack Casino Game : American Version
'''

# importing modules
import itertools, random

class GameDealer():

    def __init__(self,deck,card):
        self.deck = deck
        self.card = card
           
    def __list__(self):
        pass
    
    def deal_cards(self,player):
        '''
        Dealer Deals the card from Shuffled deck
        
        '''
        self.card = self.deck.pop()
        player["cards"].append(self.card)

    def shuffle_card(self):
        '''
        Create new deck of card and give random shuffle.
        This method must be called only once during start of the game.
        '''
        # make a deck of cards
        self.deck = list(itertools.product(range(1,14),['♠','♥','♦','♣']))

        # shuffle the cards
        random.shuffle(self.deck)

    def dealer_bust(self):
        pass



class GamePlayers(object):
    def __init__(self):
        pass
        
    def __str__(self):
        pass 
    
    def buy_chips(self, player):
        player["balance"] += int(input(f'{player["name"]} >>> How many chips do you want (min:100 max:500) : '))
        
        
    #def buy_again(self,stat):
     #   stat[1] += int(input(f"Player {stat[0]} >>> How many chips do you want (min:100 max:500) : "))
     #   return stat

    def player_stats(self,player):
        print("\n")
        print(f'{player["name"]} :')
        print('----------')
        print(f'balance : {player["balance"]}')
        print(f'cards : {player["cards"]}')
        
        
    def bet(self,player):
        player["bet"] = int(input(f'{player["name"]}, how much do you want to bet : '))
        player["balance"] -= player["bet"]     
    
    def stand(self):
        pass

    def hit(self):
        pass

    def split(self):
        pass

    def surrender(self,player):
        
        pass

    def doubling_down(self):
        pass

    def insurance(self):
        pass
        
# player_count = int(input("Enter number of player (max 6) : "))
    
    
# while player_count not in range(1,7):
#     player_count = int(input("That was wrong number (enter between 1 to 6). Try again : "))
    
# # Create an list based instance of class Game Player    
# all_players = GamePlayers(list([["Player "+str(i), 0] for i in range(1,player_count+1)]))
    
# all_players.buy_chips()
# all_players.chip_summary()
#     # Buy chips from Dealer. Each player starts with 0 chips
#    # for player in all_players:

while True:
    try:
        player_count = int(input("Enter number of player (max 6) : "))
        if player_count not in range(1,7):
            continue
    except ValueError:
        print('That was incorrect choice. Try again')
        continue
    else:
        break        
        
        
all_player_stats = []

# Create an list based instance of class Game Player

player = GamePlayers()
dealer = GameDealer([],())

#player_status = ['busted','stand','hit',"surrender","insurance"]

dealer.shuffle_card()

for i in range(0,player_count):
    all_player_stats.append({"name": "Player "+ str(i+1), "balance" : 0, "bet" : 0, "cards":[],"status" : ""})
    player.buy_chips(all_player_stats[i])
    player.bet(all_player_stats[i])

all_player_stats.append({"name": "Dealer", "balance" : None, "cards":[],"status" : ""})

for j in range(2):
    for k in range(0,player_count+1):
        dealer.deal_cards(all_player_stats[k])

for i in range(0,player_count+1):
    player.player_stats(all_player_stats[i])
    
#     decision = int(input(f'player["name"] make your decision :' ))
#     print('1 : stand\n2 : hit\n3 : split\n4 : surrender\n5 : insurance')
#     while decision not in range(1,6):
#         int(input(f'It was incorrect choice. {player["name"]} make your decision :' ))
    
    #decision = 0
    while True:
        try:
            decision = int(input(f'player["name"] make your decision :' ))
            if decision not in range(1,6):
                continue
        except ValueError:
            print('It was incorrect choice. Try again')
            continue
        else:
            break
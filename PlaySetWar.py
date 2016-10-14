from DeckOfCards import Node
from DeckOfCards import DeckOfCards
from DeckOfCards import SetDeck


# given a list of DeckOfCards objects or those that inherit DeckOfCards
# counts cards in all players hands,
# if more than 1 player has cards, returns -1
# otherwise returns player index
def get_last_player(list_of_decks):
    winner = None
    
    for i in range(len(list_of_decks)):
        if list_of_decks[i].size() > 0:
            if winner != None:
                return -1
            else:
                winner = i
    return winner
        
        

# driver for Set War game
# given a number of players and list or string of cards
# returns who wins and when
def play(nplayers, cards):
    winner = -1
    rounds = 1
    player = 0
    

    cards_list = cards.split() # list of given cards
    deck = SetDeck(cards_list) # the line

    player_decks = deck.deal(nplayers, len(cards_list)) # list full of hands

    while winner < 0 and rounds <= 10000:
        if player_decks[player].size() > 0: #checks if player at current index has cards
            card = player_decks[player].dealTop()
            deck.addBottom(card)


            if deck.check_set(): # checks if set has been formed
                player_decks[player].addPileBottom(deck)
                move_to_next_player = False
                rounds = rounds + 1

            else:
                move_to_next_player = True

        if move_to_next_player: # iterates to next player when neccesary
            if player < nplayers - 1:
                player = player + 1
            else:
                player = 0

        winner = get_last_player(player_decks) 
        
    if winner >= 0:
        if rounds == 1:
            return("Player %d won in %d round." % (winner, rounds))
        else:
            return("Player %d won in %d rounds." % (winner, rounds))
    else:
        return("Draw after 10,000 rounds")

if __name__ == "__main__":
    print(play(int(input("Enter # of players: ")),input("Enter string of cards: ")))


        
        

    

                
                

            

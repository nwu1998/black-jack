import random
suitlist=['♠', '♦', '♥', '♣']
ranklist=['','A',2,3,4,5,6,7,8,9,10,'J','Q','K']

class Card(object):
    def __init__(self,suit,rank):
        self.rank=rank
        self.suit=suit

    def get_value(self):
        if self.rank>10:
            self.value=10
        elif self.rank==1:
            self.value=11
        else:
            self.value=self.rank

    def __repr__(self):
        return suitlist[self.suit]+str(ranklist[self.rank])

class Deck(object):
    def __init__(self):
        self.cards=[]
        for suit in range(4):
            for rank in range(1,14):
                self.cards.append(Card(suit,rank))
        random.shuffle(self.cards)

class Hand(object):
    def __init__(self,cards=[]):
        self.cards=cards

    def calc_value(self):
        tot=0
        for i in self.cards:
            tot+=i.value
        self.value=tot


class Player(object):
    def __init__(self,hands=[Hand()],bank=50):
        self.hands=hands
        self.bank=bank

    def hit(self,other,nth):
        self.hands.cards.append(other.cards[-1])
        other.cards.pop(-1)

class Dealer(object):
    def __init__(self,hand):
        self.hand=hand


class Game(object):
    #setup#
    deck=Deck()
    '''
    player_hand=Hand(deck.cards[50:])
    player=Player([player_hand],0)
    deck.cards=deck.cards[:50]
    dealer_hand=Hand(deck.cards[48:])
    dealer=Dealer(dealer_hand)
    deck.cards=deck.cards[:48]
    '''
    player=Player()
    player.hit(deck,0)
    player.hit(deck,0)

    print "Your cards are:",
    for item in player.hands[0].cards:
        print item,
        item.get_value()
    player.hands[0].calc_value()

    print player.hands[0].value
    if player.hands[0].value>21:
        burst=True
        bj=False
    elif player.hands[0].value==21:
        bj=True
        print "BLACK JACK!"
    elif player.hands[0].value<21:
        burst=False
        bj=False


#    print "One of dealer's cards is:",dealer.hand.cards[0]
#    decision=raw_input("Do you want to hit or stay?")

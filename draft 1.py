import random
suitlist=['♠', '♦', '♥', '♣']
ranklist=['','A',2,3,4,5,6,7,8,9,10,'J','Q','K']

class Card(object):
    def __init__(self,suit,rank):
        self.rank=rank
        self.suit=suit
        self.get_value()

    def get_value(self):
        if self.rank>10:
            self.value=10
        elif self.rank==1:
            self.value=11
        else:
            self.value=self.rank

    def __repr__(self):
        return suitlist[self.suit]+str(ranklist[self.rank])

def create_shoe(n):
    #n is the number of decks
    deck=[]
    for i in range(n):
        for suit in range(4):
            for rank in range(1,14):
                deck.append(Card(suit,rank))
    random.shuffle(deck)
    return deck


class Hand(object):
    def __init__(self,cards=None):
        self.cards=[]

    def hit(self,deck):
        x=deck.pop()
        self.cards.append(x)

    def get_value(self):
        tot=0
        for item in self.cards:
            tot+=item.value
        self.value=tot


class Player(object):
    def __init__(self,hands=[Hand()],bank=50):
        self.hands=hands
        self.bank=bank

class Dealer(object):
    def __init__(self,hand=Hand()):
        self.hand=hand


#preset#
bet=int(raw_input("Please place your bet"))
deck=create_shoe(1)
player=Player()
(player.hands[0]).hit(deck)
(player.hands[0]).hit(deck)
dealer=Dealer()
(dealer.hand).hit(deck)
(dealer.hand).hit(deck)

print "One of the dealer's cards is:",dealer.hand.cards[0]
print "Your cards are:",player.hands[0].cards
flag=True
dealer_flag=True
player.hands[0].get_value()
if player.hands[0].value==21:
    print "Black Jack!!"
    flag=False
elif player.hands[0].value==22:
        player.hands[0].cards[0].value=1

#player playing#        
while flag:
    action=raw_input("Do you want to hit or hold?")
    if action=='hit':
        player.hands[0].hit(deck)
        player.hands[0].get_value()
        print "Your cards are now:",player.hands[0].cards
        if player.hands[0].value==21:
            print "Black Jack!!"
            dealer_flag=False
            break
        elif player.hands[0].value>21:
            if player.hands[0].cards[-1].rank==1:
                player.hands[0].cards[-1].value=1
                player.hands[0].get_value()
            if player.hands[0].value>21:
                print "You burst!!"
                dealer_flag=False
                break
    if action=='hold':
        break

print
print "Your final cards are:",player.hands[0].cards,"with a value of :",player.hands[0].value

#dealer playing#
dealer_list=True
dealer.hand.get_value()
if dealer_flag:
    while dealer.hand.value<17:
        dealer.hand.hit(deck)
        dealer.hand.get_value()
        if dealer.hand.value>21:       
            if dealer.hand.cards[0].rank==1:
                dealer.hand.cards[0].value=1
                dealer.hand.get_value()
            if dealer.hand.value>21:
                print "The dealer's cards are:",dealer.hand.cards
                print "The dealer burst!!"
                dealer_list=False

if dealer_list:
    print "The dealer's cards are:",dealer.hand.cards,"with a value of:",dealer.hand.value
    if player.hands[0].value>dealer.hand.value:
        print "You won!"
    elif player.hands[0].value<dealer.hand.value:
        print "You lost!"
else:
    print "You won!"

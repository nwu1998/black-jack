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
    def __init__(self,hands=None,bankroll=50):
        self.hands=[Hand()]
        self.bankroll=bankroll

class Dealer(object):
    def __init__(self,hand=None):
        self.hand=Hand()


#---------------------------------------------------#
print "Hi! Welcome to the game of Black Jack!"
deck=create_shoe(1)
bank=50
bet=int(raw_input("You have $50 right now, please place your bet."))
keep_playing='yes'


while keep_playing=='yes':
    #preset#

    player=Player(bankroll=bank)
    (player.hands[0]).hit(deck)
    (player.hands[0]).hit(deck)
    dealer=Dealer()
    (dealer.hand).hit(deck)
    (dealer.hand).hit(deck)
    print "One of the dealer's cards is:",dealer.hand.cards[0]
    print "Your cards are:",player.hands[0].cards
    print

    bj=False
    dealer_flag=True
    player_bust=False
    dealer_bust=False
    first_time=True

    player.hands[0].get_value()
    if player.hands[0].value==21:
        print "Natural Black Jack!!"
        bj=True
        dealer_flag=False
        bet=1.5*bet #natural bj 
    elif player.hands[0].value==22:
        player.hands[0].cards[0].value=1
    dealer.hand.get_value()
    if dealer.hand.value==22:
        dealer.hand.cards[0].value=1

    #player playing#
    while not bj:
        if first_time:
            action=raw_input("What do you want to do: hit, hold, or double down?")
            first_time=False
        else:
            action=raw_input("What do you want to do: hit or hold?")
        if action=='hit' or action=="double down":
            if action=="double down":
                bet=bet*2
                print "Your bet is now $"+str(bet)
            player.hands[0].hit(deck)
            player.hands[0].get_value()
            print "Your cards are now:",player.hands[0].cards
            if player.hands[0].value==21:
                print "Black Jack!!"
                dealer_flag=False
                bj=True
                break
            elif player.hands[0].value>21:
                for item in player.hands[0].cards:
                    if item.rank==1:
                        item.value=1
                    player.hands[0].get_value()
                if player.hands[0].value>21:
                    print "You busted!!"
                    dealer_flag=False
                    player_bust=True
                    bank-=bet
                    break
            if action=="double down":
                break
        if action=='hold':
            break

    print
    print "Your final cards are:",player.hands[0].cards,"with a value of:",player.hands[0].value

    #dealer playing#
    if dealer_flag:
        while dealer.hand.value<17:
            dealer.hand.hit(deck)
            dealer.hand.get_value()
            if dealer.hand.value>21:       
                for item in dealer.hand.cards:
                    if item.rank==1:
                        item.value=1
                    dealer.hand.get_value()
                if dealer.hand.value>21:
                    print "The dealer's cards are:",dealer.hand.cards,"with a value of:",dealer.hand.value
                    print "The dealer busted!!"
                    dealer_bust=True

    if dealer_bust==False:
        print "The dealer's cards are:",dealer.hand.cards,"with a value of:",dealer.hand.value


    if bj or dealer_bust:
        print "You won!"
        bank+=bet
    elif player_bust:
        print "You lost!"
        bank-=bet
    elif player.hands[0].value>dealer.hand.value:
        print "You won!"
        bank+=bet
    elif player.hands[0].value<dealer.hand.value:
        print "You lost!"
        bank-=bet
    elif player.hands[0].value==dealer.hand.value:
        print "It was a tie!"

    print
    if bank<=0:
        print "You have no money left! Go home!"
        break
    else:
        keep_playing=raw_input("You now have $"+str(bank)+", do you still want to play?")
        if keep_playing=='no':
            print "Well, take your $"+str(bank)+" home and see you next time!"
            break
        else:
            print "------------NEW GAME!------------"   
            bet=int(raw_input("Please place your bet."))

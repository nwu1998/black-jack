'''
Question:
1. When the dealer has a natural black jack and
    the player hits to a black jack,who wins?
2. When both the dealer and the player bust, what happens?
'''

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
    def __init__(self,bet=0,cards=None,status=None):
        if cards==None:
            self.cards=[]
        else:
            self.cards=cards
        self.bet=bet
        self.status=1

    def hit(self,deck):
        x=deck.pop()
        self.cards.append(x)

    def get_value(self):
        tot=0
        for item in self.cards:
            tot+=item.value
        self.value=tot

class Dealer(object):
    def __init__(self,hand=None):
        self.hand=Hand()


#---------------------------------------------------#
print "Hi! Welcome to the game of Black Jack!"
deck_n=int(raw_input("How many decks of cards do you want to use?"))
deck=create_shoe(deck_n)
bank=50
bet=int(raw_input("You have $50 to begin with, how much do you want to bet?"))
keep_playing='yes'


while keep_playing=='yes':
    #preset#
    hands=[]
    hands_n=0
    hands.append(Hand(bet=bet))
    hands[0].hit(deck)
    hands[0].hit(deck)
    dealer=Dealer()
    (dealer.hand).hit(deck)
    (dealer.hand).hit(deck)

    print "One of the dealer's cards is:",dealer.hand.cards[0]
    print "Your cards are:",hands[0].cards
    print

    #splitting#
    i=0
    while i<=hands_n:
        if hands[i].cards[0].rank==hands[i].cards[1].rank:
            splitting=raw_input("You have two cards of the same rank! Do you want to split?")
            if splitting=="yes":
                hands.append(Hand(cards=[hands[i].cards.pop()],bet=bet))
                hands_n+=1
                hands[i].hit(deck)
                hands[hands_n].hit(deck)
                print "Your hands are now:",
                for item in hands:
                    print item.cards,
        else:
            i+=1


    #dealer playing in the background#
    dealer.hand.get_value()
    if dealer.hand.value==22:
        dealer.hand.cards[0].value=1
    while dealer.hand.value<17:
        dealer.hand.hit(deck)
        dealer.hand.get_value()
        if dealer.hand.value>21:       
            for item in dealer.hand.cards:
                if item.rank==1:
                    item.value=1
                dealer.hand.get_value()
    if dealer.hand.value>21:
        dealer_bust=True
    else:
        dealer_bust=False

    
    i=0
    while i<=hands_n:
        if hands_n>0:
            print
            print "---Hand",i+1,':',hands[i].cards
        
        first_time=True
        done=False
        
        hands[i].get_value()
        if hands[i].value==21:
            print "Natural Black Jack!!"
            done=True
            hands[i].bet=1.5*bet #natural bj


        #playing#
        while not done:
            if first_time:
                action=raw_input("What do you want to do: hit, hold, or double down?")
                first_time=False
            else:
                action=raw_input("What do you want to do: hit or hold?")

            if action=='hit' or action=="double down":
                if action=="double down":
                    hands[i].bet=bet*2
                    print "Your bet is now $"+str(hands[i].bet)
                hands[i].hit(deck)
                hands[i].get_value()
                print "Your cards are now:",hands[i].cards
                if hands[i].value==21:
                    print "Black Jack!!"
                    done=True
                    break
                elif hands[i].value>21:
                    for item in hands[i].cards:
                        if item.rank==1:
                            item.value=1
                        hands[i].get_value()
                    if hands[i].value>21:
                        print "You busted!!"
                        hands[i].bet=-hands[i].bet
                        hands[i].status=-1
                        done=True
                        break
                if action=="double down":
                    break
            if action=='hold':
                break

        print
        print "Your final cards of this hand are:",hands[i].cards,"with a value of:",hands[i].value
        if not done and not dealer_bust:
            if hands[i].value<dealer.hand.value:
                hands[i].bet=-hands[i].bet
                hands[i].status=-1
            elif hands[i].value==dealer.hand.value:
                hands[i].bet=0
                hands[i].status=0
        i+=1



    print "The dealer's cards are:",dealer.hand.cards,"with a value of:",dealer.hand.value
    if dealer_bust:
        print "The dealer busted!"

    print "-------------Finally!-------------"

    for i,hand in enumerate(hands):
        if hands_n>0:
            print "Hand",i+1,':',hand.cards,'-->',
        if hand.status==-1 and not dealer_bust:
            print "You lost",
        elif hand.status==0:
            print "It was a push"
        else:
            print "You won",
        if hands_n>0 and hand.status!=0:
            print "this hand!"
        else:
            print "!"
        bank+=hand.bet

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


#  Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
action_message = "Hit or stand?"
reveal = False

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        if reveal:		#All cards visible including dealer
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                        CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        else:			#Hide the dealers first card
            if pos == [60,230]:
               card_loc = (CARD_BACK_CENTER[0],CARD_BACK_CENTER[1])
               canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
            else:
               card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                           CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
               canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        i = 0
        s = "Hand contains "
        while i < len(self.cards):
            s += str(self.cards[i])
            s += " "
            i += 1
        return s

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        hand_value = 0
        aces = False
        for c in self.cards:
            for key, value in VALUES.items():
                if c.rank == key:
                    if c.rank == 'A':
                        aces = True
                    hand_value += value
        if not aces:
            return hand_value
        elif hand_value + 10 <= 21:
            return hand_value+10
        else:
            return hand_value
   
    def draw(self, canvas, pos):
        for c in self.cards:
            c.draw(canvas, pos)
            pos[0] += 80
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []
        for i in range(len(SUITS)):
            for j in range(len(RANKS)):
                self.cards.append(Card(SUITS[i], RANKS[j]))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop(0)
    
    def __str__(self):
        tmp = 0
        deck = "Deck contains "
        while i < len(self.cards):
            deck += str(self.cards[i])
            deck += " "
            tmp += 1
        return deck       


#define event handlers for buttons
def deal():
    global outcome, in_play, dealer, player, game_deck, reveal, score, action_message

    if in_play:			#Game not complete - default to player loses
        score -= 1
        
    in_play = True
    reveal = False
    action_message = "Hit or stand?"
    outcome = ""
    
    game_deck = Deck()
    game_deck.shuffle()

    dealer = Hand()
    dealer.add_card(game_deck.deal_card())

    player = Hand()
    player.add_card(game_deck.deal_card())
    dealer.add_card(game_deck.deal_card())
    player.add_card(game_deck.deal_card())

def hit():
    global score, in_play, outcome, action_message
    # if the hand is in play, hit the player
    # if busted, assign a message to outcome, update in_play and score
    
    if in_play:
        player.add_card(game_deck.deal_card())
    
        if player.get_value() > 21:
            outcome = 'Player busted'
            action_message = 'New deal?'
            in_play = False
            score -= 1

       
def stand():
    global score, reveal, outcome, in_play, action_message
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score

    reveal = True		#Show dealers cards
    if in_play:
        while dealer.get_value() < 17:
            dealer.add_card(game_deck.deal_card())

        if dealer.get_value() > 21:
            outcome = 'Dealer busted'
            action_message = 'New deal?'
            in_play = False
            score += 1
        else:
            if dealer.get_value() >= player.get_value():
                outcome = 'Dealer wins'
                action_message = 'New deal?'
                in_play = False
                score -= 1
            else:
                outcome = 'Player wins'
                action_message = 'New deal?'
                score += 1
                in_play = False

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    canvas.draw_text('Blackjack', (80,100), 30, 'white')
    canvas.draw_text("Score " + str(score), (300, 100), 30, 'white')
    canvas.draw_text('Dealer', (80,200), 20, 'white')
    canvas.draw_text('Player', (80,400), 20, 'white')
    canvas.draw_text(action_message, (200,400), 20, 'white')
    canvas.draw_text(outcome, (200,200), 20, 'white')
    dealer.draw(canvas, [60,230])
    player.draw(canvas, [60,430])
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()

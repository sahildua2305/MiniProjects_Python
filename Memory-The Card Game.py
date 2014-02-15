# implementation of card game - Memory
import simplegui
import random

c = [n % 8 for n in range(16)]
state = 0 
cards = [[n % 8 for n in range(16)], False]
card1 = 0
card2 = 1
Turns = 0

# helper function to initialize globals
def new_game():
    global state, cards, Turns
    state = 0 
    Turns = 0
    
    cards = [[c[0], False],[c[1], False],[c[2], False],[c[3], False],
    [c[4], False],[c[5], False],[c[6], False],[c[7], False],
    [c[8], False],[c[9], False],[c[10], False],[c[11], False],
    [c[12], False],[c[13], False],[c[14], False],[c[15], False]]

    random.shuffle(cards)
   
# define event handlers
def mouseclick(pos):
    # add game state logic here
     global state, cards, card1, card2, Turns

     if 0 <= pos[1] <= 100 and cards[pos[0] // 50][1] == False: # if the y coordinate of pos is within the frame and the card you clicked on is face down
        if state == 0:
            state = 1
            card1 = pos[0] // 50
            cards[(pos[0] // 50)][1] = True
        elif state == 1:
            state = 2
            card2 = pos[0] // 50
            cards[(pos[0] // 50)][1] = True
            Turns += 1
        elif state == 2:
            state = 1
            if cards[card1][0] != cards[card2][0] :
                cards[card1][1] = False
                cards[card2][1] = False
            card1 = pos[0] // 50
            cards[pos[0] // 50][1] = True    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global cards, state
    label.set_text("Turns = " + str(Turns))
    for c in range(len(cards)):
        if cards[c][1] == True:
            canvas.draw_text(str(cards[c][0]), (c*50 + 10, 75), 50, "White")
        elif cards[c][1] == False:
            canvas.draw_polygon([(c*50, 0), ((c+1)*50, 0), ((c+1)*50, 100), (c*50, 100)], 2,"black", "Green")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

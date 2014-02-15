# "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

# initializing global variables 
num_range = random.randrange(0, 100)
no_guess= 7
game_range = 100


# helper function to start and restart the game
def new_game():
    global game_range,no_guess 
    print "New Game"
    print"Range is from 0 to ",game_range
    if(game_range == 100):
        no_guess = 7
    elif(game_range == 1000):
        no_guess = 10
    print "Number of remaining guesses : ",no_guess 
    print
    return    

# defining event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global num_range, game_range
    game_range = 100
    new_game()
    num_range = random.randrange(0, 100)
    return
   
def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range, game_range
    game_range = 1000
    new_game()
    print
    num_range = random.randrange(0, 1000)
    return
    
def input_guess(guess):
    # main game logic goes here	
    global no_guess
    no_guess = no_guess-1
    print "Guess was" , int(guess)
    print "Number of remaining guesses : " , no_guess
    if(no_guess>0):
        if(num_range<int(guess)):
            print "lower..!!"
            print
        elif(num_range>int(guess)):
            print "Higher..!!"
            print
        else:
            print "Correct..!!"
            print
            new_game()
    elif(no_guess== 0):
        if(num_range == int(guess)):
            print "Correct..!!"
        else:
            print "You ran out of choices"
            print"The number was : " , num_range
            print
            new_game()
            
# create frame
frame = simplegui.create_frame("Guess the Number" , 200 , 200 , 300)


# register event handlers for control elements
frame.add_button("Range[0,100)", range100, 100)
frame.add_button("Range[0,1000)", range1000, 100)
frame.add_input("Enter the guess", input_guess, 100)
frame.add_button("Restart",new_game, 100)


# call new_game and start frame
frame.start()
new_game()



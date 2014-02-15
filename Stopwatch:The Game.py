# "Stopwatch: The Game"
import simplegui

# defining global variables
A = 0
B = 0
C = 0
D = 0
time = " "
interval = 100
nitika = 0
x = 0
y = 0
watch = False

# defining helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    D = t%10
    t = t/10
    C = t%10
    t = t/10
    if t<=5 :
        B = t
        A = 0
    else:
        B = 0
        A = 1
        
    time = str(A) + " : " + str(B)+ str(C) +" . " +str(D)    
    return time
    
# defining event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global watch
    timer.start()
    watch = True
    
def stop():
    global x , watch , y
    if watch :
        timer.stop()
        if (D == 0) :
            x = x + 1
            y = y + 1
        else:
            y = y + 1
        watch = False    

def reset():
    global nitika , time , x , y
    timer.stop()
    time = " "
    nitika = 0
    x = 0
    y = 0
    
# defining event handler for timer with 0.1 sec interval
def timer_handler():
    global nitika
    nitika = nitika + 1
    
    
# defining draw handler
def draw(canvas):
    canvas.draw_text(format(nitika) , (150 , 200) , 34 , "Magenta")
    canvas.draw_text( (str(x) + "/" + str(y)) , (300 ,50) , 20 , "Lime")
    
# create frame
frame = simplegui.create_frame("Stopwatch" , 400 , 400)

# register event handlers
frame.add_button("Start" , start)
frame.add_button("Stop" , stop)
frame.add_button("Reset" , reset)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval ,timer_handler)

# start frame
frame.start()



import turtle
import random
import winsound

def reset_highscore():
    global highscore
    highscore = 0
    with open("high_score.txt", "w") as file:
        file.write("0") 

while True:
    command = input("Reset highscore? (Yes/No): ")
    if command.lower() == "yes":
        reset_highscore()
        print("High score reset to 0.")
        print("Launching Game...")
        break
    elif command.lower() == "no":
        print("Launching Game...")
        break
    else:
        print("Invalid input. Please enter 'Yes' or 'No'.")

screen = turtle.Screen()
screen.register_shape("IMAGES/BG main.gif")
screen.register_shape("IMAGES/background 2.gif")
screen.bgpic("IMAGES\BG main.gif")
screen.title("Purr-fect Hit")
screen.setup(width=800, height=600)
screen.tracer(0)

play_button = turtle.Turtle()
play_button.hideturtle()
play_button.penup()
play_button.goto(-125,  0)
play_button.pendown()
play_button.color("black")
play_button.write("Play", font=("Comic Sans MS",  24, "normal"))

quit_button = turtle.Turtle()
quit_button.hideturtle()
quit_button.penup()
quit_button.goto(75,  0)
quit_button.pendown()
quit_button.color("black")
quit_button.write("Quit", font=("Comic Sans MS",  24, "normal"))

screen.register_shape("IMAGES/target.gif")
target = turtle.Turtle()
target.shape("IMAGES/target.gif")
target.shapesize(stretch_wid=2, stretch_len=2, outline=2)
target.penup()
target.speed(0)
target.goto(0, 0)

score = 0
score_display = turtle.Turtle()
score_display.color("black")
score_display.penup()
score_display.hideturtle()
score_display.goto(-290, 240) 

def load_highscore():
    global highscore
    try:
        with open("high_score.txt", "r") as file:
            highscore = int(file.read())
    except FileNotFoundError:
        with open("high_score.txt", "w") as file:
            file.write("0")
load_highscore()
high_score = turtle.Turtle()
high_score.hideturtle()
high_score.penup()
high_score.goto(0,  -200)
high_score.color("black")
high_score.write(f"Top Score: {highscore}", align="center", font=("Comic Sans MS",  20, "bold"))

tduration = 60
timer_display = turtle.Turtle()
timer_display.color("black")
timer_display.penup()
timer_display.hideturtle()
timer_display.goto(0, 240)

def play_bgmusic(file):
    winsound.PlaySound(file, winsound.SND_ASYNC | winsound.SND_LOOP)
bgmusic = 'MUSIC/Nyan Cat! [Official].wav'
play_bgmusic(bgmusic)

def play_game():
    print("Playing game")
    screen.bgpic("IMAGES/background 2.gif")
    play_button.undo()
    quit_button.undo()
    high_score.undo()
    play_bgmusic(bgmusic)
    score_display.write("Score: {}".format(score), align="center", font=("Comic Sans MS", 24, "normal"))
    timer_display.write("Time: 60", align="center", font=("Comic Sans MS", 24, "normal"))

    def move_target():
        x = random.randint(-250, 250)
        y = random.randint(-250, 220)
        target.goto(x, y)

    def click(x, y):
        global score
        if target.distance(x, y) < 20:
            score += 10
            move_target()
        else:
            score -= 5
        score_display.clear()
        score_display.write("Score: {}".format(score), align="center", font=("Comic Sans MS", 24, "normal"))

    def timer():
        global tduration
        tduration -= 1
        timer_display.clear()
        timer_display.write("Time: {}".format(tduration), align="center", font=("Comic Sans MS", 24, "normal"))
        if tduration > 0:
            screen.ontimer(timer, 1000)
        else:
            gameover()
    
    def update_highscore():
        high_score.clear()
        high_score.write("Top Score: {}".format(highscore), align="center", font=("Comic Sans MS",  20, "bold"))

    def gameover():
        global highscore
        screen.bgpic("IMAGES/background 3.gif")
        screen.onclick(None)
        target.hideturtle()
        timer_display.clear()
        if score > highscore:
            highscore = score
        update_highscore()
        save_highscore()

    def save_highscore():
        with open("high_score.txt", "w") as file:
            file.write(str(highscore))

    screen.onclick(click)

    timer()

    while True:
        screen.update()
    
def quit_game():
    print("Quitting game")
    turtle.bye()

def menuclick(x, y):
    if play_button.distance(x, y) < 40:
        play_game()
    elif quit_button.distance(x, y) < 40:
        quit_game()

screen.onclick(menuclick)

turtle.mainloop()
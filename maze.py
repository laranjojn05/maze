
import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("maze puzzle")
wn.setup(700, 700)

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("green")
        self.penup()
        self.speed(0)
        
    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24
        
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
    
    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            
    def go_left(self):
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            
    def go_right(self):
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        
        
        
levels = [""]

level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXX",
    "X  X       X X        X",
    "XX XXXX  XXX XXXX  XX X",
    "X        X   X     X  X",
    "XXXX       XX X    X  X",
    "X    XXXXXXXX XX XXXXXX",
    "XXXX X        XX     XX",
    "X    XX XXXXX X XXXXXXX",
    "XXXX X  XX    X    XX X",
    "X       XXX X   XXXX  X",
    "XXX XXXXX XXXXX X  XX X",
    "X X   X   XX          X",
    "X X X X X XX XXXXXXXX X",
    "X   X X X X           X",
    "XXXXX X   XXXXX XXXX  X",
    "X     XX     XX   XX XX",
    "XXXXXXXXXXXXXXXXXXXXXXX",
    
]

levels.append(level_1)

def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
            
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                
                walls.append((screen_x, screen_y))
                
            if character == "P":
                player.goto(screen_x, screen_y)
                
pen = Pen()
player = Player()

walls = []

setup_maze(levels[1])


turtle.listen()
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")

wn.tracer(0)
while True:
    wn.update()
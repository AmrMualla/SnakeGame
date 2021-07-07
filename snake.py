from turtle import Turtle
START_POSITIONS = [(0,0), (-20, 0), (-40,0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]
    
    def create_snake(self):
        for pos in START_POSITIONS:
            self.add_part(pos)

    def add_part(self, position):
        snake_body = Turtle("square")
        snake_body.color("green")
        snake_body.penup()
        snake_body.goto(position)
        self.parts.append(snake_body)


    def grow(self):
        self.add_part(self.parts[-1].position())

    def move(self):
        for snake_body in range(len(self.parts)-1, 0, -1):
            x = self.parts[snake_body-1].xcor()
            y = self.parts[snake_body-1].ycor()
            self.parts[snake_body].goto(x, y)
        self.head.forward(20)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for part in self.parts:
            part.goto(1000, 1000)
        self.parts.clear()
        self.create_snake()
        self.head = self.parts[0]

from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.snake_head = self.snake[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        timmy = Turtle("square")
        timmy.color("white")
        timmy.penup()
        self.snake.append(timmy)
        timmy.setpos(position)
    
    def extend(self):
        #add new segment to the snake
        self.add_segment(self.snake[-1].position())

    def move(self):
        for snake_bits in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[snake_bits - 1].xcor()
            new_y = self.snake[snake_bits - 1].ycor()
            self.snake[snake_bits].goto(new_x, new_y)
            
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(90)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(270)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(180)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(0)
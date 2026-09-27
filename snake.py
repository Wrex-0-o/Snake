from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            timmy = Turtle("square")
            timmy.color("white")
            timmy.penup()
            self.snake.append(timmy)
            timmy.setpos(position)

    def move(self):
        for snake_bits in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[snake_bits - 1].xcor()
            new_y = self.snake[snake_bits - 1].ycor()
            self.snake[snake_bits].goto(new_x, new_y)
            
        self.snake[0].forward(MOVE_DISTANCE)
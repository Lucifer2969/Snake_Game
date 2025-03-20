from turtle import Turtle

POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.block_list = []
        self.create_snake()
        self.head = self.block_list[0]

    def create_snake(self):
        for i in POSITION:
            self.create_blocks(i)

    def create_blocks(self,i):
        blocks = Turtle("square")
        blocks.color("white")
        blocks.speed("slowest")
        blocks.penup()
        blocks.goto(i)
        self.block_list.append(blocks)

    def snake_position(self):
        for block in self.block_list:
            block.goto(1000,1000)
        self.block_list.clear()
        self.create_snake()
        self.head = self.block_list[0]

    def extend_blocks(self):
        self.create_blocks(self.block_list[-1].position())

    def move(self):
        for block_num in range(len(self.block_list) - 1, 0, -1):
            new_x = self.block_list[block_num - 1].xcor()
            new_y = self.block_list[block_num - 1].ycor()
            self.block_list[block_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
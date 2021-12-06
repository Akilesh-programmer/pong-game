from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        # Creating the paddle.
        self.shape("square")
        self.color("white")
        # Taking the pen up so that the object doesn't draw lines while it is moving.
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)



    # Listening to the user input and then moving the paddle according to the key press.


    def go_up(self):
        new_y = self.ycor() + 20 
        self.goto(x=self.xcor(), y=new_y) 

    def go_down(self):
        new_y = self.ycor() - 20 
        self.goto(x=self.xcor(), y=new_y)



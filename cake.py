from turtle import Turtle

class Cake(Turtle):

  def __init__(self):
    super().__init__()
    self.shape("arrow")
    self.pensize(4)
    self.speed("fastest")
    self.penup()
    self.goto(-70,-95)
    self.draw_cake()
    
  def draw_cake(self):
    # cake
    self.color("black","pink")
    self.begin_fill()
    self.pendown()
    self.setheading(270)
    self.forward(60)
    self.setheading(0)
    self.forward(60)
    self.setheading(90)
    self.forward(60)
    self.setheading(180)
    self.forward(60)
    self.end_fill()
    # candle
    self.setheading(0)
    self.forward(25)
    # self.color("black","white")
    # self.begin_fill()
    self.setheading(90)
    self.forward(25)
    self.setheading(0)
    self.forward(5)
    self.setheading(0)
    self.color("black","orange")
    self.begin_fill()
    self.circle(5,-180)
    self.setheading(0)
    self.circle(-5,180)
    self.end_fill()
    # self.setheading(0)
    # self.circle(-5,-180)
    self.setheading(0)
    self.forward(5)
    
    self.setheading(270)
    self.forward(25)
    # self.end_fill()
    self.setheading(180)
    self.forward(35)
    self.cream()
    self.setheading(270)
    self.forward(30)
    self.setheading(180)
    self.forward(60)
    self.cream()

  def cream(self):
    self.color("black","brown")
    self.begin_fill()
    
    for i in range (0,3):
     self.setheading(270)
     self.circle(10,180)
    self.end_fill()
    self.hideturtle()
    # self.hideturtle()

   
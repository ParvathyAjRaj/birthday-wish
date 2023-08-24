from turtle import Turtle

class Table(Turtle) :
  def __init__(self):
    super().__init__()
    self.shape("arrow")
    self.color("black","brown")
    self.speed("fastest")
    self.pensize(4)
    # print("Hello table")
    self.penup()
    self.goto(-125,-125)
    self.setheading(180)
    self.pendown()
    self.forward(20)
    self.drawing_table()

  def big_leg(self):
    self.setheading(270)
    self.forward(50)
    self.setheading(0)
    self.forward(10)
    self.setheading(90)
    self.forward(50)
    self.setheading(180)
    self.forward(10)

  def small_leg(self):
    self.setheading(270)
    self.forward(25)
    self.setheading(180)
    self.forward(10)
    self.setheading(90)
    self.forward(25)
    self.setheading(0)
    
  def drawing_table(self):
    # print("Hello table")
    self.color("black", "brown")
    self.begin_fill()
    self.forward(30)
    self.setheading(240)
    self.forward(50)
    self.setheading(0)
    
    self.forward(20)
    self.big_leg()
    
    self.setheading(0)
    self.forward(20)
    self.small_leg()

    self.forward(150)
    self.big_leg()

    self.setheading(0)
    self.forward(20)
    self.small_leg()

    self.forward(20)
    self.setheading(70)
    self.forward(45)
    self.setheading(180)
    self.forward(120)
    self.hideturtle()
    self.end_fill()
    
    
    
   
   

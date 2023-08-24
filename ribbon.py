from turtle import Turtle
import random

class Ribbon(Turtle):

  def __init__(self,color_list):
    super().__init__()
    self.shape("arrow")
    self.pensize(4)
    self.speed("fastest")
    x_big = 250
    y_big = 250
    self.draw_ribbon_large(color_list,x_big,y_big)

    x_big = -250
    y_big = -100
    self.draw_ribbon_large(color_list,x_big,y_big)

    # x_big = -250
    # y_big = -100
    # self.draw_ribbon_large(color_list,x_big,y_big)

    x_big = 150
    y_big = -150
    self.draw_ribbon_large(color_list,x_big,y_big)

    x_small = 0
    y_small = 50
    self.draw_ribbon_small(color_list,x_small,y_small)

    x_small =50
    y_small = -100
    self.draw_ribbon_small(color_list,x_small,y_small)
    x_small = 230
    y_small = 50
    self.draw_ribbon_small(color_list,x_small,y_small)

    x_small = 100
    y_small = 150
    self.draw_ribbon_small(color_list,x_small,y_small)

    x_small = -200
    y_small = 200
    self.draw_ribbon_small(color_list,x_small,y_small)

    x_small = 50
    y_small = 200
    self.draw_ribbon_small(color_list,x_small,y_small)
  def draw_ribbon_large(self,color_list,x,y):
    self.penup()
    self.color("black",random.choice(color_list))
    self.begin_fill()
    self.goto(x,y)
    self.pendown()
    self.setheading(270)
    self.forward(60)
    self.setheading(45)
    self.forward(10)
    self.setheading(315)
    self.forward(10)
    self.setheading(90)
    self.forward(60)
    self.setheading(225)
    self.forward(10)
    self.setheading(135)
    self.goto(x,y)
    self.end_fill()
    self.hideturtle()

  def draw_ribbon_small(self,color_list,x,y):
    self.penup()
    self.color("black",random.choice(color_list))
    self.begin_fill()
    self.goto(x,y)
    self.pendown()
    self.setheading(270)
    self.forward(40)
    self.setheading(45)
    self.forward(6)
    self.setheading(315)
    self.forward(6)
    self.setheading(90)
    self.forward(40)
    self.setheading(225)
    self.forward(6)
    self.setheading(135)
    self.goto(x,y)
    self.end_fill()
    self.hideturtle()
    
    
    
    
from turtle import Turtle
import random

class Balloon(Turtle):

  def __init__(self,color_list):
    print("Entered ballon class")
    super().__init__()
    self.shape("arrow")
    self.speed("fastest")
    self.pensize(10)
    y_position = -200
    x_position = [-250,-200,-150,-100,-50,0,50,100,150,200,250]
    angle = [90,70]
    
    self.balloon(color_list,x_position,y_position,angle)
    

  def balloon(self,color_list,x,y,angle):
    all_balloon=[]
    for i in range(0,11):
     b = Turtle(shape ="circle")
     # b.shape="circle"
     size = [3,4,5]
     b.shapesize(random.choice(size))
     b.pensize(10)
     b.penup()
     b.color("black",random.choice(color_list))
     b.goto(x[i],y)
     all_balloon.append(b)
     count = 1
     self.hideturtle()
    while count<=250:
      for ball in all_balloon:
       # ball.circle(20)
       distance = random.randint(0,100)
       moving_angle = random.choice(angle)
       ball.setheading(moving_angle)
       ball.forward(distance)
       count+=1
    
    
    
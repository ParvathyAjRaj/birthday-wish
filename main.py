from turtle import Turtle, Screen
import random
from table import Table
from ribbon import Ribbon
from cake import Cake
from balloon import Balloon


# Drawing A
def drawing_A(tim):
  tim.pendown()
  tim.forward(25)
  tim.right(120)
  tim.forward(25)
  tim.back(15)
  tim.right(120)
  tim.forward(10)


# Drawing P
def drawing_P(tim):
  tim.pendown()
  tim.left(90)
  tim.forward(22)
  tim.right(90)
  tim.circle(-8, 180)


# Drawing U
def drawing_U(tim):
  tim.pendown()
  tim.forward(18)
  tim.circle(5, 180)
  tim.forward(18)


# Drawing Y
def drawing_Y(tim):
  tim.pendown()
  tim.forward(12)
  tim.setheading(120)
  tim.forward(12)
  tim.backward(12)
  tim.setheading(60)
  tim.forward(12)


# Drawing B
def drawing_B(tim):
  tim.pendown()
  tim.left(90)
  tim.forward(22)
  tim.right(90)
  tim.circle(-6, 180)
  tim.setheading(0)
  tim.circle(-6, 180)


# Drawing D
def drawing_D(tim):
  tim.pendown()
  tim.setheading(90)
  tim.forward(22)
  tim.setheading(0)
  tim.circle(-12, 180)


# Drawing H
def drawing_H(tim):
  tim.forward(23)
  tim.backward(10)
  tim.left(90)
  tim.forward(10)
  tim.left(90)
  tim.forward(13)
  tim.backward(23)


# Drawing heart
def drawing_heart(tim, color_list):
  tim.color("black", random.choice(color_list))
  tim.begin_fill()
  tim.pendown()
  tim.setheading(135)
  tim.forward(30)
  tim.right(45)
  tim.circle(-10, 180)
  tim.left(180)
  tim.circle(-10, 180)
  tim.right(45)
  tim.forward(30)
  tim.left(45)
  tim.end_fill()
  tim.hideturtle()


# Drawing love
def drawing_love(tim):
  # Heart
  tim.color("black", "red")
  tim.begin_fill()
  tim.pendown()
  tim.setheading(135)
  tim.forward(40)
  tim.right(45)
  tim.circle(-15, 180)
  tim.left(180)
  tim.circle(-15, 180)
  tim.right(45)
  tim.forward(40)
  tim.left(45)
  tim.end_fill()
  # BottomArrows in heart
  tim.penup()
  tim.setheading(180)
  tim.forward(40)
  tim.setheading(270)
  tim.forward(5)
  tim.pendown()
  arrow_angle = 150
  drawing_arrow(tim, arrow_angle)
  tim.setheading(30)
  tim.forward(10)
  # tim.setheading(150)
  arrow_angle = 150
  drawing_arrow(tim, arrow_angle)
  # Piercing
  tim.setheading(30)
  tim.forward(22)
  tim.penup()
  tim.forward(20)
  tim.pendown()
  tim.forward(45)
  # TopArrow in heart
  arrow_angle = 150
  drawing_arrow(tim, arrow_angle)
  tim.hideturtle()


# Drawing Arrow
def drawing_arrow(tim, arrow_angle):
  tim.setheading(arrow_angle)
  tim.forward(10)
  tim.back(10)
  tim.setheading(arrow_angle + 120)
  tim.forward(10)
  tim.back(10)


# Print different star members
def member_star(color_list):
  x_position2 = [-125]
  y_position2 = [-125]
  all_star_turtles = []
  for turtle_index in range(0, 1):
    new_turtle_star = Turtle(shape="arrow")
    new_turtle_star.penup()
    new_turtle_star.color("black", random.choice(color_list))
    # new_turtle_firework.beginfill()
    new_turtle_star.goto(x_position2[turtle_index], y_position2[turtle_index])
    all_star_turtles.append(new_turtle_star)
  return all_star_turtles


# Print different heart members
def members(color_list):
  x_position2 = [0, -150]
  y_position2 = [-150, -150]
  # all_firework_turtles=[]
  all_heart_turtles = []
  for turtle_index in range(0, 2):
    new_turtle_heart = Turtle(shape="arrow")
    new_turtle_heart.penup()
    new_turtle_heart.color(random.choice(color_list))
    new_turtle_heart.goto(x_position2[turtle_index], y_position2[turtle_index])
    all_heart_turtles.append(new_turtle_heart)
  return all_heart_turtles


# Fireworks
def fireworks(turtle_list, color_list):
  for member in turtle_list:
    member.pendown()
    member.pensize(3)
    member.speed("fastest")
    member_angle = 0
    while member_angle <= 360:
      member_angle += 45
      member.setheading(member_angle)
      member_color = random.choice(color_list)
      member.color(member_color)
      if (member_angle == 45 or member_angle == 135 or member_angle == 225
          or member_angle == 315):
        member.forward(50)
        member.backward(50)
      else:
        member.forward(60)
        member.backward(60)
    member.hideturtle()


# Turtle heart
def turtle_heart_fn(turtle_heart, color_list):
  color_list = color_list
  for member in turtle_heart:
    member.pendown()
    member.pensize(3)
    drawing_heart(member, color_list)


def dashed_line(angle, count):
  new_turtle_firework.setheading(angle)
  for i in range(count):
    new_turtle_firework.pensize(1)
    new_turtle_firework.pendown()
    new_turtle_firework.speed("fastest")
   
    new_turtle_firework.color(random.choice(color_list))
    new_turtle_firework.forward(distance)
    new_turtle_firework.penup()
    new_turtle_firework.forward(distance)


# print(new_turtle_firework.ycor())
  turtle_list = []
  turtle_list.append(new_turtle_firework)
  return turtle_list


def star(star_list, tim):
  for member in star_list:
    member.pendown()
    member.pensize(3)
    drawing_star(member, color_list)
    # return x,y


def drawing_star(tim, color_list):
  tim.color("black", random.choice(color_list))
  tim.begin_fill()
  tim.speed("fastest")
  tim.pendown()
  
  # top diamond
  tim.setheading(0)
  tim.forward(30)
  for i in range(0, 3):
    tim.right(90)
    tim.forward(30)
  # bottom diamond and left diamond
  for i in range(0, 2):
    tim.forward(30)
    for i in range(0, 3):
      tim.left(90)
      tim.forward(30)
  # right diamond
  tim.forward(30)
  for i in range(0, 3):
    tim.right(90)
    tim.forward(30)
  # tim.hideturtle()
  tim.end_fill()

  # ribbon
  tim.setheading(90)
  tim.forward(30)
  x = tim.xcor()
  y = tim.ycor()

  tim.setheading(150)
  tim.forward(30)
  tim.circle(-15, 180)
  tim.goto(x, y)
  tim.forward(30)
  tim.goto(x,y)

  tim.setheading(30)
  tim.forward(30)
  tim.circle(15, 180)
  tim.goto(x, y)
  tim.forward(30)
  tim.goto(x,y)
  # tim.setheading(270)
  # tim.forward(30)
  tim.hideturtle()
  # y_mid = y-30
  # x_mid=x
  # return x_mid,y_mid
  


# main
tim = Turtle()
screen = Screen()
screen.bgcolor("white")
screen.setup(width=300, height=400)
screen.title("A B'Day Card for U !")
tim.shape("arrow")
tim.pensize(4)
tim.speed("fastest")
color_list = [
  "red", "yellow", "blue", "green", "violet", "orange", "purple", "cyan"]

# movement = "straight"
new_turtle_firework = Turtle(shape="turtle")
new_turtle_firework.penup()
fire_home = [150, -160]
new_turtle_firework.goto(fire_home)

new_turtle_firework.left(90)
distance = 10
turtle_list = dashed_line(90, 15)
fireworks(turtle_list, color_list)
new_turtle_firework.penup()

new_turtle_firework.goto(fire_home)
new_turtle_firework.pendown()
# movement = "left"
turtle_list = dashed_line(150, 20)
fireworks(turtle_list, color_list)
new_turtle_firework.penup()

new_turtle_firework.goto(fire_home)
new_turtle_firework.pendown()
# movement = "right"
turtle_list = dashed_line(45, 5)
fireworks(turtle_list, color_list)
new_turtle_firework.penup()

new_turtle_firework.goto(fire_home)
new_turtle_firework.pendown()
# movement = "right"
turtle_list = dashed_line(120, 22)
fireworks(turtle_list, color_list)

tim.penup()
tim.setheading(135)
tim.backward(-225)
tim.pendown()
tim.left(135)

# tim.color(random.choice(color_list))
tim.color("black")
drawing_H(tim)

tim.right(90)
tim.penup()
tim.forward(8)
tim.pendown()
tim.left(60)

# tim.color(random.choice(color_list))
tim.color("black")
drawing_A(tim)

tim.penup()
tim.left(60)
tim.forward(15)
tim.left(120)
tim.forward(30)

# tim.color(random.choice(color_list))
tim.color("black")
drawing_P(tim)

tim.penup()
tim.setheading(270)
tim.forward(6)
tim.setheading(0)
tim.forward(15)

# tim.color(random.choice(color_list))
tim.color("black")
drawing_P(tim)

tim.penup()
tim.setheading(270)
tim.forward(6)
tim.setheading(0)
tim.forward(20)
tim.setheading(90)

# tim.color(random.choice(color_list))
tim.color("black")
drawing_Y(tim)

tim.setheading(270)
tim.penup()
tim.forward(20)
tim.setheading(0)
tim.forward(30)

# tim.color(random.choice(color_list))
tim.color("black")
drawing_B(tim)

tim.setheading(0)
tim.penup()
tim.forward(15)
tim.setheading(90)
tim.forward(2)

# tim.color(random.choice(color_list))
tim.color("black")
drawing_D(tim)

tim.setheading(0)
tim.penup()
tim.forward(15)
tim.left(60)

# tim.color(random.choice(color_list))
tim.color("black")
drawing_A(tim)

tim.penup()
tim.left(60)
tim.forward(15)
tim.left(120)
tim.forward(30)
tim.setheading(90)

# tim.color(random.choice(color_list))
tim.color("black")
drawing_Y(tim)

tim.penup()
tim.home()
tim.setheading(135)
tim.forward(100)
tim.setheading(180)
tim.forward(50)
tim.setheading(0)
tim.left(60)

# tim.color(random.choice(color_list))
tim.color("black")
drawing_A(tim)

tim.penup()
tim.left(60)
tim.forward(15)
tim.left(120)
tim.forward(30)

# tim.color(random.choice(color_list))
tim.color("black")
drawing_P(tim)

tim.penup()
tim.setheading(270)
tim.forward(6)
tim.setheading(0)
tim.forward(15)

# tim.color(random.choice(color_list))
tim.color("black")
drawing_P(tim)

tim.penup()
tim.setheading(270)
tim.forward(6)
tim.setheading(0)
tim.forward(15)
tim.setheading(90)
tim.forward(22)
tim.setheading(270)

# tim.color(random.choice(color_list))
tim.color("black")
drawing_U(tim)

tim.color("black")
tim.penup()
tim.home()
tim.setheading(180)
tim.forward(80)
tim.setheading(270)
tim.forward(20)
tim.setheading(0)

drawing_love(tim)

tim.penup()
tim.hideturtle()

# # old code for turtle heart
# turtle_heart = members(color_list)
# # fireworks(turtle_firework,color_list)
# turtle_heart_fn(turtle_heart,color_list)

# table
table = Table()

# turtle star
turtle_star = member_star(color_list)
star(turtle_star, color_list)

# cake
cake = Cake()

# ribbon
ribbon = Ribbon(color_list)

# balloon
balloon = Balloon(color_list)


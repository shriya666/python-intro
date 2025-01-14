# pick sentence theme, make user pick noun/verb/whatever, show sentence with choices in them, redo button.

sentence1= "senetnce here"

noun1= input("NOUN ")
print(nou


import turtle
class shapes:
  shape=turtle.Turtle()
  shape.speed(0)
  colors= ["pink", "light blue", "#dbc4ff", "light green", "yellow","#fcc99"]
  def triangle(len, x, y):
    shapes.shape.penup()
    shapes.shape.goto(x,y)
    shapes.shape.pendown()
    for i in range(3):
      shapes.shape.forward(len)
      shapes.shape.lt(120)
  def square(len, x, y,):
    shapes.shape.penup()
    shapes.shape.goto(x, y)
    shapes.shape.pendown()
    for i in range(4):
      shapes.shape.forward(len)
      shapes.shape.lt(90)
  def spiral(r, x, y):
    shapes.shape.speed(0)
    shapes.shape.penup()
    shapes.shape.goto(x,y)
    shapes.shape.pendown()
    for i in range(r):
      for c in range(180):
        shapes.shape.forward(0.5+(i/2))
        shapes.shape.lt(1)
        shapes.shape.color(shapes.colors[c%6])
  def spiral2(r, x, y):
          shapes.shape.speed(0)
          shapes.shape.penup()
          shapes.shape.goto(x,y)
          shapes.shape.pendown()
          for c in range(r):
            shapes.shape.forward(c)
            shapes.shape.lt(125)
            shapes.square(c, x, y)
            shapes.shape.color(shapes.colors[c%6])
s=shapes

s.spiral2(500, 0, 0)
          



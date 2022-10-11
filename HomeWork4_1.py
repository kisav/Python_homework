import random
import turtle

t = turtle.Pen()
t.speed(10)


def draw_house():
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    t.setpos(x, y)
    t.fillcolor('#FFF8DC')
    t.begin_fill()
    for i in range(4):
        t.forward(70)
        t.left(90)
    t.end_fill()
    t.fillcolor('#B8860B')
    t.begin_fill()
    t.left(90)
    t.forward(70)
    t.left(90)
    t.forward(30)
    t.right(120)
    t.forward(150)
    t.right(120)
    t.forward(150)
    t.right(120)
    t.forward(120)
    t.end_fill()


for im in range(5):
    draw_house()
input('Закрыть окно')

from turtle import *
from math import *
pos = [Vec2D(100, -100), Vec2D(100, 100), Vec2D(-100, 100), Vec2D(-100, -100)]
vel = [Vec2D(15, -12), Vec2D(-12, 27), Vec2D(-23, 24), Vec2D(-13, 18)]
lnk = [[1, 3, 2], [0, 2], [1, 3, 0], [0, 2]]
col = ['red', 'blue', 'yellow', 'green']
tur = []
pre = 0.2
cof = 0.1
sta = 150
ela = 0.000001
num = 4
bgcolor('black')
title('GPE Simulator')
for i in range(num):
    tur.append(Turtle())
    tur[i].pencolor(col[i])
    #tur[i].hideturtle()
    tur[i].speed(0)
    tur[i].penup()
    tur[i].goto(pos[i])
    tur[i].shape('circle')
    tur[i].dot(5)
    tur[i].pendown()
while True:
    for i in range(num):
        vel[i] -= abs(vel[i]) * vel[i] * pre * cof
    for i in range(num):
        for j in range(num):
            if not j in lnk[i]:
                continue
            vel[i] += (sta - abs(pos[j] - pos[i])) ** 3 / abs(pos[j] - pos[i]) * pos[i] * pre * ela
    for i in range(num):
        pos[i] += vel[i] * pre
        tur[i].goto(pos[i])
    print(pos, vel)

from turtle import *
from math import *
pos = [Vec2D(100, -100), Vec2D(100, 100), Vec2D(-100, 100), Vec2D(-100, -100)]
vel = [Vec2D(15, -12), Vec2D(-12, 27), Vec2D(-23, 24), Vec2D(-13, 18)]
sta = [[0, 150, 210, 150],
       [150, 0, 150, 0],
       [210, 150, 0, 150],
       [150, 0, 150, 0]]
ela = [[0, 0.000001, 0.000001, 0.000001],
       [0.000001, 0, 0.000001, 0],
       [0.000001, 0.000001, 0, 0.000001],
       [0.000001, 0, 0.000001, 0]]
pla = [[0, 0, 0, 0.001],
       [0, 0, 0, 0],
       [0, 0, 0, 0.001],
       [0.001, 0, 0.001, 0]]
col = ['red', 'blue', 'yellow', 'green']
tur = []
pre = 0.01
cof = 0.1
num = 4
cnt = 0
bgcolor('black')
title('GPE Simulator')
for i in range(num):
    tur.append(Turtle())
    tur[i].pencolor(col[i])
    tur[i].speed(0)
    tur[i].penup()
    tur[i].goto(pos[i])
    tur[i].shape('circle')
    tur[i].dot(5)
    tur[i].pendown()
while True:
    cnt += 1
    for i in range(num):
        if abs(vel[i]) * pre * cof > 1:
            vel[i] = Vec2D(0, 0)
        else:
            vel[i] -= abs(vel[i]) * vel[i] * pre * cof
    for i in range(num):
        for j in range(num):
            if sta[i][j] == 0 or ela[i][j] == 0:
                continue
            vel[i] -= (abs(pos[j] - pos[i]) - sta[i][j]) ** 3 / abs(pos[j] - pos[i]) * pos[i] * pre * ela[i][j]
    for i in range(num):
        t = vel[i]
        for j in range(num):
            t *= (1 - pla[i][j])
        vel[i] = t
    if cnt == 10000:
        vel[3] += Vec2D(-100, -100)
    for i in range(num):
        pos[i] += vel[i] * pre
        if cnt % 100 == 0:
            tur[i].goto(pos[i])

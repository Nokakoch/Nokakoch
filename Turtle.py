from turtle import *
from random import random, randint
import time

peter = Turtle()

for i in range(3):
    for i in range(36):
        peter.forward(5)
        peter.right(10)
        if i==35 :
            peter.forward(50)

while True:
    distance = randint(1,50)
    angle = randint(0,360)
    peter.forward(distance)
    peter.right(angle)
    

peter.clone()

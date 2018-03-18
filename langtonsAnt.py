#Edmund Goodman - Creative Commons Attribution-NonCommercial-ShareAlike 2.5
#Langton's Ant
import os, math, colorsys
from turtle import *

class ant:
    def __init__(self, direction, position, board, speed):
        self.direction = direction
        self.position = position
        self.board = board
        self.speed = speed

    def turn(self, boardColour):
        if boardColour == 1:
            self.direction -= 1
        else:
            self.direction += 1
        self.direction %= 4

    def flip(self, boardColour):
        self.board[self.position[1]][self.position[0]] = (boardColour+1)%2

    def move(self):
        if self.direction == 0:
            self.position[1] += 1
        elif self.direction == 1:
            self.position[0] += 1
        elif self.direction == 2:
            self.position[1] -= 1
        else:
            self.position[0] -= 1

    def displayBoard(self):
        pu()
        goto(self.position[0]*5-500,self.position[1]*5-500)
        pd()
        dot(5)

speed(0)
setup(1000,1000)
tracer(100,0)
os.system('clear')
iterationCount, width, height = 13579, 200, 200
ant1 = ant(0,[int(width/2),int(height/2)], [[0 for _ in range(height)] for _ in range(width)], 0)
for i in range(iterationCount):
    boardColour = ant1.board[ant1.position[1]][ant1.position[0]]
    ant1.turn(boardColour)
    ant1.flip(boardColour)
    ant1.move()
    color(colorsys.hsv_to_rgb(i/1000,1.0,1.0))
    ant1.displayBoard()
update()
done()

#Edmund Goodman - Creative Commons Attribution-NonCommercial-ShareAlike 2.5
#Langton's Ant
import os, math

class ant:
    def __init__(self, direction, position, board):
        #Initialise the member variables
        self.direction = direction
        self.position = position
        self.board = board

    def turn(self, boardColour):
        #Change the ant's direction based on the current square colour
        if boardColour == 1:
            self.direction -= 1
        else:
            self.direction += 1
        self.direction %= 4

    def flip(self, boardColour):
        #Flip the colour of the current square
        self.board[self.position[1]][self.position[0]] = (boardColour+1)%2

    def move(self):
        #Move the ant 1 square in the current direction
        if self.direction == 0:
            self.position[1] += 1
        elif self.direction == 1:
            self.position[0] += 1
        elif self.direction == 2:
            self.position[1] -= 1
        else:
            self.position[0] -= 1

    def displayBoard(self):
        #Display the board
        for i,y in enumerate(self.board):
            for j,x in enumerate(y):
                if i == self.position[1] and j == self.position[0]:
                    print(list("^>v<")[self.direction], end="")
                elif x:
                    print("\u2588", end="")
                else:
                    print(" ", end="")
            print()

#Initialise variables
iterationCount, width, height = 12500, 150, 150

#Initialise the ant
ant1 = ant(0,[int(width/2),int(height/2)], [[0 for _ in range(height)] for _ in range(width)])

for i in range(iterationCount):
    #Take one step in the automaton
    boardColour = ant1.board[ant1.position[1]][ant1.position[0]]
    ant1.turn(boardColour)
    ant1.flip(boardColour)
    ant1.move()

#Print the board
ant1.displayBoard()

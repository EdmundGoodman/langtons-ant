//Edmund Goodman - Creative Commons Attribution-NonCommercial-ShareAlike 2.5
//Langton's Ant
#include<iostream>
extern const int width = 150;
extern const int height = 150;

class Ant {
    int direction;
    int position[2];
    int grid[height][width];

  public:
    void generateGrid() {
      for (int y=0; y<height; y++) {
        for (int x=0; x<width; x++) {
          grid[y][x] = 0;
        }
      }
    }

    void setValues(int d, int p[2]) {
      direction = d;
      position[0] = p[0];
      position[1] = p[1];
    }

    void printGrid() {
      //Print the grid array
      for (int y=0; y<height; y++) {
        for (int x=0; x<width; x++) {
          //std::cout << grid[y][x];
          if (x == position[0] and y == position[1]) {
            char directionIcons[5] = "^>v<";
            std::cout << directionIcons[direction];
          } else if (grid[y][x] == 0) {
            std::cout << " ";
          } else {
            std::cout << "\u2588";
          }
        }
        std::cout << std::endl;
      }
    }

    int getBoardColour() {
      return grid[position[1]][position[0]];
    }

    void turnAnt(int boardColour) {
      if (boardColour == 1) {
        direction -= 1;
      } else {
        direction += 1;
      }
      if (direction<0) {
        direction = 3;
      } else if (direction>3) {
        direction = 0;
      }
    }

    void flipAntSquare(int boardColour) {
      grid[position[1]][position[0]] = (boardColour+1)%2;
    }

    void moveAnt() {
      if (direction == 0) {
        position[1] += 1;
      } else if (direction == 1) {
        position[0] += 1;
      } else if (direction == 2) {
        position[1] -= 1;
      } else {
        position[0] -= 1;
      }
    }
};

int main() {
  int iterations = 12500;
  int startDirection = 0;
  int startPosition[2] = {width/2, height/2};

  Ant ant1;
  ant1.setValues(startDirection, startPosition);
  ant1.generateGrid();

  for (int i=0; i<iterations; i++) {
    int boardColour = ant1.getBoardColour();
    ant1.turnAnt(boardColour);
    ant1.flipAntSquare(boardColour);
    ant1.moveAnt();

  }

  ant1.printGrid();

  return 0;
}

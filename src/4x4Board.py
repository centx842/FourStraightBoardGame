#ML Libraries...
import pygame as pg
import numpy as np
from enum import Enum
import sys

# GLOBAL VARIABLES

# Board Appearence
LINE_COLOR = (0,0,0)
LINE_WIDTH = 10
SQUARE_SIZE = 200
WIDTH = 800
HEIGHT = 800
ROWS = 5
COLS = 5


# Class for Initializing Player Appearence
class Player(Enum):
    NONE = 0
    P1 = 1
    P2 = 2


class FourStraightGame():
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = np.zeros(())
        print("FOUR IN A ROW GAME")
        self.draw_board()

    def draw_board():
        pass

    def make_move():
        pass

    def check_board():
        pass

    def switch_turns():
        pass


def main():

    # Initializing Pygame
    pg.init()
    game = FourStraightGame(ROWS, COLS)
    screen = pg.display.set_mode((game.cols * 100, game.rows * 100))
    pg.display.set_caption("Four Straight Game")
    running = True
    
    # Game Loop
    while(running):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_loop = False
                break
    
    print("Closing Pygame...")
    pg.quit()
        


if __name__ == "__main__":
    main()
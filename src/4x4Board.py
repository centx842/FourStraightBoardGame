#ML Libraries...
import pygame as pg
import numpy as np
from enum import Enum
import sys


# Board Appearence
ROWS = 4
COLS = 4
WIDTH = 800
HEIGHT = 800
BG_COLOR = (128,128,128)
LINE_COLOR = (0,0,0)
LINE_WIDTH = 10
SQUARE_SIZE = WIDTH // ROWS
FPS = 60


# Class for Initializing Player Appearence
class Player(Enum):
    NONE = 0
    P1 = 1
    P2 = 2

class FourStraightGame():
    def __init__(self, screen, rows, cols):
        self.screen = screen
        self.rows = rows
        self.cols = cols
        self.board = [Player.NONE for _ in range(rows * cols)]
        self.tile_clicked = [False for _ in range(rows * cols)]
        self.draw_board()

    def draw_board(self):
        self.screen.fill(BG_COLOR)

        # NOTE: One line drawn down the column and second across the column.
        for row in range(1, self.rows):
            pg.draw.line(self.screen, LINE_COLOR, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE) , LINE_WIDTH)
                
        for col in range(1, self.cols):
            pg.draw.line(self.screen, LINE_COLOR, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        
        # #Drawing lines for the window...
        # pg.draw.line( self.screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH )
        # pg.draw.line( self.screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH )
    

    def make_move(self):
        pass

    def check_board(self):
        pass

    def switch_turns(self):
        pass

    def reset(self):
        pass


def main():

    # Initializing Pygame Window
    pg.init()
    pg.display.set_caption("Four Straight Game")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    game = FourStraightGame(screen, ROWS, COLS)
    running = True
    
    # Game Loop
    while(running):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.type == pg.K_q or event.type == pg.K_ESCAPE:
                    running = False
                if event. type == pg.K_r:
                    # game.reset()
                    pass
            elif event.type == pg.MOUSEBUTTONUP:
                    pos = pg.mouse.get_pos()
                    # game.check_tiles()
                    print(pos)
                    pass
            
        # Update Board and Screen    
        # screen.fill(BG_COLOR)
        game.draw_board()
        pg.display.flip()
        pg.time.delay(int(1000/FPS))

    
    print("Closing Pygame...")
    pg.quit()
        


if __name__ == "__main__":
    main()
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
MSG_COLOR = (0,0,0)
MSG_AREA = (WIDTH // 2, HEIGHT // 2)
MSG_FONT_SIZE = 74
MSG_COORDS = (MSG_AREA[0] // 2, MSG_AREA[1] // 2)
FPS = 60


# Class for Initializing Player Appearence
class Player(Enum):
    NONE = 0
    P1 = 1
    P2 = 2


# Class for Initializing Tiles
class Tiles():
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.p1_color = (255, 0, 0)  # Red
        self.p2_color = (0, 0, 255)  # Blue
        self.tile_clicked = [False for _ in range(rows * cols)]

    def draw_circle(self, row, col, color):
        center = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
        radius = SQUARE_SIZE // 3
        pg.draw.circle(self.screen, color, center, radius)

    def draw_cross(self, row, col, color):
        start_pos1 = (col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4)
        end_pos1 = (col * SQUARE_SIZE + 3 * SQUARE_SIZE // 4, row * SQUARE_SIZE + 3 * SQUARE_SIZE // 4)
        start_pos2 = (col * SQUARE_SIZE + 3 * SQUARE_SIZE // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4)
        end_pos2 = (col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE + 3 * SQUARE_SIZE // 4)
        pg.draw.line(self.screen, color, start_pos1, end_pos1, LINE_WIDTH)
        pg.draw.line(self.screen, color, start_pos2, end_pos2, LINE_WIDTH)

    
# Class for Initializing the Game
class FourStraightGame(Tiles):
    def __init__(self, screen):
        super().__init__(ROWS, COLS)
        self.screen = screen
        self.board = [Player.NONE for _ in range(self.rows * self.cols)]
        self.draw_board()


    def draw_board(self):
        self.screen.fill(BG_COLOR)

        # NOTE: One line drawn down the column and second across the column.
        for row in range(1, self.rows):
            pg.draw.line(self.screen, LINE_COLOR, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE) , LINE_WIDTH)
                
        for col in range(1, self.cols):
            pg.draw.line(self.screen, LINE_COLOR, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, HEIGHT), LINE_WIDTH)


    def check_tiles(self, player, pos):
        col = pos[0] // SQUARE_SIZE
        row = pos[1] // SQUARE_SIZE
        index = row * self.cols + col

        #If this tile is not clicked, then mark it based on the player.
        if self.board[index] == Player.NONE:
            self.board[index] = player
            self.draw_tile(row, col, player)
        #     if self.check_winner(player):
        #         print(f"Player {player} wins!")
        #         self.reset()
        #     else:
            player = self.switch_turns(player)
            print(f"Turn: {player}")

    def draw_tile(self, row, col, player):
        if player == Player.P1:
            self.draw_circle(row, col, self.p1_color)
        elif player == Player.P2:
            self.draw_cross(row, col, self.p2_color)
    
    def switch_turns(self, current_player):
        if current_player == Player.P1:
            return Player.P2
        else:
            return Player.P1

    def reset(self):
        self.board = [Player.NONE for _ in range(self.rows * self.cols)]
        self.draw_board()


def main():

    # Initializing Pygame Window
    pg.init()
    pg.display.set_caption("Four Straight Game")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    game = FourStraightGame(screen)
    running = True

    # ADD: Randomly choose Player 1 and Player 2 and display on screen
    player = np.random.choice([Player.P1, Player.P2])
    print(f"Player {player} starts the game!")
    
    # Display text on screen
    font = pg.font.Font(None, MSG_FONT_SIZE)
    text = font.render(f"Turn: {player}", True, (0, 0, 0))
    text_rect = text.get_rect(center=(100, 100))
    screen.blit(text, text_rect)
    
    # Running Game Loop
    while(running):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.type == pg.K_q or event.type == pg.K_ESCAPE:
                    running = False
                if event. type == pg.K_r:
                    game.reset()
                    pass
            elif event.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()
                print(pos)
                game.check_tiles(player, pos)

        # Update Board and Screen    
        game.draw_board()
        pg.display.flip()
        pg.time.delay(int(1000/FPS))
    
    # Quit Pygame
    print("Closing Pygame...")
    pg.quit()
        


if __name__ == "__main__":
    main()
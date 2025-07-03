# Game Libraries...
import pygame as pg
import numpy as np
from enum import Enum


# Board Appearence
ROWS = 4
COLS = 4
WIDTH = 800
HEIGHT = 900
BG_COLOR = (128,128,128)
LINE_COLOR = (0,0,0)
LINE_WIDTH = 10
LINE_MARGIN = 12
SQUARE_SIZE = WIDTH // ROWS
MSG_FONT_SIZE = 30
MSG_COLOR = (0,0,0)
MSG_AREA = (WIDTH - 100, 100)
SCORE_MSG_COORDS = (WIDTH // 2, 50)
STATUS_MSG_COORDS = (WIDTH // 2, 75)
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


    def draw_circle(self, surface, row, col, color):
        center = ((col * SQUARE_SIZE) + (SQUARE_SIZE // 2), (row * SQUARE_SIZE) + (SQUARE_SIZE // 2))
        radius = SQUARE_SIZE // 3
        pg.draw.circle(surface, color, center, radius)


    def draw_cross(self, surface, row, col, color):
        start_pos1 = ((col * SQUARE_SIZE) + (SQUARE_SIZE // 4), (row * SQUARE_SIZE) + (SQUARE_SIZE // 4))
        end_pos1 = ((col * SQUARE_SIZE) + (3 * SQUARE_SIZE // 4), (row * SQUARE_SIZE) + (3 * SQUARE_SIZE // 4))
        start_pos2 = ((col * SQUARE_SIZE) + (3 * SQUARE_SIZE // 4), (row * SQUARE_SIZE) + (SQUARE_SIZE // 4))
        end_pos2 = ((col * SQUARE_SIZE) + SQUARE_SIZE // 4, (row * SQUARE_SIZE) + (3 * SQUARE_SIZE // 4))
        pg.draw.line(surface, color, start_pos1, end_pos1, LINE_WIDTH)
        pg.draw.line(surface, color, start_pos2, end_pos2, LINE_WIDTH)


# Class for Initializing the Game
class FourStraightGame(Tiles):
    def __init__(self, screen):
        super().__init__(ROWS, COLS)
        self.screen = screen
        self.board = [Player.NONE for _ in range(self.rows * self.cols)]
        self.switch_cond = False
        self.scoreboard_surface = pg.Surface((WIDTH, 100))
        self.gameboard_surface = pg.Surface((WIDTH, 800))
        self.p1_wins = 0
        self.p2_wins = 0
        self.win_condition = False
        self.draw_condition = False
        self.current_player = None  # Track the current player
        self.status_message = ""    # Display game status
        self.draw_board()
        self.draw_scoreboard()


    def draw_board(self):

        self.gameboard_surface.fill(BG_COLOR)
        pg.draw.line(self.gameboard_surface, LINE_COLOR, (0, HEIGHT), (WIDTH, HEIGHT) , LINE_MARGIN)
        
        # NOTE: One line drawn down the row and second across the column.
        for row in range(1, self.rows):
            pg.draw.line(self.gameboard_surface, LINE_COLOR, (0, (row * SQUARE_SIZE)), (WIDTH, (row * SQUARE_SIZE)) , LINE_WIDTH)
                
        for col in range(1, self.cols):
            pg.draw.line(self.gameboard_surface, LINE_COLOR, ((col * SQUARE_SIZE), 0), ((col * SQUARE_SIZE), HEIGHT), LINE_WIDTH)


    def draw_scoreboard(self):
        self.scoreboard_surface.fill(BG_COLOR)
        font = pg.font.Font(None, MSG_FONT_SIZE)
        
        score_text = f"SCOREBOARD --- P1: {self.p1_wins} | P2: {self.p2_wins}"
        status_text = self.status_message

        score_render = font.render(score_text, True, MSG_COLOR)
        status_render = font.render(status_text, True, MSG_COLOR)

        score_rect = score_render.get_rect(center = SCORE_MSG_COORDS)
        status_rect = status_render.get_rect(center= STATUS_MSG_COORDS)       

        self.scoreboard_surface.blit(score_render, score_rect)
        self.scoreboard_surface.blit(status_render, status_rect)

        pg.draw.line(self.scoreboard_surface, LINE_COLOR, (0, 0), (WIDTH, 0), LINE_MARGIN)
        pg.draw.line(self.scoreboard_surface, LINE_COLOR, (0, 100), (WIDTH, 100), LINE_MARGIN)


    def draw_current_XOs(self):
        for row in range(self.rows):
            for col in range(self.cols):
                index = row * self.cols + col
                if self.board[index] == Player.P1:
                    self.draw_circle(self.gameboard_surface, row, col, self.p1_color)
                elif self.board[index] == Player.P2:
                    self.draw_cross(self.gameboard_surface, row, col, self.p2_color)


    def draw_winner(self, player):
         
        #Set color for the winner
        if player == Player.P1:
            color = self.p1_color
        else:
            color = self.p2_color

        # Check rows and draw horizontal line through center
        for row in range(self.rows):
            if all(self.board[row * self.cols + col] == player for col in range(self.cols)):
                y = (row + 0.5) * SQUARE_SIZE
                pg.draw.line(self.gameboard_surface, color, (0, y), (WIDTH, y), 20)
        
        # Check columns and draw vertical line through center
        for col in range(self.cols):
            if all(self.board[row * self.cols + col] == player for row in range(self.rows)):
                x = (col + 0.5) * SQUARE_SIZE
                pg.draw.line(self.gameboard_surface, color, (x, 0), (x, 800), 20)
        
        # Main diagonal (top-left to bottom-right)
        if all(self.board[i * self.cols + i] == player for i in range(self.rows)):
            pg.draw.line(self.gameboard_surface, color, (0, 0), (WIDTH, 800), 20)
        
        # Anti-diagonal (bottom-left to top-right)
        if all(self.board[(self.rows - 1 - i) * self.cols + i] == player for i in range(self.rows)):
            pg.draw.line(self.gameboard_surface, color, (0, 800), (WIDTH, 0), 20)


    def draw_tie_game(self, player):
        
        #Set color for the winner
        if player == Player.P1:
            color = self.p1_color
        else:
            color = self.p2_color

        pg.draw.circle(self.gameboard_surface, color, (WIDTH // 2, 400), 50, 5) 
        self.draw_scoreboard()
        self.screen.blit(self.scoreboard_surface, (0, 0))
        self.screen.blit(self.gameboard_surface, (0, 100))
        pg.display.flip()
        pg.time.delay(2000)
        self.reset()


    def check_tiles(self, player, pos):
        
        if pos[1] >= 100:
            gameboard_pos = (pos[0], pos[1] - 100)
            col = gameboard_pos[0] // SQUARE_SIZE
            row = gameboard_pos[1] // SQUARE_SIZE

            if (0 <= row < self.rows) and (0 <= col < self.cols):
                index = row * self.cols + col
                if self.board[index] == Player.NONE:
                    self.board[index] = player
                    print(f"Player {player.name} clicked on tile ({row}, {col})")
                    self.switch_cond = True
                    self.check_winner(player)
                else:
                    self.switch_cond = False

        if all(self.board[i] != Player.NONE for i in range(self.rows * self.cols)):
            self.draw_tie_game(player)


    def check_winner(self, player):
        
        game_end = False
        self.win_condition = False
        
        # Check rows
        for row in range(self.rows):
            if all(self.board[row * self.cols + col] == player for col in range(self.cols)):
                game_end = True
                self.win_condition = True
                break

        # Check columns
        for col in range(self.cols):
            if all(self.board[row * self.cols + col] == player for row in range(self.rows)):
                game_end = True
                self.win_condition = True
                break

        # Left to Right Diagonals
        if all(self.board[i * self.cols + i] == player for i in range(self.rows)):
            game_end = True
            self.win_condition = True

        # Right to Left Diagonals
        if all(self.board[(self.rows - 1 - i) * self.cols + i] == player for i in range(self.rows)):
            game_end = True
            self.win_condition = True

        if game_end:
            print(f"Player {player.name} wins!")
            self.update_scoreboard(player)
            self.status_message = f"Player {player.name} wins!"
            self.draw_winner(player)
            self.draw_scoreboard()
            self.screen.blit(self.scoreboard_surface, (0, 0))
            self.screen.blit(self.gameboard_surface, (0, 100))
            pg.display.flip()
            pg.time.delay(2000)  # Pause for 2 seconds before resetting
            self.reset()


    def update_scoreboard(self, player):
        if player == Player.P1:
            self.p1_wins += 1
        elif player == Player.P2:
            self.p2_wins += 1
 

    def switch_turns(self, current_player):
        if current_player == Player.P1:
            return Player.P2
        else:
            return Player.P1


    def reset(self):
        self.board = [Player.NONE for _ in range(self.rows * self.cols)]
        self.switch_cond = False
        self.win_condition = False
        self.draw_condition = False
        self.current_player = np.random.choice([Player.P1, Player.P2])
        self.status_message = f"Player {self.current_player.name}'s turn"
        self.draw_board()



def main():

    # Initializing Pygame Window
    pg.init()
    pg.display.set_caption("Four Straight Game")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    game = FourStraightGame(screen)
    running = True

    # Randomly choose Player 1 and Player 2 and display on screen
    player = np.random.choice([Player.P1, Player.P2])
    print(f"Player {player} starts the game!")
    
    # Running Game Loop
    while(running):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key in (pg.K_q, pg.K_ESCAPE):
                    running = False
                if event.key == pg.K_r:
                    game.reset()
            elif event.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()
                game.check_tiles(player, pos)
                if game.switch_cond:
                    player = game.switch_turns(player)
                print(f"Turn: {player}")

        # Draw Function
        game.draw_board()                                   # Update Board and Screen    
        game.draw_scoreboard()                              # Draw player turn text
        game.draw_current_XOs()                             # Update the display
        screen.blit(game.scoreboard_surface, (0, 0))        # Draw Scoreboard Surface
        screen.blit(game.gameboard_surface, (0, 100))       # Draw Gameboard Surface
        
        # Update the display
        pg.display.flip()
        pg.time.delay(int(1000/FPS))
    
    # Quit Pygame
    print("Closing Pygame...")
    pg.quit()
        


if __name__ == "__main__":
    main()
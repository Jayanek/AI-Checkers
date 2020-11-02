import pygame
from .constants import RED, SQURE_SIZE, BLACK, ROWS, COLS

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = 0
        self.red_left = self.white_left = 12
        self.red_king = self.white_king = 0

    def draw_board(self,win):
        win.fill(BLACK)

        for row in range(ROWS):
            for col in range(row%2,ROWS,2):
                pygame.draw.rect(win,RED,(row*SQURE_SIZE, col*SQURE_SIZE, SQURE_SIZE, SQURE_SIZE))
import random
import sys

import pygame


class TicTacToe:
    def __init__(self):
        pygame.init()
        self.size = 300
        self.line_width = 15
        self.board_rows = 3
        self.board_cols = 3
        self.square_size = self.size // self.board_rows
        self.circle_radius = self.square_size // 3
        self.circle_width = 15
        self.cross_width = 25
        self.space = self.square_size // 4

        # Цвета
        self.bg_color = (28, 170, 156)
        self.line_color = (23, 145, 135)
        self.circle_color = (239, 231, 200)
        self.cross_color = (66, 66, 66)

        # Экран
        self.screen = pygame.display.set_mode((self.size, self.size))
        pygame.display.set_caption('Tic Tac Toe')

        # Игровое поле
        self.board = [[0 for _ in range(self.board_cols)] for _ in range(self.board_rows)]

        # Игроки
        self.player = 1  # 1 - игрок, 2 - бот

        # Параметры игры
        self.game_over = False

        # Начальная отрисовка
        self.screen.fill(self.bg_color)
        self.draw_lines()

    def draw_lines(self):
        # Рисуем линии сетки
        for row in range(1, self.board_rows):
            pygame.draw.line(self.screen, self.line_color, (0, row * self.square_size),
                             (self.size, row * self.square_size), self.line_width)
        for col in range(1, self.board_cols):
            pygame.draw.line(self.screen, self.line_color, (col * self.square_size, 0),
                             (col * self.square_size, self.size), self.line_width)

    def draw_figures(self):
        for row in range(self.board_rows):
            for col in range(self.board_cols):
                if self.board[row][col] == 1:
                    pygame.draw.circle(self.screen, self.circle_color, (
                    int(col * self.square_size + self.square_size // 2),
                    int(row * self.square_size + self.square_size // 2)), self.circle_radius, self.circle_width)
                elif self.board[row][col] == 2:
                    pygame.draw.line(self.screen, self.cross_color, (
                    col * self.square_size + self.space, row * self.square_size + self.square_size - self.space), (
                                     col * self.square_size + self.square_size - self.space,
                                     row * self.square_size + self.space), self.cross_width)
                    pygame.draw.line(self.screen, self.cross_color,
                                     (col * self.square_size + self.space, row * self.square_size + self.space), (
                                     col * self.square_size + self.square_size - self.space,
                                     row * self.square_size + self.square_size - self.space), self.cross_width)

    def mark_square(self, row, col, player):
        self.board[row][col] = player

    def available_square(self, row, col):
        return self.board[row][col] == 0

    def is_board_full(self):
        for row in range(self.board_rows):
            for col in range(self.board_cols):
                if self.board[row][col] == 0:
                    return False
        return True

    def check_win(self, player):
        # Проверка по горизонтали
        for row in range(self.board_rows):
            if self.board[row][0] == player and self.board[row][1] == player and self.board[row][2] == player:
                return True
        # Проверка по вертикали
        for col in range(self.board_cols):
            if self.board[0][col] == player and self.board[1][col] == player and self.board[2][col] == player:
                return True
        # Проверка по диагоналям
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return True
        if self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player:
            return True
        return False

    def bot_move(self):
        empty_squares = [(row, col) for row in range(self.board_rows) for col in range(self.board_cols) if
                         self.board[row][col] == 0]
        if empty_squares:
            row, col = random.choice(empty_squares)
            self.mark_square(row, col, self.player)
            if self.check_win(self.player):
                self.game_over = True
            self.player = 1

    def restart(self):
        self.board = [[0 for _ in range(self.board_cols)] for _ in range(self.board_rows)]
        self.player = 1
        self.game_over = False
        self.screen.fill(self.bg_color)
        self.draw_lines()
        self.draw_figures()

    def start_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                    mouseX = event.pos[0]  # x
                    mouseY = event.pos[1]  # y
                    clicked_row = mouseY // self.square_size
                    clicked_col = mouseX // self.square_size

                    if self.available_square(clicked_row, clicked_col):
                        self.mark_square(clicked_row, clicked_col, self.player)
                        if self.check_win(self.player):
                            self.game_over = True
                        self.player = 2
                        self.draw_figures()
                        if not self.game_over:
                            self.bot_move()
                            self.draw_figures()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.restart()
            pygame.display.update()

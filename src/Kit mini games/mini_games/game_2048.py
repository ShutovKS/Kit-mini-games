import random

import pygame


class Game2048:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('2048')

        self.screen = pygame.display.set_mode((400, 400))
        self.size = 4  # Размер доски (4х4)
        self.board = [[0] * self.size for _ in range(self.size)]
        self.add_random_tile()
        self.add_random_tile()

    def add_random_tile(self):
        # Найти все пустые плитки
        empty_tiles = [(r, c) for r in range(self.size) for c in range(self.size) if self.board[r][c] == 0]
        if not empty_tiles:
            return
        r, c = random.choice(empty_tiles)
        self.board[r][c] = 2 if random.random() < 0.9 else 4

    def compress(self, row):
        # Сжимаем строку, удаляя все нули и добавляя их в конец
        new_row = [num for num in row if num != 0]
        new_row += [0] * (self.size - len(new_row))
        return new_row

    def merge(self, row):
        # Объединяем строку, объединяя соседние плитки одного и того же значения
        for i in range(self.size - 1):
            if row[i] == row[i + 1] and row[i] != 0:
                row[i] *= 2
                row[i + 1] = 0
        return row

    def move_left(self):
        moved = False
        for r in range(self.size):
            compressed_row = self.compress(self.board[r])
            merged_row = self.merge(compressed_row)
            new_row = self.compress(merged_row)
            if new_row != self.board[r]:
                moved = True
                self.board[r] = new_row
        if moved:
            self.add_random_tile()

    def move_right(self):
        self.reverse_board()
        self.move_left()
        self.reverse_board()

    def move_up(self):
        self.transpose_board()
        self.move_left()
        self.transpose_board()

    def move_down(self):
        self.transpose_board()
        self.move_right()
        self.transpose_board()

    def reverse_board(self):
        # Переворачиваем каждый ряд доски
        for r in range(self.size):
            self.board[r].reverse()

    def transpose_board(self):
        # Транспонировать доску (преобразовать строки в столбцы и наоборот)
        self.board = [list(row) for row in zip(*self.board)]

    def can_move(self):
        # Проверяем, возможны ли какие-либо ходы
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c] == 0:
                    return True
                if c < self.size - 1 and self.board[r][c] == self.board[r][c + 1]:
                    return True
                if r < self.size - 1 and self.board[r][c] == self.board[r + 1][c]:
                    return True
        return False

    def is_game_over(self):
        # Игра окончена, если ходы невозможны
        return not self.can_move()

    def draw_board(self):
        # Отрисовка доски
        self.screen.fill((187, 173, 160))
        for r in range(self.size):
            for c in range(self.size):
                value = self.board[r][c]
                if value == 0:
                    color = (205, 193, 180)
                else:
                    color = (238, 228, 218)
                pygame.draw.rect(self.screen, color, pygame.Rect(c * 100, r * 100, 100, 100))
                if value != 0:
                    font = pygame.font.Font(None, 55)
                    text = font.render(str(value), True, (119, 110, 101))
                    text_rect = text.get_rect(center=(c * 100 + 50, r * 100 + 50))
                    self.screen.blit(text, text_rect)
        pygame.display.flip()

    def start_game(self):
        # Запуск игры
        running = True
        while running:
            self.draw_board()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        self.move_up()
                    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.move_left()
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.move_down()
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.move_right()
            if self.is_game_over():
                print("Игра закончена!")
                running = False

        pygame.quit()

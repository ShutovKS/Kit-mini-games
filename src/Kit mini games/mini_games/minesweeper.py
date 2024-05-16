import random

import pygame


class Minesweeper:
    def __init__(self):
        self.width = 10
        self.height = 10
        self.mines = 10
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.revealed = [[False for _ in range(self.width)] for _ in range(self.height)]
        self.flags = [[False for _ in range(self.width)] for _ in range(self.height)]
        self.game_over = False
        self.game_won = False

        self.screen = None
        self.cell_size = 20
        self.margin = 5
        self.screen_width = self.width * (self.cell_size + self.margin) + self.margin
        self.screen_height = self.height * (self.cell_size + self.margin) + self.margin

        self.place_mines()
        self.calculate_numbers()

    def place_mines(self):
        mines_placed = 0
        while mines_placed < self.mines:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.grid[y][x] != -1:
                self.grid[y][x] = -1
                mines_placed += 1

    def calculate_numbers(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == -1:
                    continue
                count = 0
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        if 0 <= x + dx < self.width and 0 <= y + dy < self.height:
                            if self.grid[y + dy][x + dx] == -1:
                                count += 1
                self.grid[y][x] = count

    def reveal_cell(self, x, y):
        if self.grid[y][x] == -1:
            self.game_over = True
            return
        self.revealed[y][x] = True
        if self.grid[y][x] == 0:
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if 0 <= x + dx < self.width and 0 <= y + dy < self.height and not self.revealed[y + dy][x + dx]:
                        self.reveal_cell(x + dx, y + dy)

    def check_win(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] != -1 and not self.revealed[y][x]:
                    return False
        self.game_won = True
        return True

    def draw_grid(self):
        for y in range(self.height):
            for x in range(self.width):
                rect = pygame.Rect(x * (self.cell_size + self.margin) + self.margin,
                                   y * (self.cell_size + self.margin) + self.margin,
                                   self.cell_size, self.cell_size)
                if self.revealed[y][x]:
                    if self.grid[y][x] == -1:
                        pygame.draw.rect(self.screen, (255, 0, 0), rect)
                    else:
                        pygame.draw.rect(self.screen, (200, 200, 200), rect)
                        if self.grid[y][x] > 0:
                            font = pygame.font.Font(None, 36)
                            text = font.render(str(self.grid[y][x]), True, (0, 0, 0))
                            self.screen.blit(text, rect.topleft)
                else:
                    pygame.draw.rect(self.screen, (100, 100, 100), rect)
                    if self.flags[y][x]:
                        pygame.draw.rect(self.screen, (0, 255, 0), rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            grid_x = x // (self.cell_size + self.margin)
            grid_y = y // (self.cell_size + self.margin)
            if 0 <= grid_x < self.width and 0 <= grid_y < self.height:
                if event.button == 1:
                    self.reveal_cell(grid_x, grid_y)
                    if self.check_win():
                        self.game_won = True
                elif event.button == 3:
                    self.flags[grid_y][grid_x] = not self.flags[grid_y][grid_x]

    def start_game(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Minesweeper")
        clock = pygame.time.Clock()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if not self.game_over and not self.game_won:
                    self.handle_event(event)

            self.screen.fill((0, 0, 0))
            self.draw_grid()
            pygame.display.flip()
            clock.tick(30)

        pygame.quit()

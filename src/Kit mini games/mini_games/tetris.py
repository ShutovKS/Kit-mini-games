import random

import pygame

# Настройки
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
GRID_WIDTH = SCREEN_WIDTH // BLOCK_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // BLOCK_SIZE

# Определение форм тетромино
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[1, 0, 0], [1, 1, 1]],  # J
    [[0, 0, 1], [1, 1, 1]],  # L
    [[0, 1, 0], [1, 1, 1]]  # T
]

# Цвета форм тетромино
SHAPE_COLORS = [
    (0, 255, 255),
    (255, 255, 0),
    (0, 255, 0),
    (255, 0, 0),
    (0, 0, 255),
    (255, 127, 0),
    (128, 0, 128)
]


class Tetris:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Tetris')
        self.clock = pygame.time.Clock()
        self.grid = self.create_grid()
        self.current_piece = self.get_new_piece()
        self.next_piece = self.get_new_piece()
        self.game_over = False

    def create_grid(self):
        return [[(0, 0, 0) for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

    def get_new_piece(self):
        shape = random.choice(SHAPES)
        color = SHAPE_COLORS[SHAPES.index(shape)]
        return {'shape': shape, 'color': color, 'x': GRID_WIDTH // 2 - len(shape[0]) // 2, 'y': 0}

    def draw_grid(self):
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                pygame.draw.rect(self.screen, self.grid[y][x],
                                 (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
                pygame.draw.rect(self.screen, (128, 128, 128),
                                 (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

    def draw_piece(self, piece):
        for y, row in enumerate(piece['shape']):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, piece['color'],
                                     ((piece['x'] + x) * BLOCK_SIZE, (piece['y'] + y) * BLOCK_SIZE, BLOCK_SIZE,
                                      BLOCK_SIZE), 0)
                    pygame.draw.rect(self.screen, (128, 128, 128),
                                     ((piece['x'] + x) * BLOCK_SIZE, (piece['y'] + y) * BLOCK_SIZE, BLOCK_SIZE,
                                      BLOCK_SIZE), 1)

    def valid_space(self, piece):
        for y, row in enumerate(piece['shape']):
            for x, cell in enumerate(row):
                if cell:
                    if (x + piece['x'] < 0 or x + piece['x'] >= GRID_WIDTH or
                            y + piece['y'] >= GRID_HEIGHT or
                            self.grid[y + piece['y']][x + piece['x']] != (0, 0, 0)):
                        return False
        return True

    def lock_piece(self, piece):
        for y, row in enumerate(piece['shape']):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[y + piece['y']][x + piece['x']] = piece['color']
        self.clear_rows()

    def clear_rows(self):
        rows_to_clear = [y for y in range(GRID_HEIGHT) if all(self.grid[y][x] != (0, 0, 0) for x in range(GRID_WIDTH))]
        for y in rows_to_clear:
            del self.grid[y]
            self.grid.insert(0, [(0, 0, 0) for _ in range(GRID_WIDTH)])

    def rotate_piece(self, piece):
        piece['shape'] = [list(row) for row in zip(*piece['shape'][::-1])]
        if not self.valid_space(piece):
            piece['shape'] = [list(row) for row in zip(*piece['shape'])][::-1]

    def start_game(self):
        while not self.game_over:
            self.screen.fill((0, 0, 0))
            self.draw_grid()
            self.draw_piece(self.current_piece)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.current_piece['x'] -= 1
                        if not self.valid_space(self.current_piece):
                            self.current_piece['x'] += 1
                    elif event.key == pygame.K_RIGHT:
                        self.current_piece['x'] += 1
                        if not self.valid_space(self.current_piece):
                            self.current_piece['x'] -= 1
                    elif event.key == pygame.K_DOWN:
                        self.current_piece['y'] += 1
                        if not self.valid_space(self.current_piece):
                            self.current_piece['y'] -= 1
                    elif event.key == pygame.K_UP:
                        self.rotate_piece(self.current_piece)
            self.current_piece['y'] += 1
            if not self.valid_space(self.current_piece):
                self.current_piece['y'] -= 1
                self.lock_piece(self.current_piece)
                self.current_piece = self.next_piece
                self.next_piece = self.get_new_piece()
                if not self.valid_space(self.current_piece):
                    self.game_over = True

            pygame.display.update()
            self.clock.tick(7)

        pygame.quit()

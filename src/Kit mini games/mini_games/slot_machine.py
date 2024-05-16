import random

import pygame


class SlotMachine:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Slot Machine")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 55)
        self.running = False
        self.result = ["", "", ""]
        self.symbols = ["Cherry", "Lemon", "Orange", "Plum", "Bell", "Bar"]
        self.colors = {
            "Cherry": (255, 0, 0),
            "Lemon": (255, 255, 0),
            "Orange": (255, 165, 0),
            "Plum": (128, 0, 128),
            "Bell": (255, 215, 0),
            "Bar": (0, 0, 255)
        }
        self.message = ""

    def start_game(self):
        self.running = True
        self.message = "Нажмите пробел, чтобы вращаться"
        self.spin()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.handle_event(event)
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

    def spin(self):
        self.result = [random.choice(self.symbols) for _ in range(3)]
        if self.result[0] == self.result[1] == self.result[2]:
            self.message = "Ты победил!"
        else:
            self.message = "Попробуйте еще раз!"

    def draw(self):
        self.screen.fill((0, 0, 0))
        for i, symbol in enumerate(self.result):
            color = self.colors[symbol]
            text = self.font.render(symbol, True, color)
            self.screen.blit(text, (100 + i * 150, 200))
        message_text = self.font.render(self.message, True, (255, 255, 255))
        self.screen.blit(message_text, (100, 400))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and self.running:
                self.spin()

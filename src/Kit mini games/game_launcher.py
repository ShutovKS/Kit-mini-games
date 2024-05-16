import tkinter as tk

from mini_games import game_2048, snake, tetris, tic_tac_toe


class GameLauncher:
    def __init__(self, master):
        self.master = master
        master.title("Программа запуска игр")

        self.game_list = [
            ("2048", self.start_game_2048),
            ("Змейка", self.start_game_snake),
            ("Тетрис", self.start_game_tetris),
            ("Крестики-нолики", self.start_game_tic_tac_toe),
        ]

        self.setup_ui()

    def setup_ui(self):
        self.label = tk.Label(self.master, text="Выберите игру:")
        self.label.pack()

        for game_name, game_function in self.game_list:
            button = tk.Button(self.master, text=game_name, command=game_function)
            button.pack()

    def start_game_2048(self):
        game_2048.Game2048().start_game()
        print("Начинаем игру 2048....")

    def start_game_snake(self):
        snake.SnakeGame().start_game()
        print("Начинаем игру Змейка....")

    def start_game_tetris(self):
        tetris.Tetris().start_game()
        print("Начинаем игру Тетрис....")

    def start_game_tic_tac_toe(self):
        tic_tac_toe.TicTacToe().start_game()
        print("Начинаем игру Крестики-нолики....")

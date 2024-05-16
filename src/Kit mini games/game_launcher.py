import tkinter as tk

from mini_games import game_2048, minesweeper, slot_machine, snake, sum_game, tetris, tic_tac_toe


class GameLauncher:
    def __init__(self, master):
        self.master = master
        master.title("Программа запуска игр")

        self.game_list = [
            ("2048", self.start_game_2048),
            ("Сапер", self.start_game_minesweeper),
            ("Слот-машина", self.start_game_slot_machine),
            ("Змейка", self.start_game_snake),
            ("Сумма", self.start_game_sum_game),
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

    def start_game_minesweeper(self):
        minesweeper.Minesweeper().start_game()
        print("Начинаем игру Сапер....")

    def start_game_slot_machine(self):
        slot_machine.SlotMachine().start_game()
        print("Начинаем игру Слот-машина....")

    def start_game_snake(self):
        snake.SnakeGame().start_game()
        print("Начинаем игру Змейка....")

    def start_game_sum_game(self):
        sum_game.SumGame().start_game()
        print("Начинаем игру Сумма....")

    def start_game_tetris(self):
        tetris.Tetris().start_game()
        print("Начинаем игру Тетрис....")

    def start_game_tic_tac_toe(self):
        tic_tac_toe.TicTacToe().start_game()
        print("Начинаем игру Крестики-нолики....")

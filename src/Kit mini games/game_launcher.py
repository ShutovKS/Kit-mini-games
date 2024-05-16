import tkinter as tk
from tkinter import ttk

from mini_games import game_2048, minesweeper, slot_machine, snake, sum_game, tetris, tic_tac_toe


class GameLauncher:
    def __init__(self, master):
        self.master = master
        master.title("Программа запуска игр")
        master.geometry("440x540")

        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12), padding=10)
        style.configure("TLabel", font=("Helvetica", 14), padding=10)
        style.configure("TFrame", background="#f0f0f0")

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
        main_frame = ttk.Frame(self.master, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        title_label = ttk.Label(main_frame, text="Выберите игру для запуска")
        title_label.pack(pady=10)

        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        for game_name, game_command in self.game_list:
            button = ttk.Button(button_frame, text=game_name, command=game_command)
            button.pack(pady=5, fill=tk.X)

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

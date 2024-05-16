import mini_games.game_2048
import tkinter as tk


class GameLauncher:
    def __init__(self, master):
        self.master = master
        master.title("Программа запуска игр")

        self.game_list = [("2048", self.start_game_2048)]

        self.setup_ui()

    def setup_ui(self):
        self.label = tk.Label(self.master, text="Выберите игру:")
        self.label.pack()

        for game_name, game_function in self.game_list:
            button = tk.Button(self.master, text=game_name, command=game_function)
            button.pack()

    def start_game_2048(self):
        mini_games.game_2048.Game2048().start_game()
        print("Начинаем игру 2048....")

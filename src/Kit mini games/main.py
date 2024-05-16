import tkinter as tk

from game_launcher import GameLauncher

if __name__ == "__main__":
    root = tk.Tk()
    launcher = GameLauncher(root)
    root.mainloop()

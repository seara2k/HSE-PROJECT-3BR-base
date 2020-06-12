import sys
import os
import tkinter as tk
from tkinter import ttk
os.chdir(os.getcwd())
sys.path.append(os.path.abspath(".\\Library"))
from . import gui_mixin as gm
from . import func_mixin as fm
from . import class_database as df

# pylint: disable=C0103


class Main(tk.Tk, gm.main_gui, fm.main_funcs):

    def __init__(self):
        """
        Конструктор окна интерфейса
        Параметры: -
        Возвращает: -
        Автор: Литвинов В.С.
        """
        super().__init__()
        self.database = df.df()
        self.init_GUI()
        self.widgets()
        self.title("DataBase")
        self.geometry("1000x550")
        self.resizable(False, False)
        self.add_img_up = tk.PhotoImage(file=".\\Materials\\arrow_up.gif")
        self.add_img_down = tk.PhotoImage(file=".\\Materials\\arrow_down.gif")
        self.pickle_position = ""
        self.launch_pickle()
        self.title(self.pickle_position)

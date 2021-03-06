import sys
import os
import tkinter as tk
from tkinter import ttk
import configparser
os.chdir(os.getcwd())
sys.path.append(os.path.abspath(".\\Library"))
from . import gui_mixin as gm
from . import func_mixin as fm
from . import class_database as db


# pylint: disable=C0103


class Main(tk.Tk, gm.main_gui, fm.main_funcs):

    def __init__(self):
        """
        Конструктор интерфейса приложения
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """
        super().__init__()
        self.database = db.db()
        self.cfg = configparser.ConfigParser()
        self.cfg.read(".\\settings.ini")
        self.add_img_up = tk.PhotoImage(
            file=".\\Graphics\\Materials\\arrow_up.gif")
        self.add_img_down = tk.PhotoImage(
            file=".\\Graphics\\Materials\\arrow_down.gif")
        self.pickle_position = self.cfg["File"]["last_opened_pickle"]
        self.if_changed = 0
        self.init_GUI()
        self.widgets()
        self.title(self.pickle_position)
        self.geometry(self.cfg["Window sizes"]["main_window"])
        self.resizable(False, False)
        self.launch_pickle()
        self.filtered = 0
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

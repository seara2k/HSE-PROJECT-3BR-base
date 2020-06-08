import sys
import os

from . import gui_mixin as gm
from . import func_mixin as fm

os.chdir(os.path.dirname(os.getcwd()))
sys.path.append(os.path.abspath(".\\Library"))

import tkinter as tk
from tkinter import ttk

from . import child_add as child_add
from . import child_base_stats as child_base_stats
from . import child_summary_table as child_summary_table
from . import child_bar_chart as child_bar_chart
from . import child_histogram as child_histogram
from . import child_box_visk as child_box_visk
from . import child_dispersion as child_dispersion

# pylint: disable=C0103


class Main(tk.Tk, gm.main_gui, fm.main_funcs):

    def __init__(self):
        super().__init__()
        self.init_GUI()
        self.widgets()
        self.title("DataBase")
        self.geometry("1000x550")
        self.resizable(False, False)

    def widgets(self):
        """
        Верхнее меню программы
        """
        self.mainmenu = tk.Menu(self)
        self.config(menu=self.mainmenu)

        filemenu = tk.Menu(self.mainmenu, tearoff=0)
        filemenu.add_command(label="Открыть")
        filemenu.add_command(label="Новый")
        filemenu.add_separator()
        filemenu.add_command(label="Сохранить")
        filemenu.add_command(label="Сохранить как")

        helpmenu = tk.Menu(self.mainmenu, tearoff=0)
        helpmenu.add_command(label="Помощь")
        helpmenu.add_command(label="О программе")

        self.mainmenu.add_cascade(label="Файл", menu=filemenu)
        self.mainmenu.add_cascade(label="Справка", menu=helpmenu)

    def open_add(self):
        child_add.child_add(self)

    def open_base_stats_analysis(self):
        child_base_stats.child_base_stats(self)

    def open_summary_table_analysis(self):
        child_summary_table.child_summary_table(self)

    def open_bar_chart_analysis(self):
        child_bar_chart.child_bar_chart(self)

    def open_histogram_analysis(self):
        child_histogram.child_histogram(self)

    def open_box_visk_analysis(self):
        child_box_visk.child_box_visk(self)

    def open_dispersion_analysis(self):
        child_dispersion.child_dispersion(self)

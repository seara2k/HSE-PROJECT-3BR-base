import sys
import os

from main_gui import main_gui
from main_funcs import main_funcs

os.chdir(os.path.dirname(os.getcwd()))
sys.path.append(os.path.abspath(".\\Library"))
sys.path.append(os.path.abspath(".\\Child_windows"))

import tkinter as tk
from tkinter import ttk

from child_add import child_add
from child_base_stats import child_base_stats
from child_summary_table import child_summary_table
from child_bar_chart import child_bar_chart
from child_histogram import child_histogram
from child_box_visk import child_box_visk
from child_dispersion import child_dispersion

# pylint: disable=C0103


class Main(tk.Frame, main_gui, main_funcs):

    def __init__(self, root):
        super().__init__(root)
        self.init_GUI()
        self.widgets()

    def widgets(self):
        """
        Верхнее меню программы
        """
        mainmenu = tk.Menu(root)
        root.config(menu=mainmenu)

        filemenu = tk.Menu(mainmenu, tearoff=0)
        filemenu.add_command(label="Открыть")
        filemenu.add_command(label="Новый")
        filemenu.add_separator()
        filemenu.add_command(label="Сохранить")
        filemenu.add_command(label="Сохранить как")

        helpmenu = tk.Menu(mainmenu, tearoff=0)
        helpmenu.add_command(label="Помощь")
        helpmenu.add_command(label="О программе")

        mainmenu.add_cascade(label="Файл", menu=filemenu)
        mainmenu.add_cascade(label="Справка", menu=helpmenu)

    def open_add(self):
        child_add(root, app)

    def open_base_stats_analysis(self):
        child_base_stats(root, app)

    def open_summary_table_analysis(self):
        child_summary_table(root, app)

    def open_bar_chart_analysis(self):
        child_bar_chart(root, app)

    def open_histogram_analysis(self):
        child_histogram(root, app)

    def open_box_visk_analysis(self):
        child_box_visk(root, app)

    def open_dispersion_analysis(self):
        child_dispersion(root, app)

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("DataBase")
    root.geometry("1000x550")
    root.resizable(False, False)
    root.mainloop()

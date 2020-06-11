import tkinter as tk
from tkinter import ttk
# pylint: disable=C0103


class child_about_program(tk.Toplevel):

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.title("О программе")
        self.geometry('320x160')
        self.resizable(False, False)
        self.init_GUI()

    def init_GUI(self):

        # Фрейм окна
        lbl_name = tk.Label(self, text='База данных сотрудники')
        lbl_name.pack(side=tk.TOP, pady=5, fill=tk.X)
        lbl_name.config(font=("Courier", 13))

        lbl_author = tk.Label(self, text='Авторы')
        lbl_author.pack(side=tk.TOP, fill=tk.X)
        lbl_author.config(font=(8))

        lbl_slava = tk.Label(self, text='Вячеслав Литвинов')
        lbl_slava.pack(side=tk.TOP, fill=tk.X)

        lbl_andrey = tk.Label(self, text='Андрей Никоненко')
        lbl_andrey.pack(side=tk.TOP, fill=tk.X)

        lbl_alyona = tk.Label(self, text='Алёна Чихватова')
        lbl_alyona.pack(side=tk.TOP,  fill=tk.X)

        lbl_year = tk.Label(self, text='2019-2020')
        lbl_year.pack(side=tk.TOP,  fill=tk.X)
        lbl_year.config(font=(10))

        # Не даёт перейти в другое окно
        self.grab_set()
        self.focus_set()

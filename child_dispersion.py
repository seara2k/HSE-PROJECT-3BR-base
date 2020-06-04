import tkinter as tk
from tkinter import ttk
import numpy as np
import pandas as pd

#pylint: disable=C0103

class child_dispersion(tk.Toplevel):

    def __init__(self, root, app):
        super().__init__(root)
        self.init_GUI()
        self.view = app

    def init_GUI(self):
        self.title("Диаграмма рассеивания")
        self.geometry('340x160')
        self.resizable(False, False)

        # Фрейм окна
        summary_table_group = tk.LabelFrame(self, text='Диаграмма рассеивания')
        summary_table_group.pack(fill=tk.BOTH, expand=1, padx=5, pady=5)

        # Надписи и лейблы с их фреймами
        kach_col_group=tk.Frame(summary_table_group)
        kach_col_group.pack(side=tk.TOP, fill=tk.X)

        lbl_kach_col = tk.Label(kach_col_group, text="Качественный столбец")
        lbl_kach_col.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)

        cb_kach_col = ttk.Combobox(kach_col_group, values=["ФИО","Город"])
        cb_kach_col.pack(side=tk.RIGHT, padx=5, pady=5)
        cb_kach_col.current(0)

        numeral_group_1=tk.Frame(summary_table_group)
        numeral_group_1.pack(side=tk.TOP, fill=tk.X)

        lbl_numeral_1 = tk.Label(numeral_group_1, text="Численный столбец 1")
        lbl_numeral_1.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)

        cb_numeral_1 = ttk.Combobox(numeral_group_1, values=["Номер сотрудника","Телефон"])
        cb_numeral_1.pack(side=tk.RIGHT, padx=5, pady=5)
        cb_numeral_1.current(0)

        numeral_group_2=tk.Frame(summary_table_group)
        numeral_group_2.pack(side=tk.TOP, fill=tk.X)

        lbl_numeral_2 = tk.Label(numeral_group_2, text="Численный столбец 2")
        lbl_numeral_2.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)


        cb_numeral_2 = ttk.Combobox(numeral_group_2, values=["Номер сотрудника","Телефон"])
        cb_numeral_2.pack(side=tk.RIGHT, padx=5, pady=5)
        cb_numeral_2.current(0)

        btn_start = ttk.Button(summary_table_group, text='Начать анализ', command=self.dispersion_analyze)
        btn_start.pack(side=tk.TOP, padx=5, pady=5, fill=tk.X)
        #btn_start.bind('<Button-1>', lambda event: dialog2.view.records(dialog2.entry_quality1.get(),
        #                                                                     dialog2.entry_quality1.get(),
        #                                                                    dialog2.entry_numerical.get()))


        # Не даёт перейти в другое окно
        self.grab_set()
        self.focus_set()

    def dispersion_analyze(self):
        pass

if __name__ == "__main__":
    pass

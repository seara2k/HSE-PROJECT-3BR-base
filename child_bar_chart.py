import tkinter as tk
from tkinter import ttk
import numpy as np
import pandas as pd
import graph_lib

# pylint: disable=C0103


class child_bar_chart(tk.Toplevel):

    def __init__(self, root, app):
        super().__init__(root)
        self.init_GUI()
        self.view = app

    def init_GUI(self):
        self.title("Параметры столбчатой диаграммы")
        self.geometry('340x160')
        self.resizable(False, False)

        # Фрейм окна
        summary_table_group = tk.LabelFrame(
            self, text='Параметры столбчатой диаграммы')
        summary_table_group.pack(fill=tk.BOTH, expand=1, padx=5, pady=5)

        # Надписи и лейблы с их фреймами
        kach_col_1_group = tk.Frame(summary_table_group)
        kach_col_1_group.pack(side=tk.TOP, fill=tk.X)

        lbl_kach_col_1 = tk.Label(
            kach_col_1_group, text="Качественный столбец 1")
        lbl_kach_col_1.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)

        self.cb_kach_col_1 = ttk.Combobox(kach_col_1_group, values=["ФИО", "Город"])
        self.cb_kach_col_1.pack(side=tk.RIGHT, padx=5, pady=5)
        self.cb_kach_col_1.current(0)

        kach_col_2_group = tk.Frame(summary_table_group)
        kach_col_2_group.pack(side=tk.TOP, fill=tk.X)

        lbl_kach_col_2 = tk.Label(
            kach_col_2_group, text="Качественный столбец 2")
        lbl_kach_col_2.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)

        self.cb_kach_col_2 = ttk.Combobox(kach_col_2_group, values=["ФИО", "Город"])
        self.cb_kach_col_2.pack(side=tk.RIGHT, padx=5, pady=5)
        self.cb_kach_col_2.current(0)

        btn_start = ttk.Button(
            summary_table_group, text='Начать анализ', command=self.bar_chart_analyze)
        btn_start.pack(side=tk.TOP, padx=5, pady=5, fill=tk.X)
        # btn_start.bind('<Button-1>', lambda event: dialog2.view.records(dialog2.entry_quality1.get(),
        #                                                                     dialog2.entry_quality1.get(),
        # dialog2.entry_numerical.get()))

        # Не даёт перейти в другое окно
        self.grab_set()
        self.focus_set()

    def bar_chart_analyze(self):
        test1 = graph_lib.translate_to_eng(self.cb_kach_col_1.get())
        test2 = graph_lib.translate_to_eng(self.cb_kach_col_2.get())
        var1 = self.view.get_values(test1)
        var2 = self.view.get_values(test2)
        graph_lib.bar(var1, var2)

if __name__ == "__main__":
    pass

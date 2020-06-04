import tkinter as tk
from tkinter import ttk
import numpy as np
import pandas as pd
#pylint: disable=C0103

class child_base_stats(tk.Toplevel):

    def __init__(self,root,app):
        super().__init__(root)
        self.init_GUI()
        self.view = app

    def init_GUI(self):
        self.title("Параметры базовой статистики")
        self.geometry('200x250')
        self.resizable(False, False)

        # Фрейм окна
        base_stats_group = tk.LabelFrame(self, text='Параметры базовой статистики')
        base_stats_group.pack(fill=tk.BOTH, expand=1, padx=5, pady=5)

        # Надписи и лейблы с их фреймами
        self.cb_id_CheckVar = tk.IntVar(value=0)
        self.cb_id = ttk.Checkbutton(base_stats_group, text="Номер сотрудника",variable = self.cb_id_CheckVar)
        self.cb_id.pack(side=tk.TOP, padx=5, pady=5, fill=tk.X)

        self.cb_full_name_CheckVar = tk.IntVar(value=0)
        self.cb_full_name = ttk.Checkbutton(base_stats_group, text="ФИО",variable = self.cb_full_name_CheckVar)
        self.cb_full_name.pack(side=tk.TOP, padx=5, pady=5, fill=tk.X)

        self.cb_phone_number_CheckVar = tk.IntVar(value=0)
        self.cb_phone_number = ttk.Checkbutton(base_stats_group, text="Телефон",variable = self.cb_phone_number_CheckVar)
        self.cb_phone_number.pack(side=tk.TOP, padx=5, pady=5, fill=tk.X)

        self.cb_city_CheckVar = tk.IntVar(value=0)
        cb_city = ttk.Checkbutton(base_stats_group, text="Город",variable = self.cb_city_CheckVar)
        cb_city.pack(side=tk.TOP, padx=5, pady=5, fill=tk.X)

        cb_empty1 = ttk.Checkbutton(base_stats_group, text="empty")
        cb_empty1.pack(side=tk.TOP, padx=5, pady=5, fill=tk.X)

        cb_empty2 = ttk.Checkbutton(base_stats_group, text="empty")
        cb_empty2.pack(side=tk.TOP, padx=5, pady=5, fill=tk.X)

        btn_start = ttk.Button(base_stats_group, text='Начать анализ', command=self.base_stats_analyze)
        btn_start.pack(side=tk.TOP, padx=5, pady=5, fill=tk.X)

        # Не даёт перейти в другое окно
        self.grab_set()
        self.focus_set()

    def base_stats_analyze(self):
        pass


if __name__ == "__main__":
    pass

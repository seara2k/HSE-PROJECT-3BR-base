import tkinter as tk
from tkinter import ttk
import lib
from . import base_stats_window as base_stats_window
# pylint: disable=C0103


class child_base_stats(tk.Toplevel):

    def __init__(self, parent):
        """
        Конструктор окна выбора элементов базовой статистики
        ----------
        Параметры:
                parent - класс родителя
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """
        super().__init__()
        self.parent = parent
        self.title("Параметры базовой статистики")
        self.geometry('200x280')
        self.resizable(False, False)
        self.init_GUI()

    def init_GUI(self):
        """
        Конструктор интерфейса окна выбора элементов базовой статистики
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """

        # Фрейм окна
        base_stats_group = tk.LabelFrame(
            self, text='Параметры базовой статистики')
        base_stats_group.pack(fill=tk.BOTH, expand=1, padx=5, pady=5)

        # Надписи и лейблы с их фреймами
        self.cb_id_CheckVar = tk.IntVar(value=0)
        self.cb_id = ttk.Checkbutton(
            base_stats_group, text="Номер сотрудника", variable=self.cb_id_CheckVar)
        self.cb_id.pack(side=tk.TOP, padx=5, pady=5, fill=tk.X)

        self.cb_full_name_CheckVar = tk.IntVar(value=0)
        self.cb_full_name = ttk.Checkbutton(
            base_stats_group, text="ФИО", variable=self.cb_full_name_CheckVar)
        self.cb_full_name.pack(side=tk.TOP, padx=5, pady=5, fill=tk.X)

        self.cb_city_CheckVar = tk.IntVar(value=0)
        cb_city = ttk.Checkbutton(
            base_stats_group, text="Город", variable=self.cb_city_CheckVar)
        cb_city.pack(side=tk.TOP, padx=5, pady=5, fill=tk.X)

        self.cb_phone_number_CheckVar = tk.IntVar(value=0)
        self.cb_phone_number = ttk.Checkbutton(
            base_stats_group, text="Номер телефона", variable=self.cb_phone_number_CheckVar)
        self.cb_phone_number.pack(side=tk.TOP, padx=5, pady=5, fill=tk.X)

        self.cb_speciality_CheckVar = tk.IntVar(value=0)
        self.cb_speciality = ttk.Checkbutton(
            base_stats_group, text="Специальность", variable=self.cb_speciality_CheckVar)
        self.cb_speciality.pack(side=tk.TOP, padx=5, pady=5, fill=tk.X)

        self.cb_time_CheckVar = tk.IntVar(value=0)
        cb_time = ttk.Checkbutton(
            base_stats_group, text="Часы", variable=self.cb_time_CheckVar)
        cb_time.pack(side=tk.TOP, padx=5, pady=5, fill=tk.X)

        self.cb_pays_an_hour_CheckVar = tk.IntVar(value=0)
        cb_pays_an_hour = ttk.Checkbutton(
            base_stats_group, text="Зарплата в час", variable=self.cb_pays_an_hour_CheckVar)
        cb_pays_an_hour.pack(side=tk.TOP, padx=5, pady=5, fill=tk.X)

        btn_start = ttk.Button(
            base_stats_group, text='Начать анализ', command=self.base_stats_analyze)
        btn_start.pack(side=tk.TOP, padx=5, pady=5, fill=tk.X)

        # Не даёт перейти в другое окно
        self.grab_set()
        self.focus_set()

    def base_stats_analyze(self):
        """
        Построение диаграммы базовой статистики
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """
        column_names_ru = ["Свойства"]
        if self.cb_id_CheckVar.get() == 1:
            column_names_ru.append("Номер сотрудника")
        if self.cb_full_name_CheckVar.get() == 1:
            column_names_ru.append("ФИО")
        if self.cb_city_CheckVar.get() == 1:
            column_names_ru.append("Город")
        if self.cb_phone_number_CheckVar.get() == 1:
            column_names_ru.append("Номер телефона")
        if self.cb_speciality_CheckVar.get() == 1:
            column_names_ru.append("Специальность")
        if self.cb_time_CheckVar.get() == 1:
            column_names_ru.append("Часы")
        if self.cb_pays_an_hour_CheckVar.get() == 1:
            column_names_ru.append("Зарплата в час")
        self.destroy()    
        base_stats_window.base_stats_window(self.parent, column_names_ru)
        

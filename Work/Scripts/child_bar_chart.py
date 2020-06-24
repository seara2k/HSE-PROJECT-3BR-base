import tkinter as tk
from tkinter import ttk
from . import constants as const
import lib

# pylint: disable=C0103


class child_bar_chart(tk.Toplevel):

    def __init__(self, parent):
        """
        Конструктор окна выбора элементов для столбчатой диаграммы
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
        self.title("Анализ")
        self.geometry(const.bar_chart_variables_window)
        self.resizable(False, False)
        self.init_GUI()

    def init_GUI(self):
        """
        Конструктор интерфейса окна выбора элементов столбчатой диаграммы
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """

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

        self.cb_kach_col_1 = ttk.Combobox(
            kach_col_1_group, values=["Номер сотрудника", "ФИО", "Город",
                                      "Номер телефона", "Специальность"])
        self.cb_kach_col_1.pack(side=tk.RIGHT, padx=5, pady=5)
        self.cb_kach_col_1.current(0)

        kach_col_2_group = tk.Frame(summary_table_group)
        kach_col_2_group.pack(side=tk.TOP, fill=tk.X)

        lbl_kach_col_2 = tk.Label(
            kach_col_2_group, text="Качественный столбец 2")
        lbl_kach_col_2.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)

        self.cb_kach_col_2 = ttk.Combobox(
            kach_col_2_group, values=["Номер сотрудника", "ФИО", "Город",
                                      "Номер телефона", "Специальность"])
        self.cb_kach_col_2.pack(side=tk.RIGHT, padx=5, pady=5)
        self.cb_kach_col_2.current(0)

        btn_start = ttk.Button(
            summary_table_group, text='Начать анализ', command=self.bar_chart_analyze)
        btn_start.pack(side=tk.TOP, padx=5, pady=5, fill=tk.X)

        self.grab_set()
        self.focus_set()

    def bar_chart_analyze(self):
        """
        Построение столбчатой диаграммы
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """
        column_name_1_ru = self.cb_kach_col_1.get()
        column_name_2_ru = self.cb_kach_col_2.get()
        column_name_1_eng = lib.translate_to_eng(column_name_1_ru)
        column_name_2_eng = lib.translate_to_eng(column_name_2_ru)
        var_1 = self.parent.get_values(column_name_1_eng)
        var_2 = self.parent.get_values(column_name_2_eng)
        lib.bar_chart(var_1, var_2, column_name_1_ru, column_name_2_ru)

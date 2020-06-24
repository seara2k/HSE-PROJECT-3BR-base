import tkinter as tk
from tkinter import ttk, messagebox
from . import summary_table_window as summary_table_window
from . import constants as const

# pylint: disable=C0103


class child_summary_table(tk.Toplevel):

    def __init__(self, parent):
        """
        Конструктор окна параметров сводной таблицы
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
        self.title("Параметры сводной таблицы")
        self.geometry(const.summary_table_variables_window)
        self.resizable(False, False)
        self.init_GUI()

    def init_GUI(self):
        """
        Конструктор интерфейса окна параметров сводной таблицы
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """

        # Фрейм окна
        summary_table_group = tk.LabelFrame(
            self, text='Параметры сводной таблицы')
        summary_table_group.pack(fill=tk.BOTH, expand=1, padx=5, pady=5)

        # Надписи и лейблы с их фреймами
        kach_col_1_group = tk.Frame(summary_table_group)
        kach_col_1_group.pack(side=tk.TOP, fill=tk.X)

        lbl_kach_col_1 = tk.Label(
            kach_col_1_group, text="Качественный столбец 1")
        lbl_kach_col_1.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)

        self.cb_kach_col_1 = ttk.Combobox(kach_col_1_group, values=["Номер сотрудника", "ФИО", "Город",
                                                                    "Номер телефона", "Специальность"])
        self.cb_kach_col_1.pack(side=tk.RIGHT, padx=5, pady=5)
        self.cb_kach_col_1.current(0)

        kach_col_2_group = tk.Frame(summary_table_group)
        kach_col_2_group.pack(side=tk.TOP, fill=tk.X)

        lbl_kach_col_2 = tk.Label(
            kach_col_2_group, text="Качественный столбец 2")
        lbl_kach_col_2.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)

        self.cb_kach_col_2 = ttk.Combobox(kach_col_2_group, values=["Номер сотрудника", "ФИО", "Город",
                                                                    "Номер телефона", "Специальность"])
        self.cb_kach_col_2.pack(side=tk.RIGHT, padx=5, pady=5)
        self.cb_kach_col_2.current(0)

        numeral_group = tk.Frame(summary_table_group)
        numeral_group.pack(side=tk.TOP, fill=tk.X)

        lbl_numeral = tk.Label(numeral_group, text="Численный столбец")
        lbl_numeral.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)

        self.cb_numeral = ttk.Combobox(numeral_group, values=[
            "Часы", "Зарплата в час"])
        self.cb_numeral.pack(side=tk.RIGHT, padx=5, pady=5)
        self.cb_numeral.current(0)

        btn_start = ttk.Button(
            summary_table_group, text='Начать анализ', command=self.summary_table_analyze)
        btn_start.pack(side=tk.TOP, padx=5, pady=5, fill=tk.X)

        # Не даёт перейти в другое окно
        self.grab_set()
        self.focus_set()

    def summary_table_analyze(self):
        """
        Построение сводной таблицы
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: -
        """
        column_name_1_ru = self.cb_kach_col_1.get()
        column_name_2_ru = self.cb_kach_col_2.get()
        column_name_3_ru = self.cb_numeral.get()
        if column_name_1_ru == column_name_2_ru:
            messagebox.showerror(
                title="Ошибка ввода",
                message="Качественные столбцы одинаковые",
                parent=self)
            self.grab_set()
            self.focus_set()
        else:
            self.destroy()
            summary_table_window.summary_table_window(
                self.parent, column_name_1_ru, column_name_2_ru, column_name_3_ru)

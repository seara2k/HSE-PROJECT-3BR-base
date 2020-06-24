import tkinter as tk
from tkinter import ttk
from . import constants as const
import graphical_analysis as ga
import list_processing as lp

# pylint: disable=C0103


class child_dispersion(tk.Toplevel):

    def __init__(self, parent):
        """
        Конструктор окна выборов элементов диаграммы рассеияния
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
        self.geometry(const.scatter_variables_window)
        self.resizable(False, False)
        self.init_GUI()

    def init_GUI(self):
        """
        Конструктор интерфейса окна выбора элементов диаграммы рассеяния
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """

        # Фрейм окна
        summary_table_group = tk.LabelFrame(self, text='Диаграмма рассеивания')
        summary_table_group.pack(fill=tk.BOTH, expand=1, padx=5, pady=5)

        # Надписи и лейблы с их фреймами
        kach_col_group = tk.Frame(summary_table_group)
        kach_col_group.pack(side=tk.TOP, fill=tk.X)

        lbl_kach_col = tk.Label(kach_col_group, text="Качественный столбец")
        lbl_kach_col.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)

        self.cb_kach_col = ttk.Combobox(
            kach_col_group, values=["Номер сотрудника", "ФИО", "Город",
                                    "Номер телефона", "Специальность"])
        self.cb_kach_col.pack(side=tk.RIGHT, padx=5, pady=5)
        self.cb_kach_col.current(0)

        numeral_group_1 = tk.Frame(summary_table_group)
        numeral_group_1.pack(side=tk.TOP, fill=tk.X)

        lbl_numeral_1 = tk.Label(numeral_group_1, text="Численный столбец 1")
        lbl_numeral_1.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)

        self.cb_numeral_1 = ttk.Combobox(numeral_group_1, values=[
                                         "Часы", "Зарплата в час"])
        self.cb_numeral_1.pack(side=tk.RIGHT, padx=5, pady=5)
        self.cb_numeral_1.current(0)

        numeral_group_2 = tk.Frame(summary_table_group)
        numeral_group_2.pack(side=tk.TOP, fill=tk.X)

        lbl_numeral_2 = tk.Label(numeral_group_2, text="Численный столбец 2")
        lbl_numeral_2.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)

        self.cb_numeral_2 = ttk.Combobox(numeral_group_2, values=[
                                         "Часы", "Зарплата в час"])
        self.cb_numeral_2.pack(side=tk.RIGHT, padx=5, pady=5)
        self.cb_numeral_2.current(0)

        btn_start = ttk.Button(
            summary_table_group, text='Начать анализ', command=self.dispersion_analyze)
        btn_start.pack(side=tk.TOP, padx=5, pady=5, fill=tk.X)

        # Не даёт перейти в другое окно
        self.grab_set()
        self.focus_set()

    def dispersion_analyze(self):
        """
        Построение диаграммы рассеяния
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """
        column_name_1_ru = self.cb_kach_col.get()
        column_name_2_ru = self.cb_numeral_1.get()
        column_name_3_ru = self.cb_numeral_2.get()
        column_name_1_eng = lp.translate_to_eng(column_name_1_ru)
        column_name_2_eng = lp.translate_to_eng(column_name_2_ru)
        column_name_3_eng = lp.translate_to_eng(column_name_3_ru)
        var_1 = self.parent.get_values(column_name_1_eng)
        var_2 = self.parent.get_values(column_name_2_eng)
        var_3 = self.parent.get_values(column_name_3_eng)
        fixed_var_2 = [int(i) for i in var_2]
        fixed_var_3 = [int(i) for i in var_3]

        ga.scatter(var_1, fixed_var_2, fixed_var_3,
                    column_name_1_ru, column_name_2_ru, column_name_3_ru)

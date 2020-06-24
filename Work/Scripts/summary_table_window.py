import tkinter as tk
from tkinter import ttk
from . import constants as const
import graphical_analysis as ga
import list_processing as lp

# pylint: disable=C0103


class summary_table_window(tk.Toplevel):

    def __init__(self, parent, column_name_1_ru, column_name_2_ru, column_name_3_ru):
        """
        Конструктор окна вывода базовой статистики
        ----------
        Параметры:
                parent - класс родителя
                column_names_ru - названия колонок на русском языке
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """
        super().__init__()
        self.column_name_1_ru = column_name_1_ru
        self.column_name_2_ru = column_name_2_ru
        self.column_name_3_ru = column_name_3_ru
        self.parent = parent
        self.title("Сводная таблица")
        self.geometry(const.summary_table_window)
        self.resizable(False, False)
        self.init_GUI()

    def init_GUI(self):
        """
        Конструктор интерфейса окна базовой статистики
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """

        # Меню
        mainmenu = tk.Menu(self)
        filemenu = tk.Menu(mainmenu, tearoff=0)
        filemenu.add_command(label="Экспорт в excel", command=lambda:self.parent.export_to_excel(self.summary_dataframe,True,True))
        mainmenu.add_cascade(label="Экспорт", menu=filemenu)
        self.config(menu=mainmenu)

        # Фрейм окна
        summary_table_window = tk.LabelFrame(
            self, text="Параметры")
        summary_table_window.pack(fill=tk.BOTH, expand=1, padx=5, pady=5)

        # Размер, ширина колонок и таблица
        if self.parent.filtered == 0:
            self.summary_dataframe = ga.summary(
                self.parent.database.dataframe, self.column_name_1_ru, self.column_name_2_ru, self.column_name_3_ru)
        else:
            self.summary_dataframe = ga.summary(
                self.parent.filtered_dataframe, self.column_name_1_ru, self.column_name_2_ru, self.column_name_3_ru)

        columns_index = list(self.summary_dataframe.index)
        columns_fixed = list(self.summary_dataframe)
        columns_fixed.insert(0, self.column_name_2_ru)
        number_of_columns = len(columns_fixed)
        self.width = lp.good_looking_columns(number_of_columns)
        self.tree = ttk.Treeview(
            summary_table_window, columns=columns_fixed, height=20, show="headings")

        for i in range(len(columns_fixed)):
            self.tree.column(columns_fixed[i],
                             width=self.width, anchor=tk.CENTER)
            self.tree.heading(columns_fixed[
                              i], text=columns_fixed[i])
        self.tree.insert("", "end", values=[self.column_name_1_ru])

        for i in range(len(self.summary_dataframe.index)):
            row = sum(self.summary_dataframe.iloc[[i]].values.tolist(), [])
            row.insert(0, columns_index[i])
            for i in range(len(row)):
                if row[i] != row[i]:
                    row[i] = "-"
            self.tree.insert("", "end", values=row)

        tree_scrollbar_vertical = tk.Scrollbar(
            summary_table_window, orient="vertical", command=self.tree.yview)
        tree_scrollbar_vertical.pack(side=tk.RIGHT, fill="y")

        tree_scrollbar_horizontal = tk.Scrollbar(
            summary_table_window, orient="horizontal", command=self.tree.xview)
        tree_scrollbar_horizontal.pack(side=tk.BOTTOM, fill="x")

        self.tree.pack(pady=5)
        self.grab_set()
        self.focus_set()

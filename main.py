# -*- coding: utf-8 -*-
from tkinter import Tk, ttk, messagebox
import tkinter as tk
from tkinter.ttk import Checkbutton
import numpy as np
import pandas as pd
# import get_data
# import firsttab
# import secondtab
import sqlite3
from Child_Analysis import Child_Analysis
from Child_Add import Child_Add


def get_filtr():
    pass


def export():
    pass


def editing():
    pass


def deleting():  # не работает пока что
    item = tree.selection()[0]
    tree.delete(item)


def analyze1():
    messagebox.showinfo(
        'Предупреждение', 'Невозможно произвести анализ с данными параметрами')


def analyze2():
    messagebox.showinfo(
        'Предупреждение', 'Невозможно произвести анализ с данными параметрами')


def analyze3():
    messagebox.showinfo(
        'Предупреждение', 'Невозможно произвести анализ с данными параметрами')


def analyze4():
    messagebox.showinfo(
        'Предупреждение', 'Невозможно произвести анализ с данными параметрами')


def analyze5():
    messagebox.showinfo(
        'Предупреждение', 'Невозможно произвести анализ с данными параметрами')


def analyze6():
    messagebox.showinfo(
        'Предупреждение', 'Невозможно произвести анализ с данными параметрами')


class Main(tk.Frame):

    def __init__(self, root):
        super().__init__(root)
        self.init_GUI()
        self.db = db
        self.widgets()

    def widgets(self):
        """
        Строка меню
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

    def init_GUI(self):
        """
        Инициализация интерфейса
        """

        # design
        # Разобраться со стилями надо
        ttk.Style().configure("TNotebook.Tab", padding=('50', '5'))
        style = ttk.Style()
        style.layout("Tab",
                     [('Notebook.tab', {'sticky': 'nswe', 'children':
                                        [('Notebook.padding', {'side': 'top', 'sticky': 'nswe', 'children':
                                                               #[('Notebook.focus', {'side': 'top', 'sticky': 'nswe', 'children':
                                                               [('Notebook.label', {
                                                                 'side': 'top', 'sticky': ''})],
                                                               #})],
                                                               })],
                                        })]
                     )

        # Верхняя часть программы
        toolbar = tk.Frame(bd=10)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        # Фрейм добавки
        editing_group = tk.LabelFrame(toolbar, text='Таблица')
        editing_group.pack(side=tk.LEFT, padx=0, pady=0,
                           anchor=tk.N, fill=tk.Y)

        eg_btn_add = tk.Button(
            editing_group, text='Добавить строку', command=self.open_Add)
        eg_btn_add.pack(side=tk.TOP, padx=5, pady=5, fill=tk.X, expand=1)

        eg_btn_edit = tk.Button(
            editing_group, text="Изменить", command=editing)
        eg_btn_edit.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=1)

        eg_btn_export = tk.Button(
            editing_group, text="Экспорт", command=export)
        eg_btn_export.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=1)

        eg_btn_delete = tk.Button(
            editing_group, text="Удалить", command=deleting)
        eg_btn_delete.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=1)

        # Фрейм анализов
        analysis_group = tk.LabelFrame(toolbar, text='Метод анализа')
        analysis_group.pack(side=tk.LEFT, padx=10, pady=0,
                            anchor=tk.N, fill=tk.Y)

        ag_cb_analys = ttk.Combobox(analysis_group,
                                    values=["Базовая статистика",
                                            "Сводная таблица",
                                            "Столбчатая диаграмма",
                                            "Гистограмма",
                                            "Диаграмма Бокса-Вискера",
                                            "Диаграмма рассеивания"], width=25)
        ag_cb_analys.pack(side=tk.TOP, padx=5, pady=5)
        ag_cb_analys.current(0)

        ag_btn_choose = tk.Button(
            analysis_group, text="Выбрать", command=get_analysis)
        ag_btn_choose.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=1)

        ag_btn_export = tk.Button(
            analysis_group, text="Экспорт", command=export)
        ag_btn_export.pack(side=tk.RIGHT, padx=5, pady=5, fill=tk.X, expand=1)

        # Фрейм фильтров
        filtr_group = tk.LabelFrame(toolbar, text='Фильтры')
        filtr_group.pack(side=tk.LEFT, padx=0, pady=0, anchor=tk.N, fill=tk.Y)

        fg_cb_filter = ttk.Combobox(filtr_group,
                                    values=["Номер сотрудника",
                                            "ФИО",
                                            "Номер телефона",
                                            "Город"])
        fg_cb_filter.pack(side=tk.TOP, padx=5, pady=5)
        fg_cb_filter.current(0)

        fg_btn_filtr = tk.Button(
            filtr_group, text="Отфильтровать", command=get_filtr)
        fg_btn_filtr.pack(side=tk.TOP, padx=5, pady=5)

        # Фрейм таблицы и табов
        bottom_frame = tk.Frame(bd=10)
        tab_parent = ttk.Notebook(bottom_frame)
        tab_1 = ttk.Frame(tab_parent, padding=10)
        tab_2 = ttk.Frame(tab_parent, padding=10)
        tab_3 = ttk.Frame(tab_parent, padding=10)
        tab_parent.add(tab_1, text="Сотрудник")
        tab_parent.add(tab_2, text="Часы")
        tab_parent.add(tab_3, text="Работы")
        tab_parent.pack()
        bottom_frame.pack()

        # Таблицы и скролл бары к ним
        self.tree_1 = ttk.Treeview(tab_1, columns=(
            'ID', 'Full_Name', "Phone_Number"), height=20, show="headings")

        self.tree_1.column('ID', width=325, anchor=tk.CENTER)
        self.tree_1.column('Full_Name', width=325, anchor=tk.CENTER)
        self.tree_1.column("Phone_Number", width=325, anchor=tk.CENTER)

        self.tree_1.heading("ID", text="Номер сотрудника")
        self.tree_1.heading("Full_Name", text='ФИО')
        self.tree_1.heading("Phone_Number", text="Номер телефона")

        tree_scrollbar_vertical_1 = tk.Scrollbar(
            tab_1, orient="vertical", command=self.tree_1.yview)
        tree_scrollbar_vertical_1.pack(side="right", fill="y")

        tree_scrollbar_horizontal_1 = tk.Scrollbar(
            tab_1, orient="horizontal", command=self.tree_1.xview)
        tree_scrollbar_horizontal_1.pack(side="bottom", fill="x")

        self.tree_1.pack()

        self.tree_2 = ttk.Treeview(tab_2, columns=(
            "ID", "Specialty", "Time"), height=20, show="headings")

        self.tree_2.column("ID", width=325, anchor=tk.CENTER)
        self.tree_2.column("Specialty", width=325, anchor=tk.CENTER)
        self.tree_2.column("Time", width=325, anchor=tk.CENTER)

        self.tree_2.heading("ID", text='Номер сотрудника')
        self.tree_2.heading("Specialty", text="Специальность")
        self.tree_2.heading("Time", text="Часы")

        tree_scrollbar_vertical_2 = tk.Scrollbar(
            tab_2, orient="vertical", command=self.tree_2.yview)
        tree_scrollbar_vertical_2.pack(side="right", fill="y")

        tree_scrollbar_horizontal_2 = tk.Scrollbar(
            tab_2, orient="horizontal", command=self.tree_2.xview)
        tree_scrollbar_horizontal_2.pack(side="bottom", fill="x")

        self.tree_2.pack()

        self.tree_3 = ttk.Treeview(tab_3, columns=(
            "City", "Specialty", "Pays_An_Hour"), height=20, show="headings")
        self.tree_3.column("City", width=325, anchor=tk.CENTER)
        self.tree_3.column("Specialty", width=325, anchor=tk.CENTER)
        self.tree_3.column("Pays_An_Hour", width=325, anchor=tk.CENTER)

        self.tree_3.heading("City", text="Город")
        self.tree_3.heading("Specialty", text="Специальность")
        self.tree_3.heading("Pays_An_Hour", text="Зарплата в час")

        tree_scrollbar_vertical_3 = tk.Scrollbar(
            tab_3, orient="vertical", command=self.tree_3.yview)
        tree_scrollbar_vertical_3.pack(side="right", fill="y")

        tree_scrollbar_horizontal_3 = tk.Scrollbar(
            tab_3, orient="horizontal", command=self.tree_3.xview)
        tree_scrollbar_horizontal_3.pack(side="bottom", fill="x")

        self.tree_3.pack()

    # def record(self, ID, Full_Name, Phone_Number, City):
    #     self.db.insert_data(ID, Full_Name, Phone_Number, City)
    #     self.view_records()

    # def view_records(self):
    #     self.db.c.execute('''SELECT * FROM database''')
    #     [self.tree_1.delete(i) for i in self.tree_1.get_children()]
    #     [self.tree_1.insert('', 'end', values=row)
    #      for row in self.db.c.fetchall()]

    def get_analysis():
        pass

    def open_Add(self):
        Child_Add(root, app)

    def open_Analysis(self):
        Child_Analysis(root, app)


# class DB:

#     def __init__(self):

#         self.conn = sqlite3.connect("database.pickle")
#         self.c = self.conn.cursor()
#         self.c.execute(
#             '''CREATE TABLE IF NOT EXISTS database(ID integer primary key,Full_Name text,Phone_Number text,City text)''')
#         self.conn.commit()

#     def insert_data(self, ID, Full_Name, Phone_Number, City):
#         self.c.execute(
#             '''INSERT INTO database(ID,Full_Name,Phone_Number,City) VALUES (?,?,?,?)''',
#             (ID, Full_Name, Phone_Number, City))
#         self.conn.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("I LOVE POLYAKOV")
    root.geometry("1000x550")
    root.resizable(False, False)
    root.mainloop()

# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
# import numpy as np
# import pandas as pd

from child_add import child_add
from child_base_stats import child_base_stats
from child_summary_table import child_summary_table
from child_bar_chart import child_bar_chart
from child_histogram import child_histogram
from child_box_visk import child_box_visk
from child_dispersion import child_dispersion
# pylint: disable=C0103


class Main(tk.Frame):

    def __init__(self, root):
        super().__init__(root)
        self.init_GUI()
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

        eg_btn_add = ttk.Button(
            editing_group, text='Добавить строку', command=self.open_add)
        eg_btn_add.pack(side=tk.TOP, padx=5, pady=5, fill=tk.X, expand=1)

        eg_btn_edit = ttk.Button(
            editing_group, text="Изменить")
        eg_btn_edit.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=1)

        eg_btn_export = ttk.Button(
            editing_group, text="Экспорт")
        eg_btn_export.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=1)

        eg_btn_delete = ttk.Button(
            editing_group, text="Удалить", command=self.delete)
        eg_btn_delete.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=1)

        # Фрейм анализов
        analysis_group = tk.LabelFrame(toolbar, text='Метод анализа')
        analysis_group.pack(side=tk.LEFT, padx=10, pady=0,
                            anchor=tk.N, fill=tk.Y)

        self.ag_cb_analys = ttk.Combobox(analysis_group,
                                         values=["Базовая статистика",
                                                 "Сводная таблица",
                                                 "Столбчатая диаграмма",
                                                 "Гистограмма",
                                                 "Диаграмма Бокса-Вискера",
                                                 "Диаграмма рассеивания"], width=25)
        self.ag_cb_analys.pack(side=tk.TOP, padx=5, pady=5)
        self.ag_cb_analys.current(0)

        ag_btn_choose = ttk.Button(
            analysis_group, text="Выбрать", command=self.choose_analysis_function)
        ag_btn_choose.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=1)
        ag_btn_export = ttk.Button(
            analysis_group, text="Экспорт")
        ag_btn_export.pack(side=tk.RIGHT, padx=5, pady=5, fill=tk.X, expand=1)

        # Фрейм фильтров
        filtr_group = tk.LabelFrame(toolbar, text='Фильтры')
        filtr_group.pack(side=tk.LEFT, padx=0, pady=0, anchor=tk.N, fill=tk.Y)

        self.fg_cb_filter = ttk.Combobox(filtr_group,
                                         values=["Номер сотрудника",
                                                 "ФИО",
                                                 "Номер телефона",
                                                 "Город"])
        self.fg_cb_filter.pack(side=tk.TOP, padx=5, pady=5)
        self.fg_cb_filter.current(0)

        self.fg_btn_filtr = ttk.Button(
            filtr_group, text="Отфильтровать")
        self.fg_btn_filtr.pack(side=tk.TOP, padx=5, pady=5)

        # Фрейм таблицы и табов
        bottom_frame = tk.Frame(bd=10)
        self.tab_parent = ttk.Notebook(bottom_frame)
        tab_all = ttk.Frame(self.tab_parent, padding=10)
        tab_1 = ttk.Frame(self.tab_parent, padding=10)
        tab_2 = ttk.Frame(self.tab_parent, padding=10)
        tab_3 = ttk.Frame(self.tab_parent, padding=10)
        self.tab_parent.add(tab_all, text="Полная таблица")
        self.tab_parent.add(tab_1, text="Сотрудник")
        self.tab_parent.add(tab_2, text="Часы")
        self.tab_parent.add(tab_3, text="Работы")
        self.tab_parent.pack()
        bottom_frame.pack()

        # Таблицы и скролл бары к ним
        self.tree_all = ttk.Treeview(tab_all, columns=(
            "ID", "Full_Name", "City", "Phone_Number", "Speciality", "Time", "Pays_An_Hour"),
            height=20, show="headings")

        self.tree_all.column('ID', width=135, anchor=tk.CENTER)
        self.tree_all.column('Full_Name', width=135, anchor=tk.CENTER)
        self.tree_all.column('City', width=135, anchor=tk.CENTER)
        self.tree_all.column("Phone_Number", width=135, anchor=tk.CENTER)
        self.tree_all.column("Speciality", width=135, anchor=tk.CENTER)
        self.tree_all.column("Time", width=135, anchor=tk.CENTER)
        self.tree_all.column("Pays_An_Hour", width=135, anchor=tk.CENTER)

        self.tree_all.heading("ID", text="Номер сотрудника", command=lambda:
                              self.sort(self.tree_all, "ID", False))
        self.tree_all.heading("Full_Name", text='ФИО', command=lambda:
                              self.sort(self.tree_all, "Full_Name", False))
        self.tree_all.heading("City", text="Город", command=lambda:
                              self.sort(self.tree_all, "City", False))
        self.tree_all.heading("Phone_Number", text="Номер телефона", command=lambda:
                              self.sort(self.tree_all, "Phone_Number", False))
        self.tree_all.heading("Speciality", text="Специальность", command=lambda:
                              self.sort(self.tree_all, "Speciality", False))
        self.tree_all.heading("Time", text="Часы", command=lambda:
                              self.sort(self.tree_all, "Time", False))
        self.tree_all.heading("Pays_An_Hour", text="Зарплата в час", command=lambda:
                              self.sort(self.tree_all, "Pays_An_Hour", False))

        tree_scrollbar_vertical_all = tk.Scrollbar(
            tab_all, orient="vertical", command=self.tree_all.yview)
        tree_scrollbar_vertical_all.pack(side="right", fill="y")
        tree_scrollbar_horizontal_all = tk.Scrollbar(
            tab_all, orient="horizontal", command=self.tree_all.xview)
        tree_scrollbar_horizontal_all.pack(side="bottom", fill="x")

        self.tree_all.pack()

        self.tree_1 = ttk.Treeview(tab_1, columns=(
            'ID', 'Full_Name', "Phone_Number"), height=20, show="headings")

        self.tree_1.column('ID', width=315, anchor=tk.CENTER)
        self.tree_1.column('Full_Name', width=315, anchor=tk.CENTER)
        self.tree_1.column("Phone_Number", width=315, anchor=tk.CENTER)

        self.tree_1.heading("ID", text="Номер сотрудника", command=lambda:
                            self.sort(self.tree_1, "ID", False))
        self.tree_1.heading("Full_Name", text='ФИО', command=lambda:
                            self.sort(self.tree_1, "Full_Name", False))
        self.tree_1.heading("Phone_Number", text="Номер телефона", command=lambda:
                            self.sort(self.tree_1, "Phone_Number", False))

        tree_scrollbar_vertical_1 = tk.Scrollbar(
            tab_1, orient="vertical", command=self.tree_1.yview)
        tree_scrollbar_vertical_1.pack(side="right", fill="y")

        tree_scrollbar_horizontal_1 = tk.Scrollbar(
            tab_1, orient="horizontal", command=self.tree_1.xview)
        tree_scrollbar_horizontal_1.pack(side="bottom", fill="x")

        self.tree_1.pack()

        self.tree_2 = ttk.Treeview(tab_2, columns=(
            "ID", "Speciality", "Time"), height=20, show="headings")

        self.tree_2.column("ID", width=315, anchor=tk.CENTER)
        self.tree_2.column("Speciality", width=315, anchor=tk.CENTER)
        self.tree_2.column("Time", width=315, anchor=tk.CENTER)

        self.tree_2.heading("ID", text='Номер сотрудника', command=lambda:
                            self.sort(self.tree_2, "ID", False))
        self.tree_2.heading("Speciality", text="Специальность", command=lambda:
                            self.sort(self.tree_2, "Speciality", False))
        self.tree_2.heading("Time", text="Часы", command=lambda:
                            self.sort(self.tree_2, "Time", False))

        tree_scrollbar_vertical_2 = tk.Scrollbar(
            tab_2, orient="vertical", command=self.tree_2.yview)
        tree_scrollbar_vertical_2.pack(side="right", fill="y")

        tree_scrollbar_horizontal_2 = tk.Scrollbar(
            tab_2, orient="horizontal", command=self.tree_2.xview)
        tree_scrollbar_horizontal_2.pack(side="bottom", fill="x")

        self.tree_2.pack()

        self.tree_3 = ttk.Treeview(tab_3, columns=(
            "City", "Speciality", "Pays_An_Hour"), height=20, show="headings")
        self.tree_3.column("City", width=315, anchor=tk.CENTER)
        self.tree_3.column("Speciality", width=315, anchor=tk.CENTER)
        self.tree_3.column("Pays_An_Hour", width=315, anchor=tk.CENTER)

        self.tree_3.heading("City", text="Город", command=lambda:
                            self.sort(self.tree_3, "City", False))
        self.tree_3.heading("Speciality", text="Специальность", command=lambda:
                            self.sort(self.tree_3, "Speciality", False))
        self.tree_3.heading("Pays_An_Hour", text="Зарплата в час", command=lambda:
                            self.sort(self.tree_3, "Pays_An_Hour", False))

        tree_scrollbar_vertical_3 = tk.Scrollbar(
            tab_3, orient="vertical", command=self.tree_3.yview)
        tree_scrollbar_vertical_3.pack(side="right", fill="y")

        tree_scrollbar_horizontal_3 = tk.Scrollbar(
            tab_3, orient="horizontal", command=self.tree_3.xview)
        tree_scrollbar_horizontal_3.pack(side="bottom", fill="x")

        self.tree_3.pack()

    def record(self, input_ID, input_Full_Name, input_Phone_Number, input_City,
               input_Speciality, input_Time, input_Pays_An_Hour):
        """
        Запись данных в таблицы
        """
        self.tree_all.insert("", "end", values=(
            input_ID, input_Full_Name, input_City, input_Phone_Number, input_Speciality, input_Time,
            input_Pays_An_Hour))
        self.tree_1.insert("", "end", values=(
            input_ID, input_Full_Name, input_Phone_Number))

        self.tree_2.insert("", "end", values=(
            input_ID, input_Speciality, input_Time))

        self.tree_3.insert("", "end", values=(
            input_City, input_Speciality, input_Pays_An_Hour))

    def sort(self, tv, col, reverse):
        """
        Сортировка при нажатии на колонку
        """
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)

        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)
        self.add_img_up = tk.PhotoImage(file="arrow_up.gif")
        self.add_img_down = tk.PhotoImage(file="arrow_down.gif")
        if reverse:
            tv.heading(col, image=self.add_img_up)
        else:
            tv.heading(col, image=self.add_img_down)
        # reverse sort next time
        tv.heading(col, command=lambda:
                   self.sort(tv, col, not reverse))

    def delete(self):
        """
        Удаление элементов таблицы
        """
        if self.tab_parent.tab(self.tab_parent.select(), "text") == "Полная таблица":
            tree = "tree_1"
        elif self.tab_parent.tab(self.tab_parent.select(), "text") == "Сотрудник":
            tree = "tree_1"
        elif self.tab_parent.tab(self.tab_parent.select(), "text") == "Часы":
            tree = "tree_2"
        elif self.tab_parent.tab(self.tab_parent.select(), "text") == "Работы":
            tree = "tree_3"
        [getattr(self, tree).delete(row)
         for row in getattr(self, tree).selection()]

    def choose_analysis_function(self):
        chosen_analysis = self.ag_cb_analys.get()
        print(chosen_analysis)
        if chosen_analysis == "Базовая статистика":
            self.open_base_stats_analysis()
        elif chosen_analysis == 'Сводная таблица':
            self.open_summary_table_analysis()
        elif chosen_analysis == 'Столбчатая диаграмма':
            self.open_bar_chart_analysis()
        elif chosen_analysis == 'Гистограмма':
            self.open_histogram_analysis()
        elif chosen_analysis == 'Диаграмма Бокса-Вискера':
            self.open_box_visk_analysis()
        elif chosen_analysis == 'Диаграмма рассеивания':
            self.open_dispersion_analysis()

    def get_values(self, column_name):
        """
        Получает данные из колонки
        """
        self.column_name_values = []
        for line in self.tree_all.get_children():
            self.column_name_values.append(
                self.tree_all.set(line, column_name))
            # print(self.tree_1.item(line)['values'])
        #     for value in self.tree_1.item(line)['values']:

        return self.column_name_values

    def open_add(self):
        child_add(root, app)

    def open_base_stats_analysis(self):
        child_base_stats(root, app)

    def open_summary_table_analysis(self):
        child_summary_table(root, app)

    def open_bar_chart_analysis(self):
        child_bar_chart(root, app)

    def open_histogram_analysis(self):
        child_histogram(root, app)

    def open_box_visk_analysis(self):
        child_box_visk(root, app)

    def open_dispersion_analysis(self):
        child_dispersion(root, app)

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("DataBase")
    root.geometry("1000x550")
    root.resizable(False, False)
    root.mainloop()

import tkinter as tk
from tkinter import ttk
import lib

# pylint: disable=C0103


class child_base_stats(tk.Toplevel):

    def __init__(self, root, app):
        super().__init__(root)
        self.init_GUI()
        self.view = app
        self.root = root

    def init_GUI(self):
        self.title("Параметры базовой статистики")
        self.geometry('200x280')
        self.resizable(False, False)

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
            base_stats_group, text="Телефон", variable=self.cb_phone_number_CheckVar)
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
        column_names_ru = ["Свойства"]
        if self.cb_id_CheckVar.get() == 1:
            column_names_ru.append("Номер сотрудника")
        if self.cb_full_name_CheckVar.get() == 1:
            column_names_ru.append("ФИО")
        if self.cb_city_CheckVar.get() == 1:
            column_names_ru.append("Город")
        if self.cb_phone_number_CheckVar.get() == 1:
            column_names_ru.append("Телефон")
        if self.cb_speciality_CheckVar.get() == 1:
            column_names_ru.append("Специальность")
        if self.cb_time_CheckVar.get() == 1:
            column_names_ru.append("Часы")
        if self.cb_pays_an_hour_CheckVar.get() == 1:
            column_names_ru.append("Зарплата в час")
        base_stats_window(self.root, self.view, column_names_ru)


class base_stats_window(tk.Toplevel):

    def __init__(self, root, app, column_names_ru):
        super().__init__(root)
        self.column_names_ru = column_names_ru
        self.view = app
        self.init_GUI()

    def init_GUI(self):
        self.title("Базовая статистика")
        self.geometry("1000x350")
        self.resizable(False, False)

        # Фрейм окна
        base_stats_window = tk.LabelFrame(
            self, text="Параметры")
        base_stats_window.pack(fill=tk.BOTH, expand=1, padx=5, pady=5)

        # Размер, ширина колонок и таблица
        number_of_columns = len(self.column_names_ru)
        self.width = lib.good_looking_columns(number_of_columns)
        self.column_names_eng = [lib.translate_to_eng(
            self.column_names_ru[x]) for x in range(number_of_columns)]
        self.tree = ttk.Treeview(
            base_stats_window, columns=self.column_names_eng, height=20, show="headings")
        for i in range(len(self.column_names_eng)):
            self.tree.column(self.column_names_eng[i],
                             width=self.width, anchor=tk.CENTER)
            self.tree.heading(self.column_names_eng[i], text=self.column_names_ru[i], command=lambda:
                              self.sort(self.tree, self.column_names_eng[i], False))

        tree_scrollbar_vertical = tk.Scrollbar(
            base_stats_window, orient="vertical", command=self.tree.yview)
        tree_scrollbar_vertical.pack(side=tk.RIGHT, fill="y")

        tree_scrollbar_horizontal = tk.Scrollbar(
            base_stats_window, orient="horizontal", command=self.tree.xview)
        tree_scrollbar_horizontal.pack(side=tk.BOTTOM, fill="x")

        self.tree.pack(pady=5)
        self.clever_insert_values()
        # Не даёт перейти в другое окно
        self.grab_set()
        self.focus_set()

    def sort(self, tv, col, reverse):
        """
        Сортировка при нажатии на колонку
        """
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)

        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)
        self.add_img_up = tk.PhotoImage(file=".\\Mats\\arrow_up.gif")
        self.add_img_down = tk.PhotoImage(file=".\\Mats\\arrow_down.gif")
        if reverse:
            tv.heading(col, image=self.add_img_up)
        else:
            tv.heading(col, image=self.add_img_down)
        # reverse sort next time
        tv.heading(col, command=lambda:
                   self.sort(tv, col, not reverse))

    def clever_insert_values(self):
        self.column_names_eng.remove("Properties")

        for row_name in lib.base_stats_rows.items():
            row = [row_name[0]]
            for name in self.column_names_eng:
                column = self.view.get_values(name)
                print(column)
                row.append(row_name[1](column))
            self.tree.insert("", "end", values=row)


if __name__ == "__main__":
    pass

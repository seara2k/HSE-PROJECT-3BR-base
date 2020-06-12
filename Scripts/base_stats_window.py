import tkinter as tk
from tkinter import ttk
import lib

# pylint: disable=C0103


class base_stats_window(tk.Toplevel):

    def __init__(self, parent, column_names_ru):
        super().__init__()
        self.column_names_ru = column_names_ru
        self.parent = parent
        self.title("Базовая статистика")
        self.geometry("1000x350")
        self.resizable(False, False)
        self.init_GUI()

    def init_GUI(self):

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
                column = self.parent.get_values(name)
                print(column)
                row.append(row_name[1](column))
            self.tree.insert("", "end", values=row)
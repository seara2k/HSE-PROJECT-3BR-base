import tkinter as tk
from tkinter import ttk


class main_funcs:

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
        self.add_img_up = tk.PhotoImage(file=".\\Mats\\arrow_up.gif")
        self.add_img_down = tk.PhotoImage(file=".\\Mats\\arrow_down.gif")
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

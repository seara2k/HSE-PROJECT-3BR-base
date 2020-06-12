import tkinter as tk
import os
from tkinter import filedialog
from tkinter import ttk, messagebox
import pandas as pd
import pickle


class main_funcs:

    def refresh_from_database(self):
        """
        Создает их фрейма построчно массивы + вывод
        ---------
        Библиотеки: pandas
        """
        for tree in self.tree_names:
            getattr(self, tree).delete(*getattr(self, tree).get_children())

            for column in getattr(self, tree + "_columns"):
                getattr(self, tree).heading(column, image="")

        for i in range(len(self.database.dataframe.index)):
            row = sum(self.database.dataframe.iloc[[i]].values.tolist(), [])
            self.add_row_to_table(row)

    def add_row_to_table(self, row):
        """
        Запись добавленных данных в таблицу
        Параметры: row - список введённых данных
        Возвращает: -
        Автор: Литвинов В.С.
        """

        self.tree_all.insert("", "end", values=(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        self.tree_1.insert("", "end", values=(
            row[0], row[1], row[2]))

        self.tree_2.insert("", "end", values=(
            row[0], row[4], row[5]))

        self.tree_3.insert("", "end", values=(
            row[3], row[5], row[6]))

    def add(self, add_array):
        self.database.add(add_array)
        self.refresh_from_database()

    def delete(self):
        """
        Удаление строки из датафрейма
        Параметры: -
        Возвращает: -
        Авторы: Литвинов В.С и Никоненко А.Р.
        """
        tree = self.chosen_tree()
        for row in getattr(self, tree).selection():
            row_id = getattr(self, tree).item(row)["values"][0]
            self.database.delete(row_id)
        self.refresh_from_database()

    def chosen_tree(self):
        """

        Параметры:
        Возвращает:
        Автор:
        """
        if self.tab_parent.tab(self.tab_parent.select(), "text") == "Полная таблица":
            tree = "tree_all"
        elif self.tab_parent.tab(self.tab_parent.select(), "text") == "Сотрудник":
            tree = "tree_1"
        elif self.tab_parent.tab(self.tab_parent.select(), "text") == "Часы":
            tree = "tree_2"
        elif self.tab_parent.tab(self.tab_parent.select(), "text") == "Работы":
            tree = "tree_3"
        return tree

    def change_row(self, ID, array):
        """

        Параметры:
        Возвращает:
        Автор:
        """
        self.database.change(ID, array)
        self.refresh_from_database()


# def delete_from_table(self):
    #     """
    #     Удаление элементов таблицы
    #     """
    #     if self.tab_parent.tab(self.tab_parent.select(), "text") == "Полная таблица":
    #         tree = "tree_1"
    #     elif self.tab_parent.tab(self.tab_parent.select(), "text") == "Сотрудник":
    #         tree = "tree_1"
    #     elif self.tab_parent.tab(self.tab_parent.select(), "text") == "Часы":
    #         tree = "tree_2"
    #     elif self.tab_parent.tab(self.tab_parent.select(), "text") == "Работы":
    #         tree = "tree_3"
    #     [getattr(self, tree).delete(row)
    #      for row in getattr(self, tree).selection()]

    def sort(self, tv, col, reverse, tv_name):
        """

        Параметры: tv -
                   col -
                   reverse -
                   tv_name -
        Возвращает:
        Автор:
        """
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)

        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)
        for column in getattr(self, tv_name + "_columns"):
            tv.heading(column, image="")
        if reverse:
            tv.heading(col, image=self.add_img_up)
        else:
            tv.heading(col, image=self.add_img_down)
        # reverse sort next time
        tv.heading(col, command=lambda:
                   self.sort(tv, col, not reverse, tv_name))

    def choose_analysis_function(self):
        """

        Параметры:
        Возвращает:
        Автор:
        """
        chosen_analysis = self.ag_cb_analys.get()
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

        Параметры: column name -
        Возвращает:
        Автор:
        """

        self.column_name_values = []
        for line in self.tree_all.get_children():
            self.column_name_values.append(
                self.tree_all.set(line, column_name))
            # print(self.tree_1.item(line)['values'])
        #     for value in self.tree_1.item(line)['values']:

        return self.column_name_values

    def edit_button_check(self, event):
        """

        Параметры:
        Возвращает:
        Автор:
        """
        tree = self.chosen_tree()
        if ((len(getattr(self, tree).selection()) >= 2) or (len(getattr(self, tree).selection()) == 0)):
            self.eg_btn_edit.config(state="disabled")

        else:
            self.eg_btn_edit.config(state="normal")

    def deselect_rows(self, event):
        """

        Параметры:
        Возвращает:
        Автор:
        """
        for tree in self.tree_names:
            if len(getattr(self, tree).selection()) > 0:
                getattr(self, tree).selection_remove(
                    getattr(self, tree).selection())

    def launch_pickle(self):
        """

        Параметры:
        Возвращает:
        Автор:
        """
        try:
            f = open(".\\Database\\database.pickle", 'rb')
        except:
            messagebox.showerror(title='Ошибка!',
                                 message="Не обнаружено database.pickle файла в .\\Database, программа автоматически создаст его")
            self.pickle_position = os.getcwd() + "\\Database\\database.pickle"
            self.save()
        else:
            self.database = pickle.load(f)
            f.close()
            self.pickle_position = os.getcwd() + "\\Database\\database.pickle"
        finally:
            self.refresh_from_database()

    def true_load(self):
        """

        Параметры:
        Возвращает:
        Автор:
        """
        opening_path = filedialog.askopenfilename(title="Открыть pickle", initialdir=".\\Database", filetypes=[
                                                  ("Pickle file", ".pickle")], defaultextension=".pickle")
        if opening_path == "":
            return
        self.pickle_position = opening_path
        self.title(self.pickle_position)
        with open(self.pickle_position, 'rb') as f:
            self.database = pickle.load(f)
            f.close()
            self.refresh_from_database()

    def save(self):
        """

        Параметры:
        Возвращает:
        Автор:
        """
        with open(self.pickle_position, 'wb') as f:
            pickle.dump(self.database, f)
            f.close()

    def new(self):
        """

        Параметры:
        Возвращает:
        Автор:
        """
        action = messagebox.askyesnocancel(title="Сохранить изменения?",
                                           message=self.pickle_position + " фаил был модифицирован, сохранить изменения?", icon="warning")

        if action == True:
            self.save()
            self.database.re_init()
            self.refresh_from_database()
            self.pickle_position = os.getcwd() + "\\Database\\database.pickle"
            self.title(self.pickle_position)
            self.save()
        elif action == False:
            self.database.re_init()
            self.refresh_from_database()
            self.pickle_position = os.getcwd() + "\\Database\\database.pickle"
            self.title(self.pickle_position)
            self.save()

    def open(self):
        """

        Параметры:
        Возвращает:
        Автор:
        """
        action = messagebox.askyesnocancel(title="Сохранить изменения?",
                                           message=self.pickle_position + " фаил был модифицирован, сохранить изменения?", icon="warning")
        if action == True:
            self.save()
            self.true_load()
        elif action == False:
            self.true_load()

    def save_to_pickle(self):
        """

        Параметры:
        Возвращает:
        Автор:
        """
        saving_path = filedialog.asksaveasfilename(
            title="Сохранить как", initialdir=".\\Database", filetypes=[("Pickle file", ".pickle")], defaultextension=".pickle")
        if saving_path == "":
            return
        else:
            self.pickle_position = saving_path
            self.title(self.pickle_position)
            self.save()

    def export_to_excel(self):
        """

        Параметры:
        Возвращает:
        Автор:
        """
        # saving_path=''
        saving_path = filedialog.asksaveasfilename(
            title="Сохранить в xlsx", initialdir=".\\Database", filetypes=[("Excel file", ".xlsx")], defaultextension=".xlsx")
        if saving_path == "":
            return
        else:
            self.database.dataframe.to_excel(saving_path, index=False)

    def import_from_excel(self):
        action = messagebox.askyesnocancel(title="Сохранить изменения?",
                                           message=self.pickle_position + " фаил был модифицирован, сохранить изменения?", icon="warning")

        if action == True:
            self.save()
            self.get_excel()
        elif action == False:
            self.get_excel()

    def get_excel(self):
        opening_path = filedialog.askopenfilename(title="Открыть xlsx", initialdir=".\\Database", filetypes=[
                                                  ("Excel file", ".xlsx")], defaultextension=".xlsx")

        if opening_path == "":
            return
        else:
            self.database.dataframe = pd.read_excel(opening_path)
            self.refresh_from_database()
            self.pickle_position = os.getcwd() + "\\Database\\database.pickle"
            self.title(self.pickle_position)
            self.save()

    def get_help(self):
        os.system("start " + (os.getcwd() + "\\Notes\\govno.docx"))

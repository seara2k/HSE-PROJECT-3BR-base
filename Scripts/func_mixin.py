import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import pandas as pd
import pickle


class main_funcs:

    def refresh_from_database(self):
        """
        Создает их фрейма построчно массивы + вывод
        ---------
        Библиотеки: pandas
        """
        self.tree_all.delete(*self.tree_all.get_children())
        self.tree_1.delete(*self.tree_1.get_children())
        self.tree_2.delete(*self.tree_2.get_children())
        self.tree_3.delete(*self.tree_3.get_children())
        for i in range(len(self.database.dataframe.index)):
            row = sum(self.database.dataframe.iloc[[i]].values.tolist(), [])
            self.add_row_to_table(row)

    def add_row_to_table(self, row):
        """
        Запись данных в таблицы
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
        Сортировка при нажатии на колонку
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
        Получает данные из колонки
        """

        self.column_name_values = []
        for line in self.tree_all.get_children():
            self.column_name_values.append(
                self.tree_all.set(line, column_name))
            # print(self.tree_1.item(line)['values'])
        #     for value in self.tree_1.item(line)['values']:

        return self.column_name_values

    def delete(self):
        """
        Удаление строки из датафрейма
        ---------
        Библиотеки: pandas(pd)
        """
        if self.tab_parent.tab(self.tab_parent.select(), "text") == "Полная таблица":
            tree = "tree_all"
        elif self.tab_parent.tab(self.tab_parent.select(), "text") == "Сотрудник":
            tree = "tree_1"
        elif self.tab_parent.tab(self.tab_parent.select(), "text") == "Часы":
            tree = "tree_2"
        elif self.tab_parent.tab(self.tab_parent.select(), "text") == "Работы":
            tree = "tree_3"
        for row in getattr(self, tree).selection():
            row_id = getattr(self, tree).item(row)["values"][0]
            self.database.delete(str(row_id))
        self.refresh_from_database()

    def save_to_pickle(self):
        """
        сохраняет датафрейм в .pickle файл
        """

        with open(".\\Database\\database.pickle", 'wb') as f:
            pickle.dump(self.database, f)
            f.close()

    def open_pickle(self, path=".\\Database\\database.pickle"):
        """
        создает датафрейм из .pickle файла

        """
        try:
            f = open(path, 'rb')
        except:
            mb.showerror(title='Ошибка!',
                         message="Файл по такому пути отсутствует")
        else:
            self.database = pickle.load(f)
        finally:
            f.close()
        self.refresh_from_database()
    # def export_to_excel(self, pickle_base, path, name):

    def export_to_excel(self):
        """
        Экспорт базы в pickle в excel файл
        ----------
        pickle : .pickle файл
        path : путь сохранения файла
        name : название файла
        ----------
        Возвращает: -
        ----------
        Автор: loh
        """
        # saving_path=''
        saving_path = filedialog.asksaveasfilename(
            title="Сохранить в xlsx", initialdir=".\\Database", filetypes=[("Excel file", ".xlsx")], defaultextension=".xlsx")
        if saving_path == "":
            return
        else:
            self.database.dataframe.to_excel(saving_path)

    def import_from_excel(self):

        opening_path = filedialog.askopenfilename(title="Открыть xlsx", initialdir=".\\Database", filetypes=[
                                                  ("Excel file", ".xlsx")], defaultextension=".xlsx")

        if opening_path == "":
            return
        else:
            self.database.dataframe = pd.read_excel(opening_path)
            self.refresh_from_database()     
    # def import_file(self, path):
    #     """
    #     Импорт базы из excel файла в .pickle
    #     ----------
    #     path : пусть загружаемого файла
    #     ----------
    #     Возвращает : .pickle файл
    #     ----------
    #     Автор: убейся головой об стену
    #     """
    #     try:
    #         excel_base = pd.read_excel(path)
    #         with open(".\\Database\\database.pickle", 'wb') as f:
    #             pickle.dump(excel_base, f)
    #     except:
    #         mb.showerror(title='Ошибка!',
    #                      message="Файл по такому пути отсутствует")
    #     # else:
    #     #     with open(".\\Database\\database.pickle", "rb") as f:
    #     #         pickle_base = pickle.load(f)
    #     # return pickle_base

    # def export_file(self, pickle_base, path, name):
    #     """
    #     Экспорт базы в pickle в excel файл
    #     ----------
    #     pickle : .pickle файл
    #     path : путь сохранения файла
    #     name : название файла
    #     ----------
    #     Возвращает: -
    #     ----------
    #     Автор: loh
    #     """
    #     full_path = path + name + '.xlsx'
    #     if os.path.exists(full_path):
    #         ans = mb.askyesno(title='Примечание',
    #                           message='''Файл с таким путём уже существует и будет
    #                     перезаписан. Продолжить?''')
    #         if ans:
    #             pickle_base.to_excel(full_path)
    #     else:
    # #         pickle_base.to_excel(full_path)

    # def refresh_file(pickle_base):
    #     """
    #     Обновление .pickle файла
    #     --------
    #     pickle_base : изменённый .pickle файл
    #     -------
    #     Возвращает : нихуя
    #     -------
    #     Автор : прекращай писать докстринги
    #     """
    #     with open('database.pickle', 'wb') as f:
    #         pickle.dump(pickle_base, f)
    #         f.close()
    #     with open('database.pickle', 'rb') as f:
    #         pickle.load(f)
    #         f.close()

    # def clear_images_tree_all(self):
    #     temp=str(getattr(tree_name,""))
    #     for column in temp:
    #         getattr(self, tree_name).heading(column, image="")

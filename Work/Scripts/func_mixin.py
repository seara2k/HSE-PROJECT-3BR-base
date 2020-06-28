import tkinter as tk
import os
from tkinter import filedialog
from tkinter import ttk, messagebox
import pandas as pd
import pickle
from . import class_database as db


class main_funcs:

    def refresh_from_database(self, database):
        """
        Регенерирует таблицу из датафрейма
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """

        for tree in self.tree_names:
            getattr(self, tree).delete(*getattr(self, tree).get_children())

            for column in getattr(self, tree + "_columns"):
                getattr(self, tree).heading(column, image="")
        database.merge()
        for i in range(len(database.dataframe_all.index)):
            row = sum(database.dataframe_all.iloc[[i]].values.tolist(), [])
            self.tree_all.insert("", "end", values=row)

        for i in range(len(database.dataframe_1.index)):
            row = sum(database.dataframe_1.iloc[[i]].values.tolist(), [])
            self.tree_1.insert("", "end", values=row)

        for i in range(len(database.dataframe_2.index)):
            row = sum(database.dataframe_2.iloc[[i]].values.tolist(), [])
            self.tree_2.insert("", "end", values=row)

        for i in range(len(database.dataframe_3.index)):
            row = sum(database.dataframe_3.iloc[[i]].values.tolist(), [])
            self.tree_3.insert("", "end", values=row)

        self.eg_btn_edit.config(state="disabled")
        self.filtered = 0

    def add(self, add_array):
        """
        Добавление данных в датафрейм
        ----------
        Параметры: - add_array - список введённых данных
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """
        tree = self.chosen_tree()
        if tree == "tree_1":
            self.database.add_specialist(add_array)
        if tree == "tree_2":
            self.database.add_hours(add_array)
        if tree == "tree_3":
            self.database.add_jobs(add_array)

        self.refresh_from_database(self.database)
        self.if_changed = 1

    def delete(self):
        """
        Удаление строки из датафрейма
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Авторы: Литвинов В.С и Никоненко А.Р.
        """
        tree = self.chosen_tree()
        if tree == "tree_1":
            for row in getattr(self, tree).selection():
                row_id = getattr(self, tree).item(row)["values"][0]
                self.database.delete_specialist(row_id)
        elif tree == "tree_2":
            for row in getattr(self, tree).selection():
                row_id = getattr(self, tree).item(row)["values"][0]
                self.database.delete_hours(row_id)
        elif tree == "tree_3":
            for row in getattr(self, tree).selection():
                row_city = getattr(self, tree).item(row)["values"][0]
                row_speciality = getattr(self, tree).item(row)["values"][1]
                print(row_city, row_speciality)
                self.database.delete_jobs(row_city, row_speciality)

        self.refresh_from_database(self.database)
        self.if_changed = 1

    def change_row(self, change_array):
        """
        Изменяет строку в датафрейме
        ----------
        Параметры: - identity - номер сотрудника, array - массив изменений
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """

        tree = self.chosen_tree()
        if tree == "tree_1":
            for row in getattr(self, tree).selection():
                row_id = getattr(self, tree).item(row)["values"][0]
                self.database.change_specialist(row_id, change_array)
        elif tree == "tree_2":
            for row in getattr(self, tree).selection():
                row_id = getattr(self, tree).item(row)["values"][0]
                self.database.change_hours(row_id, change_array)
        elif tree == "tree_3":
            for row in getattr(self, tree).selection():
                row_city = getattr(self, tree).item(row)["values"][0]
                row_speciality = getattr(self, tree).item(row)["values"][1]
                self.database.change_jobs(
                    row_city, row_speciality, change_array)

        self.refresh_from_database(self.database)
        self.if_changed = 1

    def filter(self, identity, sign_identity, name, city, number, spec, hour, sign_hour, pay, sign_pay):
        filtered_database = db.db()
        filtered_database.dataframe_all = self.database.dataframe_all
        filtered_database.dataframe_1 = self.database.dataframe_1
        filtered_database.dataframe_2 = self.database.dataframe_2
        filtered_database.dataframe_3 = self.database.dataframe_3
        if identity != '':
            if sign_identity == '>':
                filtered_database.dataframe_all = filtered_database.dataframe_all.loc[
                    filtered_database.dataframe_all['Номер сотрудника'] > int(identity)]
                filtered_database.dataframe_1 = filtered_database.dataframe_1.loc[
                    filtered_database.dataframe_1['Номер сотрудника'] > int(identity)]
                filtered_database.dataframe_2 = filtered_database.dataframe_2.loc[
                    filtered_database.dataframe_2['Номер сотрудника'] > int(identity)]
            if sign_identity == '>=':
                filtered_database.dataframe_all = filtered_database.dataframe_all.loc[
                    filtered_database.dataframe_all['Номер сотрудника'] >= int(identity)]
                filtered_database.dataframe_1 = filtered_database.dataframe_1.loc[
                    filtered_database.dataframe_1['Номер сотрудника'] >= int(identity)]
                filtered_database.dataframe_2 = filtered_database.dataframe_2.loc[
                    filtered_database.dataframe_2['Номер сотрудника'] >= int(identity)]
            if sign_identity == '=':
                filtered_database.dataframe_all = filtered_database.dataframe_all.loc[
                    filtered_database.dataframe_all['Номер сотрудника'] == int(identity)]
                filtered_database.dataframe_1 = filtered_database.dataframe_1.loc[
                    filtered_database.dataframe_1['Номер сотрудника'] == int(identity)]
                filtered_database.dataframe_2 = filtered_database.dataframe_2.loc[
                    filtered_database.dataframe_2['Номер сотрудника'] == int(identity)]
            if sign_identity == '<=':
                filtered_database.dataframe_all = filtered_database.dataframe_all.loc[
                    filtered_database.dataframe_all['Номер сотрудника'] <= int(identity)]
                filtered_database.dataframe_1 = filtered_database.dataframe_1.loc[
                    filtered_database.dataframe_1['Номер сотрудника'] <= int(identity)]
                filtered_database.dataframe_2 = filtered_database.dataframe_2.loc[
                    filtered_database.dataframe_2['Номер сотрудника'] <= int(identity)]
            if sign_identity == '<':
                filtered_database.dataframe_all = filtered_database.dataframe_all.loc[
                    filtered_database.dataframe_all['Номер сотрудника'] < int(identity)]
                filtered_database.dataframe_1 = filtered_database.dataframe_1.loc[
                    filtered_database.dataframe_1['Номер сотрудника'] < int(identity)]
                filtered_database.dataframe_2 = filtered_database.dataframe_2.loc[
                    filtered_database.dataframe_2['Номер сотрудника'] < int(identity)]
        if name != '':
            filtered_database.dataframe_all = filtered_database.dataframe_all.loc[
                filtered_database.dataframe_all['ФИО'] == name]
            filtered_database.dataframe_1 = filtered_database.dataframe_1.loc[
                filtered_database.dataframe_1['ФИО'] == name]
        if city != '':
            filtered_database.dataframe_all = filtered_database.dataframe_all.loc[
                filtered_database.dataframe_all['Город'] == city]
            filtered_database.dataframe_1 = filtered_database.dataframe_1.loc[
                filtered_database.dataframe_1['Город'] == city]
            filtered_database.dataframe_3 = filtered_database.dataframe_3.loc[
                filtered_database.dataframe_3['Город'] == city]
        if number != '':
            filtered_database.dataframe_all = filtered_database.dataframe_all.loc[
                filtered_database.dataframe_all['Номер телефона'] == number]
            filtered_database.dataframe_1 = filtered_database.dataframe_1.loc[
                filtered_database.dataframe_1['Номер телефона'] == number]
        if spec != '':
            filtered_database.dataframe_all = filtered_database.dataframe_all.loc[
                filtered_database.dataframe_all['Специальность'] == spec]
            filtered_database.dataframe_2 = filtered_database.dataframe_2.loc[
                filtered_database.dataframe_2['Специальность'] == spec]
            filtered_database.dataframe_3 = filtered_database.dataframe_3.loc[
                filtered_database.dataframe_3['Специальность'] == spec]
        if hour != '':
            if sign_hour == '>':
                filtered_database.dataframe_all = filtered_database.dataframe_all.loc[
                    filtered_database.dataframe_all['Часы'] > int(hour)]
                filtered_database.dataframe_2 = filtered_database.dataframe_2.loc[
                    filtered_database.dataframe_2['Часы'] > int(hour)]
            if sign_hour == '>=':
                filtered_database.dataframe_all = filtered_database.dataframe_all.loc[
                    filtered_database.dataframe_all['Часы'] >= int(hour)]
                filtered_database.dataframe_2 = filtered_database.dataframe_2.loc[
                    filtered_database.dataframe_2['Часы'] >= int(hour)]
            if sign_hour == '=':
                filtered_database.dataframe_all = filtered_database.dataframe_all.loc[
                    filtered_database.dataframe_all['Часы'] == int(hour)]
                filtered_database.dataframe_2 = filtered_database.dataframe_2.loc[
                    filtered_database.dataframe_2['Часы'] == int(hour)]
            if sign_hour == '<=':
                filtered_database.dataframe_all = filtered_database.dataframe_all.loc[
                    filtered_database.dataframe_all['Часы'] <= int(hour)]
                filtered_database.dataframe_2 = filtered_database.dataframe_2.loc[
                    filtered_database.dataframe_2['Часы'] <= int(hour)]
            if sign_hour == '<':
                filtered_database.dataframe_all = filtered_database.dataframe_all.loc[
                    filtered_database.dataframe_all['Часы'] < int(hour)]
                filtered_database.dataframe_2 = filtered_database.dataframe_2.loc[
                    filtered_database.dataframe_2['Часы'] < int(hour)]
        if pay != '':
            if sign_pay == '>':
                filtered_database.dataframe_all = filtered_database.dataframe_all.loc[
                    filtered_database.dataframe_all['Зарплата в час'] > int(pay)]
                filtered_database.dataframe_3 = filtered_database.dataframe_3.loc[
                    filtered_database.dataframe_3['Зарплата в час'] > int(pay)]
            if sign_pay == '>=':
                filtered_database.dataframe_all = filtered_database.dataframe_all.loc[
                    filtered_database.dataframe_all['Зарплата в час'] >= int(pay)]
                filtered_database.dataframe_3 = filtered_database.dataframe_3.loc[
                    filtered_database.dataframe_3['Зарплата в час'] >= int(pay)]
            if sign_pay == '=':
                filtered_database.dataframe_all = filtered_database.dataframe_all.loc[
                    filtered_database.dataframe_all['Зарплата в час'] == int(pay)]
                filtered_database.dataframe_3 = filtered_database.dataframe_3.loc[
                    filtered_database.dataframe_3['Зарплата в час'] == int(pay)]
            if sign_pay == '<=':
                filtered_database.dataframe_all = filtered_database.dataframe_all.loc[
                    filtered_database.dataframe_all['Зарплата в час'] <= int(pay)]
                filtered_database.dataframe_3 = filtered_database.dataframe_3.loc[
                    filtered_database.dataframe_3['Зарплата в час'] <= int(pay)]
            if sign_pay == '<':
                filtered_database.dataframe_all = filtered_database.dataframe_all.loc[
                    filtered_database.dataframe_all['Зарплата в час'] < int(pay)]
                filtered_database.dataframe_3 = filtered_database.dataframe_3.loc[
                    filtered_database.dataframe_3['Зарплата в час'] < int(pay)]
        return filtered_database

    def chosen_tree(self):
        """
        Возвращает название дерева, которое находится на выбранной в данный момент вкладке
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
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

    def sort(self, tv, col, reverse, tv_name):
        """
        Смена направления вывода элементов в таблице интерфейса
        ----------
        Параметры:
                tv - таблица
                col - колонки таблицы
                reverse - состояние сортировки
                tv_name - название колонки таблицы
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)
        try:
            l.sort(key=lambda t: int(t[0]), reverse=reverse)
        except ValueError:
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
        Вызывает окно анализа в зависимости от выбранного способа анализа
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
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
        Получает массив значений в столбце
        ----------
        Параметры:
                column_name - названия столбца
        ----------
        Возвращает: - массив значений столбца
        ----------
        Автор: Литвинов В.С.
        """

        self.column_name_values = []
        for line in self.tree_all.get_children():
            self.column_name_values.append(
                self.tree_all.set(line, column_name))
        return self.column_name_values

    def edit_button_check(self, event):
        """
        Проверка на доступность изменения строки таблицы
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """
        tree = self.chosen_tree()
        if (len(getattr(self, tree).selection()) >= 2) or (len(getattr(self, tree).selection()) == 0):
            self.eg_btn_edit.config(state="disabled")

        else:
            self.eg_btn_edit.config(state="normal")

    def deselect_rows(self, event):
        """
        Отмена выбора строк таблицу
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """
        if self.chosen_tree() == "tree_all":
            self.eg_btn_add.config(state="disabled")
            self.eg_btn_edit.config(state="disabled")
            self.eg_btn_delete.config(state="disabled")
        else:
            self.eg_btn_add.config(state="normal")
            self.eg_btn_delete.config(state="normal")

        for tree in self.tree_names:
            if len(getattr(self, tree).selection()) > 0:
                getattr(self, tree).selection_remove(
                    getattr(self, tree).selection())

    def launch_pickle(self):
        """
        Загрузка .pickle файла при старте программы
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Никоненко А.Р.
        """
        try:
            f = open(self.pickle_position, 'rb')
        except:
            # messagebox.showerror(title='Ошибка!',
            # message="Не обнаружено последнего открытого .pickle файла " +
            # self.pickle_position)
            self.new()
        else:
            self.database = pickle.load(f)
            f.close()
        finally:
            self.refresh_from_database(self.database)

    def true_load(self):
        """
        Окно открытия .pickle файла
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """
        opening_path = filedialog.askopenfilename(title="Открыть pickle", initialdir=".\\Data", filetypes=[
                                                  ("Pickle file", ".pickle")], defaultextension=".pickle")
        if opening_path == "":
            return
        self.pickle_position = opening_path
        self.save_to_settings()
        self.title(self.pickle_position)
        with open(self.pickle_position, 'rb') as f:
            self.database = pickle.load(f)
            f.close()
            self.refresh_from_database(self.database)

    def save(self):
        """
        Сохранение активной базы данных
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """
        if self.pickle_position == "":
            result = self.save_to_pickle()
            if result == True:
                self.if_changed = 0
            return result

        else:
            with open(self.pickle_position, 'wb') as f:
                pickle.dump(self.database, f)
                f.close()
            self.if_changed = 0
            return True

    def new(self):
        """
        Создание новой базы данных
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """
        action = self.check_if_changed()

        if action == True:
            if self.save() == True:
                self.database.re_init()
                self.refresh_from_database(self.database)
                self.pickle_position = ""
                self.title("untitled")
                self.if_changed = 0
        elif action == False:
            self.database.re_init()
            self.refresh_from_database(self.database)
            self.pickle_position = ""
            self.title("untitled")
            self.if_changed = 0

    def open(self):
        """
        Открытие .pickle файла
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """
        action = self.check_if_changed()
        if action == True:
            if self.save() == True:
                self.true_load()
                self.if_changed = 0

        elif action == False:
            self.true_load()
            self.if_changed = 0

    def save_to_pickle(self):
        """
        Сохранение базы данных в .pickle файл
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Никоненко А.Р.
        """
        saving_path = filedialog.asksaveasfilename(
            title="Сохранить как", initialdir=".\\Data", filetypes=[("Pickle file", ".pickle")], defaultextension=".pickle")
        if saving_path == "":
            return False
        else:
            self.pickle_position = saving_path
            self.save_to_settings()
            self.title(self.pickle_position)
            self.save()
            return True

    def export_to_excel(self, index):
        """
        Экспорт базы данных в .xlsx файл
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Никоненко А.Р.
        """
        if self.filtered == 1:
            if self.chosen_tree() == "tree_all":
                self.give_excel(self.filtered_database.dataframe_all, False)
            elif self.chosen_tree() == "tree_1":
                self.give_excel(self.filtered_database.dataframe_1, False)

            elif self.chosen_tree() == "tree_2":
                self.give_excel(self.filtered_database.dataframe_2, False)

            elif self.chosen_tree() == "tree_3":
                self.give_excel(self.filtered_database.dataframe_3, False)
        elif self.filtered == 0:
            if self.chosen_tree() == "tree_all":
                self.give_excel(self.database.dataframe_all, False)

            elif self.chosen_tree() == "tree_1":
                self.give_excel(self.database.dataframe_1, False)

            elif self.chosen_tree() == "tree_2":
                self.give_excel(self.database.dataframe_2, False)

            elif self.chosen_tree() == "tree_3":
                self.give_excel(self.database.dataframe_3, False)

    def give_excel(self, dataframe, index):
        saving_path = filedialog.asksaveasfilename(
            title="Сохранить в xlsx", initialdir=".\\Output", filetypes=[("Excel file", ".xlsx")], defaultextension=".xlsx")
        if saving_path == "":
            return
        else:
            dataframe.to_excel(saving_path, index=index)

    def import_from_excel(self):
        """
        Импорт из .xlsx в базу данных
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Никоненко А.Р.
        """
        action = self.check_if_changed()

        if action == True:
            if self.save() == True:
                self.get_excel()
                self.if_changed = 1
        elif action == False:
            self.get_excel()
            self.if_changed = 1

    def get_excel(self):
        """
        Окно импорта из .xlsx файла
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """
        opening_path = filedialog.askopenfilename(title="Открыть xlsx", initialdir=".\\Output", filetypes=[
                                                  ("Excel file", ".xlsx")], defaultextension=".xlsx")

        if opening_path == "":
            return
        else:
            self.database.launch_from_one(opening_path)
            self.refresh_from_database(self.database)
            self.pickle_position = ""
            self.title("untitled")

    def get_help(self):
        """
        Вывод окна "Помощь"
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Никоненко А.Р.
        """
        os.system("start " + (os.getcwd() + "\\Notes\\help.pdf"))

    def check_if_changed(self):
        """
        Окно предупреждения о сохранении изменений
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """
        if self.if_changed == 1:
            action = messagebox.askyesnocancel(title="Сохранить изменения?",
                                               message=self.pickle_position + " фаил был модифицирован, сохранить изменения?", icon="warning")
            return action
        else:
            return False

    def save_to_settings(self):
        """
        Изменение файла settings.py
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """
        self.cfg["File"]["last_opened_pickle"] = self.pickle_position
        with open("settings.ini", "w") as config_file:
            self.cfg.write(config_file)

    def on_closing(self):
        """
        Спрашивает сохранить или нет про закрытии программы
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """
        action = self.check_if_changed()
        if action == True:
            if self.save() == True:
                self.destroy()
        elif action == False:
            self.destroy()

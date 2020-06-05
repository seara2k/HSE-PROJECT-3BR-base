# -*- coding: utf-8 -*-

import pandas as pd
# import matplotlib as mpl
import matplotlib.pyplot as plt

# C:\Users\Sonan\Desktop\BD.xlsx


def open_file(path):
    w = pd.read_excel(path)
    return w


def append(w):
    w1 = pd.DataFrame([], index=[0], columns=['Н_СОТР', 'ФИО', 'ГОР', 'Н_ТЕЛ',
                                              'СПЕЦ', 'ЗП_ЧАС', 'ЧАС'])
    w1.loc[0, 'Н_СОТР'] = input()
    w1.loc[0, 'ФИО'] = input()
    w1.loc[0, 'ГОР'] = input()
    w1.loc[0, 'Н_ТЕЛ'] = input()
    w1.loc[0, 'СПЕЦ'] = input()
    w1.loc[0, 'ЗП_ЧАС'] = input()
    w1.loc[0, 'ЧАС'] = input()
    return w.append(w1, ignore_index=True)


def export(w):
    w.to_excel("output.xlsx")


# Базовая Статистика
def stats():
    pass


# Сводная Таблица
def summary():
    pass


# Столбчатая Диаграмма
# def bar(w,var1, var2):
def bar_chart(x_name, y_name, var1, var2):
    plt.title("Столбчатая Диаграмма")
    plt.bar(var1, var2)
    # plt.bar(w[var1][0:],w[var2][0:])
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.show()


# Гистограмма
def histogram(x_name, y_name, var1):
    plt.title("Гистограмма")
    plt.hist(var1)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.show()

# Диаграмма Бокса-Вискера
def box_whiskers(x_name, y_name, var1):
    plt.title("Диаграмма Бокса-Вискера")
    plt.boxplot(var1, showmeans=True)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.show()


# Диаграмма Рассеивания
def dispersion(w, var1, var2):
    plt.title("Диаграмма Рассеивания")
    plt.scatter(w[var1][0:], w[var2][0:])
    plt.xlabel(var1)
    plt.ylabel(var2)
    plt.show()


def good_looking_columns(number_of_columns):
    if number_of_columns == 2:
        return 472
    if number_of_columns == 3:
        return 315
    if number_of_columns == 4:
        return 236
    if number_of_columns == 5:
        return 189
    if number_of_columns == 6:
        return 157
    if number_of_columns == 7:
        return 135
    if number_of_columns == 8:
        return 119


def translate_to_eng(input_column):
    if input_column == "Номер сотрудника":
        return "ID"
    if input_column == "ФИО":
        return "Full_Name"
    if input_column == "Город":
        return "City"
    if input_column == "Телефон":
        return "Phone_Number"
    if input_column == "Специальность":
        return "Speciality"
    if input_column == "Часы":
        return "Time"
    if input_column == "Зарплата в час":
        return "Pays_An_Hour"
    if input_column == "Свойства":
        return "Properties"

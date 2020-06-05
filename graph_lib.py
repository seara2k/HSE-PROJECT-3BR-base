# -*- coding: utf-8 -*-

import pandas as pd
# import matplotlib as mpl
import matplotlib.pyplot as plt

# C:\Users\Sonan\Desktop\BD.xlsx

def open_file(path):
    w = pd.read_excel(path)
    return w


def append(w):
    w1 = pd.DataFrame([],index = [0], columns=['Н_СОТР', 'ФИО', 'ГОР', 'Н_ТЕЛ',
                                               'СПЕЦ', 'ЗП_ЧАС','ЧАС'])
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
def bar(var1, var2):
    plt.title("Столбчатая Диаграмма")
    plt.bar(var1,var2)
    # plt.bar(w[var1][0:],w[var2][0:])
    plt.xlabel(var1)
    plt.ylabel(var2)
    plt.show()


# Гистограмма
def histogram(w, var1):
    plt.title("Гистограмма")
    plt.hist(w[var1][0:])
    plt.xlabel(var1)
    plt.show()

# Диаграмма Бокса-Вискера
def box_whiskers(w, var1):
    plt.title("Диаграмма Бокса-Вискера")
    plt.boxplot(w[var1][0:], showmeans=True)
    plt.xlabel(var1)
    plt.show()


# Диаграмма Рассеивания
def dispersion(w, var1, var2):
    plt.title("Диаграмма Рассеивания")
    plt.scatter(w[var1][0:], w[var2][0:])
    plt.xlabel(var1)
    plt.ylabel(var2)
    plt.show()
    

def translate_to_eng(input_column):
    if input_column=="ФИО":
        return "Full_Name" 
    if input_column=="Город":
        return "City" 

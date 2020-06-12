# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def amount_of_elements(var):
    """
    Подсчет элементов в списке
    Параметры: var - список элементов
    Возвращает: количество элементов
    Автор: Никоненко А.Р.
    """
    return len(var)


def unique_elements(var):
    """
    Подсчет уникальных элементов в списке
    Параметры: var - список элементов
    Возвращает: количество уникальных элементов
    Автор: Никоненко А.Р.
    """
    return len(set(var))


def most_frequent(var):
    """
    Поиск самого частого элемента в списке
    Параметры: var - список элементов
    Возвращает: первый самый частый элемент
    Автор: Никоненко А.Р.
    """
    var_set = set(var)
    count = 0
    most_frequent_element = None
    for i in var_set:
        element = var.count(i)
        if element > count:
            count = element
            most_frequent_element = i
    return most_frequent_element


def most_frequent_count(var):
    """
    Подсчет повторений самого частого элемента в списке
    Параметры: var - список элементов
    Возвращает: количество повторений первого самого частого элемента
    Автор: Никоненко А.Р.
    """
    var_set = set(var)
    count = 0
    for i in var_set:
        element = var.count(i)
        if element > count:
            count = element
    return count


def average(var):
    """
    Подсчет среднего значения в списке элементов
    Параметры: var - список элементов
    Возвращает: среднее значение (прочерк, если подсчитать значение нельзя)
    Автор: Никоненко А.Р.
    """
    elem_sum = 0
    try:
        for i in range(len(var)):
            elem_sum += float(var[i])
        return f'{(elem_sum / len(var)):.{3}f}'
    except ValueError:
        return '-'
    except TypeError:
        return '-'


def standard_deviation(var):
    """
    Подсчет среднеквадратического отклонения
    Параметры: var - список элементов
    Возвращает: среднеквадратическое отклонение (прочерк, если подсчитать значение нельзя)
    Автор: Никоненко А.Р.
    """
    try:
        result = [int(item) for item in var]
        return f'{np.std(result):.{3}f}'
    except ValueError:
        return '-'


def maximum(var):
    """
    Поиск максимального элемента в списке
    Параметры: var - список элементов
    Возвращает: максимальный элемент (прочерк, если поиск невозможен)
    Автор: Никоненко А.Р.
    """
    try:
        maxi = float(var[0])
        for i in var:
            if float(i) > maxi:
                maxi = float(i)
        return maxi
    except ValueError:
        return '-'


def minimum(var):
    """
    Поиск минимального элемента в списке
    Параметры: var - список элементов
    Возвращает: минимальный элемент (прочерк, если поиск невозможен)
    Автор: Никоненко А.Р.
    """
    try:
        mini = float(var[0])
        for i in var:
            if float(i) < mini:
                mini = float(i)
        return mini
    except ValueError:
        return '-'

base_stats_rows = {"Количество элементов": amount_of_elements, "Уникальные элементы": unique_elements,
                   "Самый частый элемент": most_frequent, "Количество повторений": most_frequent_count,
                   "Среднее значение": average, "Среднеквадратическое отклонение": standard_deviation,
                   "Максимальный элемент": maximum, "Минимальный элемент": minimum}


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
def bar_chart(kach_st_1, kach_st_2):  # количественный (численный) столбец 1 и 2
    position = np.arange(len(kach_st_1))

    fig, ax = plt.subplots()

    ax.bar(position, kach_st_2,  color=np.random.rand(7, 3))

    # Устанавливаем позиции тиков:
    ax.set_xticks(position)

    # Устанавливаем подписи тиков
    labels = ax.set_xticklabels(kach_st_1)

    fig.set_figwidth(10)
    fig.set_figheight(6)

    plt.show()


# Гистограмма
def histogramm(kach_st, kol_st):
    position = np.arange(len(kach_st))
    for i in range(len(kach_st)):
        kach_st[i] = kach_st[i].replace(' ', '\n')
    fig, ax = plt.subplots()

    ax.bar(position, kol_st, color=np.random.rand(7, 3))

    # Устанавливаем позиции тиков:
    ax.set_xticks(position)

    # Устанавливаем подписи тиков
    labels = ax.set_xticklabels(kach_st,
                                verticalalignment='top')  # Вертикальное выравнивание

    fig.set_figwidth(10)
    fig.set_figheight(6)

    plt.show()

# Диаграмма Бокса-Вискера


def boxplot(kach_st, kol_st):  # качественный и количественный столбцы
    fig = plt.figure()
    fig.suptitle('Диаграмма Бокса-Висскера')
    ax = fig.add_subplot(111)
    ax.boxplot(kol_st  # patch_artist must be True to control box fill
               # Properties of whisker caps
               , patch_artist=True, medianprops={'color': "#297083"}, boxprops={'color': "#539caf", 'facecolor': "#539caf"}, whiskerprops={'color': "#539caf"}, capprops={'color': "#539caf"})
    ax.set_xticklabels(kach_st)
    plt.show()

# Диаграмма Рассеивания


def scatter(kach_st, kol_st_1, kol_st_2):
    data = {'Name': kach_st,
            'Hours': kol_st_1,
            'Salary': kol_st_2}
    midwest = pd.DataFrame(data)

    categories = np.unique(midwest['Name'])
    colors = [plt.cm.tab10(i / float(len(categories) - 1))
              for i in range(len(categories))]
    plt.figure(figsize=(16, 10), dpi=80, facecolor='w', edgecolor='k')
    for i, Name in enumerate(categories):
        plt.scatter('Hours', 'Salary',
                    data=midwest.loc[midwest.Name == Name, :],
                    s=20, c=np.array([colors[i]]), label=str(Name))

    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.title("Диаграмма Рассеивания", fontsize=22)
    plt.legend(fontsize=12)
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
    """
    Перевод названий столбцов с русского на английский язык
    Параметры: input_column - название колонки на русском языке
    Возвращает: название колонки на английском языке
    Автор: Литвинов В.С.
    """
    if input_column == "Номер сотрудника":
        return "ID"
    if input_column == "ФИО":
        return "Full_Name"
    if input_column == "Город":
        return "City"
    if input_column == "Номер телефона":
        return "Phone_Number"
    if input_column == "Специальность":
        return "Speciality"
    if input_column == "Часы":
        return "Time"
    if input_column == "Зарплата в час":
        return "Pays_An_Hour"
    if input_column == "Свойства":
        return "Properties"

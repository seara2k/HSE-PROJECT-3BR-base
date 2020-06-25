import numpy as np


def amount_of_elements(var):
    """
    Подсчет элементов в списке
    ----------
    Параметры:
            var - список элементов
    ----------
    Возвращает: количество элементов
    ----------
    Автор: Никоненко А.Р.
    """
    return len(var)


def unique_elements(var):
    """
    Подсчет уникальных элементов в списке
    ----------
    Параметры:
            var - список элементов
    ----------
    Возвращает: количество уникальных элементов
    ----------
    Автор: Никоненко А.Р.
    """
    return len(set(var))


def most_frequent(var):
    """
    Поиск самого частого элемента в списке
    ----------
    Параметры:
            var - список элементов
    ----------
    Возвращает: первый самый частый элемент
    ----------
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
    ----------
    Параметры:
            var - список элементов
    ----------
    Возвращает: количество повторений первого самого частого элемента
    ----------
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
    ----------
    Параметры:
            var - список элементов
    ----------
    Возвращает: среднее значение (прочерк, если подсчитать значение нельзя)
    ----------
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
    except ZeroDivisionError:
        return '-'


def standard_deviation(var):
    """
    Подсчет среднеквадратического отклонения
    ----------
    Параметры:
            var - список элементов
    ----------
    Возвращает: среднеквадратическое отклонение (прочерк, если подсчитать значение нельзя)
    ----------
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
    ----------
    Параметры:
            var - список элементов
    ----------
    Возвращает: максимальный элемент (прочерк, если поиск невозможен)
    ----------
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
    except IndexError:
        return '-'


def minimum(var):
    """
    Поиск минимального элемента в списке
    ----------
    Параметры:
            var - список элементов
    ----------
    Возвращает: минимальный элемент (прочерк, если поиск невозможен)
    ----------
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
    except IndexError:
        return '-'


base_stats_rows = {"Количество элементов": amount_of_elements, "Уникальные элементы": unique_elements,
                   "Самый частый элемент": most_frequent, "Количество повторений": most_frequent_count,
                   "Среднее значение": average, "Среднеквадратическое отклонение": standard_deviation,
                   "Максимальный элемент": maximum, "Минимальный элемент": minimum}


def good_looking_columns(number_of_columns):
    """
    Выбор ширины столбца в зависимости от количества столбцов
    ----------
    Параметры:
            number_of_columns - количество столбцов
    ----------
    Возвращает: Оптимальная ширина столбца
    ----------
    Автор: Литвинов В.С.
    """
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
    if number_of_columns >= 8:
        return 119


def translate_to_eng(input_column):
    """
    Перевод названий столбцов с русского на английский язык
    ----------
    Параметры:
            input_column - название колонки на русском языке
    ----------
    Возвращает: название колонки на английском языке
    ----------
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
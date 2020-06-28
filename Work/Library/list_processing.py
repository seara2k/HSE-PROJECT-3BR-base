import pandas as pd

base_stats_rows = ["Количество элементов", "Уникальные элементы",
                   "Самый частый элемент", "Количество повторений",
                   "Среднее значение", "Среднеквадратическое отклонение", "Минимальный элемент", "25%", "50%",
                   "75%", "Максимальный элемент"]


def base_stats(df, array):
    df3 = pd.DataFrame(index=['count', 'unique', 'top', 'freq', 'mean',
                              'std', 'min', '25%', '50%', '75%', 'max'])
    df1 = df[array].astype(str).describe(include='all')
    df2 = df[array].describe(include='all')
    df2 = df2.fillna(value=df1)
    df_all = pd.concat([df3,df2], axis=1, join='outer')
    return df_all.fillna(value='-')


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
        return "id"
    if input_column == "ФИО":
        return "full_name"
    if input_column == "Город":
        return "city"
    if input_column == "Номер телефона":
        return "phone_number"
    if input_column == "Специальность":
        return "speciality"
    if input_column == "Часы":
        return "time"
    if input_column == "Зарплата в час":
        return "pays_an_hour"
    if input_column == "Свойства":
        return "properties"

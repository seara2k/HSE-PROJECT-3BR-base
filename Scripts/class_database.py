import pandas as pd


class df:

    def __init__(self):
        """
        Конструктор базы данных
        ----------
        Параметры:  -
        ----------
        Возвращает: -
        ----------
        Автор: Никоненко А.Р.
        """
        self.dataframe = pd.DataFrame(columns=['Н_СОТР', 'ФИО', 'ГОР',
                                               'Н_ТЕЛ', 'СПЕЦ',
                                               'ЧАС', 'ЗП_ЧАС'])

    def re_init(self):
        """
        Повторная сборка базы данных
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """
        self.dataframe = pd.DataFrame(columns=['Н_СОТР', 'ФИО', 'ГОР',
                                               'Н_ТЕЛ', 'СПЕЦ',
                                               'ЧАС', 'ЗП_ЧАС'])

    def add(self, add_array):
        """
        Добавление строки в базу данных
        ----------
        Параметры:
                add_array - список добавляемой строки
        ---------
        Возвращает: -
        ----------
        Автор: Никоненко А.Р.
        """
        adding_row = pd.DataFrame(columns=['Н_СОТР', 'ФИО', 'ГОР',
                                           'Н_ТЕЛ', 'СПЕЦ',
                                           'ЧАС', 'ЗП_ЧАС'])
        adding_row.loc[0, :] = add_array
        self.dataframe = self.dataframe.append(adding_row, ignore_index=True)

    def delete(self, w_id):
        """
        Удаление строки из базы данных
        ----------
        Параметры:
                w_id - номер сотрудника
        ----------
        Возвращает:
        ----------
        Автор: Никоненко А.Р.
        """
        self.dataframe = self.dataframe.drop(
            self.dataframe.loc[self.dataframe["Н_СОТР"] == w_id].index)

    def change(self, w_id, array):
        """
        Изменение строки в базе данных
        ----------
        Параметры:
                w_id - номер сотрудника
                array - список новой строки
        ----------
        Возвращает: -
        ----------
        Автор: Никоненко А.Р.
        """
        temp = self.dataframe.loc[self.dataframe["Н_СОТР"] == w_id].index
        self.dataframe.loc[temp, :] = array

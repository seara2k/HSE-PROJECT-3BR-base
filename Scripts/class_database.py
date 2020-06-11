import pandas as pd


class df:

    def __init__(self):
        self.dataframe = pd.DataFrame(columns=['Н_СОТР', 'ФИО', 'ГОР',
                                               'Н_ТЕЛ', 'СПЕЦ',
                                               'ЧАС', 'ЗП_ЧАС'])

    def re_init(self):
        self.dataframe = pd.DataFrame(columns=['Н_СОТР', 'ФИО', 'ГОР',
                                               'Н_ТЕЛ', 'СПЕЦ',
                                               'ЧАС', 'ЗП_ЧАС'])

    def add(self, add_array):
        adding_row = pd.DataFrame(columns=['Н_СОТР', 'ФИО', 'ГОР',
                                           'Н_ТЕЛ', 'СПЕЦ',
                                           'ЧАС', 'ЗП_ЧАС'])
        adding_row.loc[0, :] = add_array
        self.dataframe = self.dataframe.append(adding_row, ignore_index=True)

    def delete(self, ID):
        self.dataframe = self.dataframe.drop(
            self.dataframe.loc[self.dataframe["Н_СОТР"] == ID].index)

    def change(self, ID, array):
        temp = self.dataframe.loc[self.dataframe["Н_СОТР"] == ID].index
        self.dataframe.loc[temp, :] = array

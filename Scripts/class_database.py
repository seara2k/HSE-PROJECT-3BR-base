import pandas as pd


class df:

    def __init__(self):
        self.dataframe = pd.DataFrame(columns=['Н_СОТР', 'ФИО', 'ГОР',
                                               'Н_ТЕЛ', 'СПЕЦ',
                                               'ЗП_ЧАС', 'ЧАС'])

    def add(self, add_array):
        adding_row = pd.DataFrame(columns=['Н_СОТР', 'ФИО', 'ГОР', 'Н_ТЕЛ', 'СПЕЦ',
                                           'ЗП_ЧАС', 'ЧАС'])
        adding_row.loc[0, :] = add_array
        self.dataframe = self.dataframe.append(adding_row, ignore_index=True)

    def delete(self, ID):
        self.dataframe = self.dataframe.drop(
            self.dataframe.loc[self.dataframe["Н_СОТР"] == ID].index)

    def change(self):
        pass


# # aa = df()
# # aa.add([1, "fgdfgfdgf", "fgdfgfdgf", "fgdfgfdgf",
# #        "fgdfgfdgf", "fgdfgfdgf", "fgdfgfdgf"])
# # aa.add([2, "fgdfgfdgf", "fgdfgfdgf", "fgdfgfdgf",
# #        "fgdfgfdgf", "fgdfgfdgf", "fgdfgfdgf"])
# # print(aa.dataframe)
# # print("//////////////////")
# # ID=2
# # aa.delete(ID)
# print(aa.dataframe)

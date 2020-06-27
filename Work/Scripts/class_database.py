import pandas as pd


class db:

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
        self.dataframe_all = pd.DataFrame(columns=['Номер сотрудника', 'ФИО', 'Город', 'Номер телефона',
                                                     'Специальность', 'Часы', 'Зарплата в час'])
        self.dataframe_1 = pd.DataFrame(columns=['Номер сотрудника', 'ФИО', 'Город', 'Номер телефона'])
        self.dataframe_2 = pd.DataFrame(columns=['Номер сотрудника', 'Специальность', 'Часы'])
        self.dataframe_3 = pd.DataFrame(columns=['Город', 'Специальность', 'Зарплата в час'])

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
        self.dataframe_all = pd.DataFrame(columns=['Номер сотрудника', 'ФИО', 'Город', 'Номер телефона',
                                                     'Специальность', 'Часы', 'Зарплата в час'])
        self.dataframe_1 = pd.DataFrame(columns=['Номер сотрудника', 'ФИО', 'Город', 'Номер телефона'])
        self.dataframe_2 = pd.DataFrame(columns=['Номер сотрудника', 'Специальность', 'Часы'])
        self.dataframe_3 = pd.DataFrame(columns=['Город', 'Специальность', 'Зарплата в час'])


    def launch_from_one(self, path):
        self.dataframe_all = pd.read_excel(path)
        self.dataframe_1 = self.dataframe_all.loc[:, ['Номер сотрудника', 'ФИО', 'Город', 'Номер телефона']]
        self.dataframe_2 = self.dataframe_all.loc[:, ['Номер сотрудника', 'Специальность', 'Часы']]
        self.dataframe_3 = self.dataframe_all.loc[:, ['Город', 'Специальность', 'Зарплата в час']]


    def merge(self):

        temp = pd.merge(self.dataframe_1, self.dataframe_2, on="Номер сотрудника")
        self.dataframe_all = pd.merge(temp, self.dataframe_3, on=["Город", "Специальность"])

    def add_full(self, dictionary):
        """
        Добавление всей строки в таблицу
        ----------

        """
        d = pd.DataFrame(columns=['Номер сотрудника', 'ФИО', 'Город', 'Номер телефона',
                                  'Специальность', 'Часы', 'Зарплата в час'])
        d.loc[0, :] = dictionary
        df1 = d.loc[:, ['Номер сотрудника', 'ФИО', 'Город', 'Номер телефона']]
        df2 = d.loc[:, ['Номер сотрудника', 'Специальность', 'Часы']]
        df3 = d.loc[:, ['Город', 'Специальность', 'Зарплата в час']]
        self.dataframe_1 = self.dataframe_1.append(df1, ignore_index=True)
        if any(self.dataframe_1.duplicated()):
            self.dataframe_1 = self.dataframe_1.drop_duplicates()
        self.dataframe_2 = self.dataframe_2.append(df2, ignore_index=True)
        if any(self.dataframe_2.duplicated()):
            self.dataframe_2 = self.dataframe_2.drop_duplicates()
        self.dataframe_3 = self.dataframe_3.append(df3, ignore_index=True)
        if any(self.dataframe_3.duplicated()):
            self.dataframe_3 = self.dataframe_3.drop_duplicates()

    def add_specialist(self, dictionary):
        """
        Добавление строки в таблицу "Сотрудники"
        ----------

        """
        d = pd.DataFrame(columns=['Номер сотрудника', 'ФИО', 'Город', 'Номер телефона'])
        d.loc[0, :] = dictionary
        self.dataframe_1 = self.dataframe_1.append(d, ignore_index=True)
        if any(self.dataframe_1.duplicated()):
            self.dataframe_1 = self.dataframe_1.drop_duplicates()

    def add_hours(self, dictionary):
        """
        Добавление строки в таблицу "Часы"
        ----------

        """
        d = pd.DataFrame(columns=['Номер сотрудника', 'Специальность', 'Часы'])
        d.loc[0, :] = dictionary
        self.dataframe_2 = self.dataframe_2.append(d, ignore_index=True)
        if any(self.dataframe_2.duplicated()):
            self.dataframe_2 = self.dataframe_2.drop_duplicates()

    def add_jobs(self, dictionary):
        """
        Добавление строки в таблицу "Работы"
        ----------
        """
        d = pd.DataFrame(columns=['Город', 'Специальность', 'Зарплата в час'])
        d.loc[0, :] = dictionary
        self.dataframe_3 = self.dataframe_3.append(d, ignore_index=True)
        if any(self.dataframe_3.duplicated()):
            self.dataframe_3 = self.dataframe_3.drop_duplicates()

    def delete_full(self, w):
        """

        """
        self.dataframe_1 = self.dataframe_1.drop(
            self.dataframe_1.loc[self.dataframe_1["Номер сотрудника"] == w[0]].index)
        self.dataframe_2 = self.dataframe_2.drop(
            self.dataframe_2.loc[self.dataframe_2["Номер сотрудника"] == w[0]].index)
        self.dataframe_3 = self.dataframe_3.drop(
            self.dataframe_3.loc[
                (self.dataframe_3["Город"]) == w[2] & (self.dataframe_3["Специальность"] == w[4])].index)

    def delete_specialist(self, w_id):
        """
        Удаление строки из базы данных
        ----------
        Параметры:
                w_id - номер сотрудника из удаляемой строки
        ----------
        Возвращает:
        ----------
        Автор: Никоненко А.Р.
        """
        self.dataframe_1 = self.dataframe_1.drop(
            self.dataframe_1.loc[self.dataframe_1["Номер сотрудника"] == w_id].index)

    def delete_hours(self, w_id):
        """
        Удаление строки из базы данных
        ----------
        Параметры:
                w_id - номер сотрудника из удаляемой строки
        ----------
        Возвращает:
        ----------
        Автор: Никоненко А.Р.
        """
        self.dataframe_2 = self.dataframe_2.drop(
            self.dataframe_2.loc[self.dataframe_2["Номер сотрудника"] == w_id].index)

    def delete_jobs(self, city,speciality):
        """
        Удаление строки из базы данных
        ----------
        Параметры:
                w_id - номер сотрудника из удаляемой строки
        ----------
        Возвращает:
        ----------
        Автор: Никоненко А.Р.
        """

        self.dataframe_3 = self.dataframe_3.drop(
            self.dataframe_3.loc[
                (self.dataframe_3["Город"] == city) & (self.dataframe_3["Специальность"] == speciality)].index)

#    def change(self, w_id, array):
#        """
#        Изменение строки в базе данных
#        ----------
#        Параметры:
#                w_id - номер сотрудника в изменяемой строке
#                array - список новой строки
#        ----------
#        Возвращает: -
#        ----------
#        Автор: Никоненко А.Р.
#        """
#        temp = self.dataframe.loc[self.dataframe[
#            "Номер сотрудника"] == w_id].index
#        self.dataframe.loc[temp, :] = array

    def change_full(self, w, dictionary):
        self.dataframe_1 = self.dataframe_1.drop(
            self.dataframe_1.loc[self.dataframe_1["Номер сотрудника"] == w[0]].index)
        self.dataframe_2 = self.dataframe_2.drop(
            self.dataframe_2.loc[self.dataframe_2["Номер сотрудника"] == w[0]].index)
        self.dataframe_3 = self.dataframe_3.drop(
            self.dataframe_3.loc[
                (self.dataframe_3["Город"]) == w[2] & (self.dataframe_3["Специальность"] == w[4])].index)
        d = pd.DataFrame(columns=['Номер сотрудника', 'ФИО', 'Город', 'Номер телефона',
                                  'Специальность', 'Часы', 'Зарплата в час'])
        d.loc[0, :] = dictionary
        df1 = d.loc[:, ['Номер сотрудника', 'ФИО', 'Город', 'Номер телефона']]
        df2 = d.loc[:, ['Номер сотрудника', 'Специальность', 'Часы']]
        df3 = d.loc[:, ['Город', 'Специальность', 'Зарплата в час']]
        self.dataframe_1 = self.dataframe_1.append(df1, ignore_index=True)
        if any(self.dataframe_1.duplicated()):
            self.dataframe_1 = self.dataframe_1.drop_duplicates()
        self.dataframe_2 = self.dataframe_2.append(df2, ignore_index=True)
        if any(self.dataframe_2.duplicated()):
            self.dataframe_2 = self.dataframe_2.drop_duplicates()
        self.dataframe_3 = self.dataframe_3.append(df3, ignore_index=True)
        if any(self.dataframe_3.duplicated()):
            self.dataframe_3 = self.dataframe_3.drop_duplicates()

    def change_specialist(self, w_id, dictionary):
        self.dataframe_1 = self.dataframe_1.drop(
            self.dataframe_1.loc[self.dataframe_1["Номер сотрудника"] == w_id].index)
        d = pd.DataFrame(columns=['Номер сотрудника', 'ФИО', 'Город', 'Номер телефона'])
        d.loc[0, :] = dictionary
        self.dataframe_1 = self.dataframe_1.append(d, ignore_index=True)
        if any(self.dataframe_1.duplicated()):
            self.dataframe_1 = self.dataframe_1.drop_duplicates()

    def change_hours(self, w_id, dictionary):
        self.dataframe_2 = self.dataframe_2.drop(
            self.dataframe_2.loc[self.dataframe_2["Номер сотрудника"] == w_id].index)
        d = pd.DataFrame(columns=['Номер сотрудника', 'Специальность', 'Часы'])
        d.loc[0, :] = dictionary
        self.dataframe_2 = self.dataframe_2.append(d, ignore_index=True)
        if any(self.dataframe_2.duplicated()):
            self.dataframe_2 = self.dataframe_2.drop_duplicates()

    def change_jobs(self, city,speciality, dictionary):
        self.dataframe_3 = self.dataframe_3.drop(
            self.dataframe_3.loc[
                (self.dataframe_3["Город"]) == city & (self.dataframe_3["Специальность"] == speciality)].index)
        d = pd.DataFrame(columns=['Город', 'Специальность', 'Зарплата в час'])
        d.loc[0, :] = dictionary
        self.dataframe_3 = self.dataframe_3.append(d, ignore_index=True)
        if any(self.dataframe_3.duplicated()):
            self.dataframe_3 = self.dataframe_3.drop_duplicates()

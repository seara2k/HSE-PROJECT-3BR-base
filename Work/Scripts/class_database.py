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
        Автор: Никоненко А.Р.
        """
        self.dataframe_all = pd.DataFrame(columns=['Номер сотрудника', 'ФИО', 'Город', 'Номер телефона',
                                                   'Специальность', 'Часы', 'Зарплата в час'])
        self.dataframe_1 = pd.DataFrame(columns=['Номер сотрудника', 'ФИО', 'Город', 'Номер телефона'])
        self.dataframe_2 = pd.DataFrame(columns=['Номер сотрудника', 'Специальность', 'Часы'])
        self.dataframe_3 = pd.DataFrame(columns=['Город', 'Специальность', 'Зарплата в час'])

    def launch_from_one(self, path):
        """
        Создание справочников из таблицы excel
        ----------
        Параметры:
                path - полный путь до файла .xlsx
        ----------
        Возвращает: -
        ----------
        Автор: Никоненко А.Р.
        """
        self.dataframe_all = pd.read_excel(path)
        self.dataframe_all = self.dataframe_all.drop_duplicates()
        self.dataframe_1 = self.dataframe_all.loc[:, ['Номер сотрудника', 'ФИО', 'Город', 'Номер телефона']]
        self.dataframe_1 = self.dataframe_1.drop_duplicates()
        self.dataframe_2 = self.dataframe_all.loc[:, ['Номер сотрудника', 'Специальность', 'Часы']]
        self.dataframe_2 = self.dataframe_2.drop_duplicates()
        self.dataframe_3 = self.dataframe_all.loc[:, ['Город', 'Специальность', 'Зарплата в час']]
        self.dataframe_3 = self.dataframe_3.drop_duplicates()

    def merge(self):
        """
        Создание полной таблицы из справочников
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Никоненко А.Р.
        """
        temp = pd.merge(self.dataframe_1, self.dataframe_2, on="Номер сотрудника")
        self.dataframe_all = pd.merge(temp, self.dataframe_3, on=["Город", "Специальность"])

    def add_specialist(self, dictionary):
        """
        Добавление строки в справочник "Сотрудник"
        ----------
        Параметры:
                dictionary - добавляемая строка
        ----------
        Возвращает: -
        ----------
        Автор: Никоненко А.Р.
        """
        d = pd.DataFrame(columns=['Номер сотрудника', 'ФИО', 'Город', 'Номер телефона'])
        d.loc[0, :] = dictionary
        self.dataframe_1 = self.dataframe_1.append(d, ignore_index=True)
        if any(self.dataframe_1.duplicated()):
            self.dataframe_1 = self.dataframe_1.drop_duplicates()

    def add_hours(self, dictionary):
        """
        Добавление строки в справочник "Часы"
        ----------
        Параметры:
                dictionary - добавляемая строка
        ----------
        Возвращает: -
        ----------
        Автор: Никоненко А.Р.
        """
        d = pd.DataFrame(columns=['Номер сотрудника', 'Специальность', 'Часы'])
        d.loc[0, :] = dictionary
        self.dataframe_2 = self.dataframe_2.append(d, ignore_index=True)
        if any(self.dataframe_2.duplicated()):
            self.dataframe_2 = self.dataframe_2.drop_duplicates()

    def add_jobs(self, dictionary):
        """
        Добавление строки в справочник "Работы"
        ----------
        Параметры:
                dictionary - добавляемая строка
        ----------
        Возвращает: -
        ----------
        Автор: Никоненко А.Р.
        """
        d = pd.DataFrame(columns=['Город', 'Специальность', 'Зарплата в час'])
        d.loc[0, :] = dictionary
        self.dataframe_3 = self.dataframe_3.append(d, ignore_index=True)
        if any(self.dataframe_3.duplicated()):
            self.dataframe_3 = self.dataframe_3.drop_duplicates()

    def delete_specialist(self, w_id):
        """
        Удаление строки из справочника "Сотрудник"
        ----------
        Параметры:
                w_id - номер сотрудника из удаляемой строки
        ----------
        Возвращает: -
        ----------
        Автор: Никоненко А.Р.
        """
        self.dataframe_1 = self.dataframe_1.drop(
            self.dataframe_1.loc[self.dataframe_1["Номер сотрудника"] == w_id].index)

    def delete_hours(self, w_id):
        """
        Удаление строки из справочника "Часы"
        ----------
        Параметры:
                w_id - номер сотрудника из удаляемой строки
        ----------
        Возвращает: -
        ----------
        Автор: Никоненко А.Р.
        """
        self.dataframe_2 = self.dataframe_2.drop(
            self.dataframe_2.loc[self.dataframe_2["Номер сотрудника"] == w_id].index)

    def delete_jobs(self, city, speciality):
        """
        Удаление строки из справочника "Работы"
        ----------
        Параметры:
                city- значение "Город" из удаляемой строки
                speciality - значение "Специальность" из удаляемой строки
        ----------
        Возвращает: -
        ----------
        Автор: Никоненко А.Р.
        """

        self.dataframe_3 = self.dataframe_3.drop(
            self.dataframe_3.loc[
                (self.dataframe_3["Город"] == city) & (self.dataframe_3["Специальность"] == speciality)].index)

    def change_specialist(self, w_id, dictionary):
        """
        Изменение строки в справочнике "Сотрудник"
        ----------
        Параметры:
                w_id - номер сотрудника из изменяемой строки
                dictionary - изменённая строка
        ----------
        Возвращает: -
        ----------
        Автор: Никоненко А.Р.
        """
        self.dataframe_1 = self.dataframe_1.drop(
            self.dataframe_1.loc[self.dataframe_1["Номер сотрудника"] == w_id].index)
        d = pd.DataFrame(columns=['Номер сотрудника', 'ФИО', 'Город', 'Номер телефона'])
        d.loc[0, :] = dictionary
        self.dataframe_1 = self.dataframe_1.append(d, ignore_index=True)
        if any(self.dataframe_1.duplicated()):
            self.dataframe_1 = self.dataframe_1.drop_duplicates()

    def change_hours(self, w_id, dictionary):
        """
        Изменение строки в справочнике "Часы"
        ----------
        Параметры:
                w_id - номер сотрудника из изменяемой строки
                dictionary - изменённая строка
        ----------
        Возвращает: -
        ----------
        Автор: Никоненко А.Р.
        """
        self.dataframe_2 = self.dataframe_2.drop(
            self.dataframe_2.loc[self.dataframe_2["Номер сотрудника"] == w_id].index)
        d = pd.DataFrame(columns=['Номер сотрудника', 'Специальность', 'Часы'])
        d.loc[0, :] = dictionary
        self.dataframe_2 = self.dataframe_2.append(d, ignore_index=True)
        if any(self.dataframe_2.duplicated()):
            self.dataframe_2 = self.dataframe_2.drop_duplicates()

    def change_jobs(self, city, speciality, dictionary):
        """
        Изменение строки в справочнике "Работы"
        ----------
        Параметры:
                city - значение "Город" из изменяемой строки
                speciality - значение "Специальность" из изменяемой строки
                dictionary - изменённая строка
        ----------
        Возвращает: -
        ----------
        Автор: Никоненко А.Р.
        """
        self.dataframe_3 = self.dataframe_3.drop(
            self.dataframe_3.loc[
                (self.dataframe_3["Город"] == city) & (self.dataframe_3["Специальность"] == speciality)].index)
        d = pd.DataFrame(columns=['Город', 'Специальность', 'Зарплата в час'])
        d.loc[0, :] = dictionary
        self.dataframe_3 = self.dataframe_3.append(d, ignore_index=True)
        if any(self.dataframe_3.duplicated()):
            self.dataframe_3 = self.dataframe_3.drop_duplicates()

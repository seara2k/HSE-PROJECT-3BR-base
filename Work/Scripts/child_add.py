import tkinter as tk
from tkinter import ttk, messagebox
from . import constants as const
# pylint: disable=C0103


class child_add(tk.Toplevel):

    def __init__(self, parent, fate):
        """
        Конструктор окна добавления элемента
        ----------
        Параметры:
                parent - класс родителя
                fate - функция, которую будет выполнять окно(либо добавление элемента, либо изменение)
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """
        super().__init__()
        self.fate = fate
        self.parent = parent
        self.init_GUI()

    def init_GUI(self):
        """
        Конструктор интерфейса окна добавления элемента
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """
        if self.fate == "add":
            self.title("Добавить элемент")
        elif self.fate == "change":
            self.title("Изменить элемент")
        elif self.fate == "filter":
            self.title("Выбрать фильтрацию")
        self.geometry(const.add_element_window)
        self.resizable(False, False)

        # Фрейм окна
        adding_group = tk.LabelFrame(self, text='Параметры')
        adding_group.pack(fill=tk.BOTH, expand=1, padx=5, pady=5)

        # Надписи и лейблы с их фреймами
        ID_group = tk.Frame(adding_group)
        ID_group.pack(side=tk.TOP, fill=tk.X)
        lbl_ID = tk.Label(ID_group, text='Номер сотрудника')
        lbl_ID.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)
        if self.fate == "filter":
            values = list(set(self.parent.get_values("ID")))
            values.insert(0, "")
            self.cb_id = ttk.Combobox(ID_group, values=values)
            self.cb_id.pack(
                side=tk.RIGHT, padx=5, pady=5, fill=tk.X)
            self.cb_id.current(0)
        else:
            self.entry_ID = ttk.Entry(ID_group)
            self.entry_ID.pack(side=tk.RIGHT, padx=5, pady=5, fill=tk.X)

        Full_Name_group = tk.Frame(adding_group)
        Full_Name_group.pack(side=tk.TOP, fill=tk.X)
        lbl_Full_Name = tk.Label(Full_Name_group, text='ФИО')
        lbl_Full_Name.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)
        if self.fate == "filter":
            values = list(set(self.parent.get_values("Full_Name")))
            values.insert(0, "")
            self.cb_full_name = ttk.Combobox(Full_Name_group, values=values)
            self.cb_full_name.pack(
                side=tk.RIGHT, padx=5, pady=5, fill=tk.X)
            self.cb_full_name.current(0)
        else:
            self.entry_Full_Name = ttk.Entry(Full_Name_group)
            self.entry_Full_Name.pack(
                side=tk.RIGHT, padx=5, pady=5, fill=tk.X)

        City_group = tk.Frame(adding_group)
        City_group.pack(side=tk.TOP, fill=tk.X)
        lbl_City = tk.Label(City_group, text='Город')
        lbl_City.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)
        if self.fate == "filter":
            values = list(set(self.parent.get_values("City")))
            values.insert(0, "")
            self.cb_city = ttk.Combobox(City_group, values=values)
            self.cb_city.pack(
                side=tk.RIGHT, padx=5, pady=5, fill=tk.X)
            self.cb_city.current(0)
        else:
            self.entry_City = ttk.Entry(City_group)
            self.entry_City.pack(
                side=tk.RIGHT, padx=5, pady=5, fill=tk.X)

        Phone_Number_group = tk.Frame(adding_group)
        Phone_Number_group.pack(side=tk.TOP, fill=tk.X)
        lbl_Phone_Number = tk.Label(Phone_Number_group, text='Номер телефона')
        lbl_Phone_Number.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)
        if self.fate == "filter":
            values = list(set(self.parent.get_values("Phone_Number")))
            values.insert(0, "")
            self.cb_phone_number = ttk.Combobox(
                Phone_Number_group, values=values)
            self.cb_phone_number.pack(
                side=tk.RIGHT, padx=5, pady=5, fill=tk.X)
            self.cb_phone_number.current(0)
        else:
            self.entry_Phone_Number = ttk.Entry(Phone_Number_group)
            self.entry_Phone_Number.pack(
                side=tk.RIGHT, padx=5, pady=5, fill=tk.X)

        Speciality_group = tk.Frame(adding_group)
        Speciality_group.pack(side=tk.TOP, fill=tk.X)
        lbl_Speciality = tk.Label(Speciality_group, text='Специальность')
        lbl_Speciality.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)
        if self.fate == "filter":
            values = list(set(self.parent.get_values("Speciality")))
            values.insert(0, "")
            self.cb_speciality = ttk.Combobox(Speciality_group, values=values)
            self.cb_speciality.pack(
                side=tk.RIGHT, padx=5, pady=5, fill=tk.X)
            self.cb_speciality.current(0)
        else:
            self.entry_Speciality = ttk.Entry(Speciality_group)
            self.entry_Speciality.pack(
                side=tk.RIGHT, padx=5, pady=5, fill=tk.X)

        Time_group = tk.Frame(adding_group)
        Time_group.pack(side=tk.TOP, fill=tk.X)
        lbl_Time = tk.Label(Time_group, text='Часы')
        lbl_Time.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)
        if self.fate == "filter":
            values = list(set(self.parent.get_values("Time")))
            values.insert(0, "")
            self.cb_time = ttk.Combobox(Time_group, values=values)
            self.cb_time.pack(
                side=tk.RIGHT, padx=5, pady=5, fill=tk.X)
            self.cb_time.current(0)
        else:
            self.entry_Time = ttk.Entry(Time_group)
            self.entry_Time.pack(
                side=tk.RIGHT, padx=5, pady=5, fill=tk.X)

        Pays_An_Hour_group = tk.Frame(adding_group)
        Pays_An_Hour_group.pack(side=tk.TOP, fill=tk.X)
        lbl_Pays_An_Hour = tk.Label(Pays_An_Hour_group, text="Зарплата в час")
        lbl_Pays_An_Hour.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)
        if self.fate == "filter":
            values = list(set(self.parent.get_values("Pays_An_Hour")))
            values.insert(0, "")
            self.cb_pays_an_hour = ttk.Combobox(
                Pays_An_Hour_group, values=values)
            self.cb_pays_an_hour.pack(
                side=tk.RIGHT, padx=5, pady=5, fill=tk.X)
            self.cb_pays_an_hour.current(0)
        else:
            self.entry_Pays_An_Hour = ttk.Entry(Pays_An_Hour_group)
            self.entry_Pays_An_Hour.pack(
                side=tk.RIGHT, padx=5, pady=5, fill=tk.X)

        btn_group = tk.Frame(adding_group)
        btn_group.pack(side=tk.TOP, fill=tk.X)
        btn_clear = ttk.Button(
            adding_group, text="Очистить поля", command=self.clear)
        btn_clear.pack(side=tk.LEFT, padx=5, pady=5,
                       fill=tk.X, expand=1)
        btn_accept = ttk.Button(
            adding_group, text="Подтвердить", command=self.go)
        btn_accept.pack(side=tk.RIGHT, padx=5, pady=5, fill=tk.X, expand=1)
        if self.fate == "change":
            tree = self.parent.chosen_tree()
            self.row = getattr(self.parent, tree).item(
                getattr(self.parent, tree).selection())["values"]
            self.id_check = self.row[0]
            self.entry_ID.insert(0, self.row[0])
            self.entry_Full_Name.insert(0, self.row[1])
            self.entry_City.insert(0, self.row[2])
            self.entry_Phone_Number.insert(0, self.row[3])
            self.entry_Speciality.insert(0, self.row[4])
            self.entry_Time.insert(0, self.row[5])
            self.entry_Pays_An_Hour.insert(0, self.row[6])
        # Не даёт перейти в другое окно
        self.grab_set()
        self.focus_set()

    def go(self):
        """
        Начало работы окна, либо добавление либо изменение значений таблицы
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """
        if self.fate == "add":
            if self.check_input():
                if self.parent.get_values("ID").count(self.entry_ID.get()) >= 1:
                    messagebox.showerror(
                        title="Ошибка ввода",
                        message="Такой номер сотрудника уже есть", parent=self)
                    self.grab_set()
                    self.focus_set()
                else:
                    self.parent.add([int(self.entry_ID.get()),
                                     str(self.entry_Full_Name.get(
                                     )),
                                     str(self.entry_City.get(
                                     )),
                                     str(self.entry_Phone_Number.get(
                                     )),
                                     str(self.entry_Speciality.get(
                                     )),
                                     int(self.entry_Time.get(
                                     )),
                                     int(self.entry_Pays_An_Hour.get())])
            else:
                messagebox.showerror(
                    title="Ошибка ввода",
                    message="Ввод должен быть в формате:\nЧисло\nСтрока\nСтрока\nСтрока или число\nСтрока\nЧисло\nЧисло\nТакже недопускается пустой ввод.",
                    parent=self)
                self.grab_set()
                self.focus_set()
        if self.fate == "change":
            if self.check_input():
                if (self.parent.get_values("ID").count(self.entry_ID.get()) >= 1) and (int(self.entry_ID.get()) != self.id_check):
                    messagebox.showerror(
                        title="Ошибка ввода",
                        message="Такой номер сотрудника уже есть", parent=self)
                    self.grab_set()
                    self.focus_set()
                else:
                    self.parent.change_row(self.row[0], [int(self.entry_ID.get()),
                                                         str(self.entry_Full_Name.get(
                                                         )),
                                                         str(self.entry_City.get(
                                                         )),
                                                         str(self.entry_Phone_Number.get(
                                                         )),
                                                         str(self.entry_Speciality.get(
                                                         )),
                                                         int(self.entry_Time.get(
                                                         )),
                                                         int(self.entry_Pays_An_Hour.get())])
                    self.destroy()
            else:
                messagebox.showerror(
                    title="Ошибка ввода",
                    message="Ввод должен быть в формате:\nчисло\nстрока\nстрока\nстрока или число\nстрока\nчисло\nчисло,\nТакже недопускается пустой ввод.",
                    parent=self)
                self.grab_set()
                self.focus_set()
            self.parent.eg_btn_edit.config(state="disabled")
        if self.fate == "filter":
            filtered_dataframe = self.parent.filter(self.cb_id.get(),
                                                    self.cb_full_name.get(),
                                                    self.cb_city.get(),
                                                    self.cb_phone_number.get(),
                                                    self.cb_speciality.get(),
                                                    self.cb_time.get(),
                                                    self.cb_pays_an_hour.get())

            self.parent.refresh_from_database(filtered_dataframe)
            self.parent.filtered = 1
            self.parent.filtered_dataframe = filtered_dataframe
            self.destroy()

    def check_input(self):
        """
        Проверка на ввод в окне добавления элемента
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """
        true_value_output = ["int", "str", "str", "str", "int", "int"]
        value_array = [self.entry_ID.get(),
                       self.entry_Full_Name.get(),
                       self.entry_City.get(),
                       self.entry_Speciality.get(),
                       self.entry_Time.get(),
                       self.entry_Pays_An_Hour.get()]
        value_output = []

        for value in value_array:
            try:
                temp = int(value)
                value_output.append("int")
            except ValueError:
                temp = str(value)
                value_output.append("str")
        return true_value_output == value_output

    def clear(self):
        """
        Очиста значений, введённых в окно добавления элемента
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """
        if self.fate == "filter":
            self.cb_id.current(0)
            self.cb_full_name.current(0)
            self.cb_city.current(0)
            self.cb_phone_number.current(0)
            self.cb_speciality.current(0)
            self.cb_time.current(0)
            self.cb_pays_an_hour.current(0)
        else:
            self.entry_ID.delete(0, tk.END)
            self.entry_Full_Name.delete(0, tk.END)
            self.entry_Phone_Number.delete(0, tk.END)
            self.entry_City.delete(0, tk.END)
            self.entry_Speciality.delete(0, tk.END)
            self.entry_Time.delete(0, tk.END)
            self.entry_Pays_An_Hour.delete(0, tk.END)

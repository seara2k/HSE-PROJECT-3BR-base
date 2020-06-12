import tkinter as tk
from tkinter import ttk

# pylint: disable=C0103


class child_add(tk.Toplevel):

    def __init__(self, parent, fate):
        """
        Конструктор окна добавления элемента
        Параметры: parent -
                   fate -
        Возвращает: -
        Автор: Литвинов В.С.
        """
        super().__init__()
        self.fate = fate
        self.parent = parent
        self.init_GUI()

    def init_GUI(self):
        """
        Конструктор интерфейса окна добавления элемента
        Параметры: -
        Возвращает: -
        Автор: Литвинов В.С.
        """
        self.title("Добавить элемент")
        self.geometry('300x295')
        self.resizable(False, False)

        # Фрейм окна
        adding_group = tk.LabelFrame(self, text='Параметры')
        adding_group.pack(fill=tk.BOTH, expand=1, padx=5, pady=5)

        # Надписи и лейблы с их фреймами
        ID_group = tk.Frame(adding_group)
        ID_group.pack(side=tk.TOP, fill=tk.X)
        lbl_ID = tk.Label(ID_group, text='Номер сотрудника')
        lbl_ID.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)
        self.entry_ID = ttk.Entry(ID_group)
        self.entry_ID.pack(side=tk.RIGHT, padx=5, pady=5, fill=tk.X)

        Full_Name_group = tk.Frame(adding_group)
        Full_Name_group.pack(side=tk.TOP, fill=tk.X)
        lbl_Full_Name = tk.Label(Full_Name_group, text='ФИО')
        lbl_Full_Name.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)
        self.entry_Full_Name = ttk.Entry(Full_Name_group)
        self.entry_Full_Name.pack(
            side=tk.RIGHT, padx=5, pady=5, fill=tk.X)

        City_group = tk.Frame(adding_group)
        City_group.pack(side=tk.TOP, fill=tk.X)
        lbl_City = tk.Label(City_group, text='Город')
        lbl_City.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)
        self.entry_City = ttk.Entry(City_group)
        self.entry_City.pack(
            side=tk.RIGHT, padx=5, pady=5, fill=tk.X)

        Phone_Number_group = tk.Frame(adding_group)
        Phone_Number_group.pack(side=tk.TOP, fill=tk.X)
        lbl_Phone_Number = tk.Label(Phone_Number_group, text='Номер телефона')
        lbl_Phone_Number.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)
        self.entry_Phone_Number = ttk.Entry(Phone_Number_group)
        self.entry_Phone_Number.pack(
            side=tk.RIGHT, padx=5, pady=5, fill=tk.X)

        Speciality_group = tk.Frame(adding_group)
        Speciality_group.pack(side=tk.TOP, fill=tk.X)
        lbl_Speciality = tk.Label(Speciality_group, text='Специальность')
        lbl_Speciality.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)
        self.entry_Speciality = ttk.Entry(Speciality_group)
        self.entry_Speciality.pack(
            side=tk.RIGHT, padx=5, pady=5, fill=tk.X)

        Time_group = tk.Frame(adding_group)
        Time_group.pack(side=tk.TOP, fill=tk.X)
        lbl_Time = tk.Label(Time_group, text='Часы')
        lbl_Time.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)
        self.entry_Time = ttk.Entry(Time_group)
        self.entry_Time.pack(
            side=tk.RIGHT, padx=5, pady=5, fill=tk.X)

        Pays_An_Hour_group = tk.Frame(adding_group)
        Pays_An_Hour_group.pack(side=tk.TOP, fill=tk.X)
        lbl_Pays_An_Hour = tk.Label(Pays_An_Hour_group, text="Зарплата в час")
        lbl_Pays_An_Hour.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)
        self.entry_Pays_An_Hour = ttk.Entry(Pays_An_Hour_group)
        self.entry_Pays_An_Hour.pack(
            side=tk.RIGHT, padx=5, pady=5, fill=tk.X)

        btn_group = tk.Frame(adding_group)
        btn_group.pack(side=tk.TOP, fill=tk.X)
        btn_clear = ttk.Button(
            adding_group, text="Очистить поля", command=self.clear)
        btn_clear.pack(side=tk.LEFT, padx=5, pady=5,
                       fill=tk.X, expand=1)
        btn_accept = ttk.Button(adding_group, text="Подтвердить")
        btn_accept.pack(side=tk.RIGHT, padx=5, pady=5, fill=tk.X, expand=1)
        if self.fate == "add":
            btn_accept.bind('<Button-1>', lambda event: self.parent.add([int(self.entry_ID.get()),
                                                                         self.entry_Full_Name.get(),
                                                                         self.entry_City.get(),
                                                                         self.entry_Phone_Number.get(),
                                                                         self.entry_Speciality.get(),
                                                                         self.entry_Time.get(),
                                                                         self.entry_Pays_An_Hour.get()]))
        if self.fate == "change":
            tree = self.parent.chosen_tree()
            row = getattr(self.parent, tree).item(
                getattr(self.parent, tree).selection())["values"]
            self.entry_ID.insert(0, row[0])
            self.entry_Full_Name.insert(0, row[1])
            self.entry_Phone_Number.insert(0, row[2])
            self.entry_City.insert(0, row[3])
            self.entry_Speciality.insert(0, row[4])
            self.entry_Time.insert(0, row[5])
            self.entry_Pays_An_Hour.insert(0, row[6])
            btn_accept.bind('<Button-1>', lambda event: (self.parent.change_row(row[0], [self.entry_ID.get(),
                                                                                         self.entry_Full_Name.get(),
                                                                                         self.entry_City.get(),
                                                                                         self.entry_Phone_Number.get(),
                                                                                         self.entry_Speciality.get(),
                                                                                         self.entry_Time.get(),
                                                                                         self.entry_Pays_An_Hour.get()]), self.destroy()))
            self.parent.eg_btn_edit.config(state="disabled")
        # Не даёт перейти в другое окно
        self.grab_set()
        self.focus_set()

    def clear(self):
        """
        Очиста значений, введённых в окно добавления элемента
        Параметры: -
        Возвращает: -
        Автор: Литвинов В.С.
        """
        self.entry_ID.delete(0, tk.END)
        self.entry_Full_Name.delete(0, tk.END)
        self.entry_Phone_Number.delete(0, tk.END)
        self.entry_City.delete(0, tk.END)
        self.entry_Speciality.delete(0, tk.END)
        self.entry_Time.delete(0, tk.END)
        self.entry_Pays_An_Hour.delete(0, tk.END)

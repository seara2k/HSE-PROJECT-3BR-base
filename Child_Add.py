from tkinter import Tk, ttk, messagebox
import tkinter as tk


class Child_Add(tk.Toplevel):

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title("Добавить элемент")
        self.geometry('300x290')
        self.resizable(False, False)

        adding_group = tk.LabelFrame(self, text='Параметры')
        adding_group.pack(fill=tk.BOTH, expand=1, padx=5, pady=5)

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

        Phone_Number_group = tk.Frame(adding_group)
        Phone_Number_group.pack(side=tk.TOP, fill=tk.X)
        lbl_Phone_Number = tk.Label(Phone_Number_group, text='Номер телефона')
        lbl_Phone_Number.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)
        self.entry_Phone_Number = ttk.Entry(Phone_Number_group)
        self.entry_Phone_Number.pack(
            side=tk.RIGHT, padx=5, pady=5, fill=tk.X)

        City_group = tk.Frame(adding_group)
        City_group.pack(side=tk.TOP, fill=tk.X)
        lbl_City = tk.Label(City_group, text='Город')
        lbl_City.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)
        self.entry_City = ttk.Entry(City_group)
        self.entry_City.pack(
            side=tk.RIGHT, padx=5, pady=5, fill=tk.X)

        Specialty_group = tk.Frame(adding_group)
        Specialty_group.pack(side=tk.TOP, fill=tk.X)
        lbl_Specialty = tk.Label(Specialty_group, text='Специальность')
        lbl_Specialty.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)
        self.entry_Specialty = ttk.Entry(Specialty_group)
        self.entry_Specialty.pack(
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
        btn_close = ttk.Button(adding_group, text="Очистить поля")
        btn_close.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=1)
        btn_accept = ttk.Button(adding_group, text="Подтвердить")
        btn_accept.pack(side=tk.RIGHT, padx=5, pady=5, fill=tk.X, expand=1)

        # btn_add = ttk.Button(adding_group, text="Добавить")
        # btn_add.place(x=150, y=350)
        # btn_add.bind('<Button-1>', lambda event: self.view.record(self.entry_ID.get(),
        #                                                           self.entry_Full_Name.get(),
        #                                                           self.entry_Phone_Number.get(),
        #                                                           self.entry_City.get()))

        # Не даёт перейти в другое окно
        self.grab_set()
        self.focus_set()

if __name__ == "__main__":
    pass

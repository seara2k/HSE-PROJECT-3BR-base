# -*- coding: utf-8 -*-
from tkinter import Tk, ttk, messagebox
import tkinter as tk
from tkinter.ttk import Checkbutton
import numpy as np
import pandas as pd
# import get_data
# import firsttab
# import secondtab
import sqlite3


def get_filtr():
    pass


def export():
    pass


def editing():
    pass


def deleting():  # не работает пока что
    item = tree.selection()[0]
    tree.delete(item)


class Main(tk.Frame):

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.widgets()
        root.title("I LOVE POLYAKOV")
        root.geometry("1000x600")
        root.resizable(False, False)
        self.view_records()

    # def grid(self):

    def widgets(self):

        menubar = tk.Menu(root)
        menubar.add_command(label="File")
        menubar.add_command(label="Quit", command=root.quit())

        root.config(menu=menubar)

        # mainmenu = Menu(root)
        # root.config(menu=mainmenu)

        filemenu = tk.Menu(mainmenu, tearoff=0)
        filemenu.add_command(label="Открыть...")
        filemenu.add_command(label="Новый")
        filemenu.add_command(label="Сохранить...")
        filemenu.add_command(label="Выход")

        helpmenu = tk.Menu(mainmenu, tearoff=0)
        helpmenu.add_command(label="Помощь")
        helpmenu.add_command(label="О программе")

        mainmenu.add_cascade(label="Файл", menu=filemenu)
        mainmenu.add_cascade(label="Справка", menu=helpmenu)

    def init_main(self):

        def analyze1():
            messagebox.showinfo(
                'Предупреждение', 'Невозможно произвести анализ с данными параметрами')

        def analyze2():
            messagebox.showinfo(
                'Предупреждение', 'Невозможно произвести анализ с данными параметрами')

        def analyze3():
            messagebox.showinfo(
                'Предупреждение', 'Невозможно произвести анализ с данными параметрами')

        def analyze4():
            messagebox.showinfo(
                'Предупреждение', 'Невозможно произвести анализ с данными параметрами')

        def analyze5():
            messagebox.showinfo(
                'Предупреждение', 'Невозможно произвести анализ с данными параметрами')

        def analyze6():
            messagebox.showinfo(
                'Предупреждение', 'Невозможно произвести анализ с данными параметрами')

        def get_analysis():
            choosen_analysis = combobox_2.get()
            if (choosen_analysis == "Базовая статистика"):
                dialog1 = Tk()
                dialog1.title('Параметры базовой статистики')
                dialog1.geometry('300x300+400+300')
                dialog1.resizable(False, False)
                dialog1.title = ttk.Checkbutton(dialog1, text='Название')
                dialog1.title.place(x=50, y=30)
                dialog1.city = ttk.Checkbutton(dialog1, text='Город')
                dialog1.city.place(x=50, y=60)
                dialog1.region = ttk.Checkbutton(dialog1, text='Регион')
                dialog1.region.place(x=50, y=90)
                dialog1.contacts = ttk.Checkbutton(dialog1, text='Контакты')
                dialog1.contacts.place(x=50, y=120)
                dialog1.additional_information = ttk.Checkbutton(
                    dialog1, text='Дополнительная информация')
                dialog1.additional_information.place(x=50, y=150)
                dialog1.numerical1 = ttk.Checkbutton(dialog1, text='Пустая1')
                dialog1.numerical1.place(x=50, y=180)
                dialog1.numerical2 = ttk.Checkbutton(dialog1, text='Пустая2')
                dialog1.numerical2.place(x=50, y=210)

                dialog1.btn_ok = ttk.Button(
                    dialog1, text='Начать анализ', command=analyze1)
                dialog1.btn_ok.place(x=50, y=250)
                btn_cancel = ttk.Button(
                    dialog1, text='Закрыть', command=dialog1.destroy)
                btn_cancel.place(x=150, y=250)

                dialog1.grab_set()
                dialog1.focus_set()
                dialog1.mainloop()
            elif (choosen_analysis == 'Сводная таблица'):
                dialog2 = Tk()
                dialog2.title('Параметры сводной таблицы')
                dialog2.geometry('400x220+400+300')
                dialog2.resizable(False, False)

                label_quality1 = tk.Label(
                    dialog2, text='Качественный столбец 1')
                label_quality1.place(x=50, y=50)
                label_quality2 = tk.Label(
                    dialog2, text='Качественный столбец 2')
                label_quality2.place(x=50, y=80)
                label_numerical = tk.Label(dialog2, text='Численный столбец')
                label_numerical.place(x=50, y=110)
                dialog2.entry_quality1 = ttk.Combobox(dialog2, values=[
                                                      u'Название', u'Город', u'Регион', u'Контакты', u'Дополнительная информация'])
                dialog2.entry_quality1.current(0)
                dialog2.entry_quality1.place(x=200, y=50)
                dialog2.entry_quality2 = ttk.Combobox(dialog2, values=[
                                                      u'Название', u'Город', u'Регион', u'Контакты', u'Дополнительная информация'])
                dialog2.entry_quality2.current(0)
                dialog2.entry_quality2.place(x=200, y=80)

                dialog2.entry_numerical = ttk.Combobox(
                    dialog2, values=[u'', u''])
                dialog2.entry_numerical.current(0)
                dialog2.entry_numerical.place(x=200, y=110)

                btn_cancel = ttk.Button(
                    dialog2, text='Закрыть', command=dialog2.destroy)
                btn_cancel.place(x=300, y=170)

                dialog2.btn_ok = ttk.Button(
                    dialog2, text='Начать анализ', command=analyze2)
                dialog2.btn_ok.place(x=200, y=170)
                dialog2.btn_ok.bind('<Button-1>', lambda event: dialog2.view.records(dialog2.entry_quality1.get(),
                                                                                     dialog2.entry_quality1.get(),
                                                                                     dialog2.entry_numerical.get()))

                dialog2.grab_set()  # перехват всех событий, происходящих в приложении
                dialog2.focus_set()  # захват и удержание фокуса
                dialog2.mainloop()
            elif (choosen_analysis == 'Столбчатая диаграмма'):
                dialog3 = Tk()
                dialog3.title('Параметры столбчатой диаграммы')
                dialog3.geometry('400x220+400+300')
                dialog3.resizable(False, False)

                label_quality1 = tk.Label(
                    dialog3, text='Качественный столбец 1')
                label_quality1.place(x=50, y=50)
                label_quality2 = tk.Label(
                    dialog3, text='Качественный столбец 2')
                label_quality2.place(x=50, y=100)
                dialog3.entry_quality1 = ttk.Combobox(dialog3, values=[
                                                      u'Название', u'Город', u'Регион', u'Контакты', u'Дополнительная информация'])
                dialog3.entry_quality1.current(0)
                dialog3.entry_quality1.place(x=200, y=50)
                dialog3.entry_quality2 = ttk.Combobox(dialog3, values=[
                                                      u'Название', u'Город', u'Регион', u'Контакты', u'Дополнительная информация'])
                dialog3.entry_quality2.current(0)
                dialog3.entry_quality2.place(x=200, y=100)

                btn_cancel = ttk.Button(
                    dialog3, text='Закрыть', command=dialog3.destroy)
                btn_cancel.place(x=300, y=170)

                dialog3.btn_ok = ttk.Button(
                    dialog3, text='Начать анализ', command=analyze3)
                dialog3.btn_ok.place(x=200, y=170)
                dialog3.btn_ok.bind('<Button-1>', lambda event: dialog3.view.records(dialog3.entry_quality1.get(),
                                                                                     dialog3.entry_quality2.get(),
                                                                                     ))

                dialog3.grab_set()  # перехват всех событий, происходящих в приложении
                dialog3.focus_set()  # захват и удержание фокуса
                dialog3.mainloop()
            elif (choosen_analysis == 'Гистограмма'):
                dialog4 = Tk()
                dialog4.title('Параметры гистограммы')
                dialog4.geometry('400x220+400+300')
                dialog4.resizable(False, False)

                label_quality1 = tk.Label(dialog4, text='Качественный столбец')
                label_quality1.place(x=50, y=50)
                label_numerical = tk.Label(dialog4, text='Численный столбец')
                label_numerical.place(x=50, y=100)
                dialog4.entry_quality1 = ttk.Combobox(dialog4, values=[
                                                      u'Название', u'Город', u'Регион', u'Контакты', u'Дополнительная информация'])
                dialog4.entry_quality1.current(0)
                dialog4.entry_quality1.place(x=200, y=50)
                dialog4.entry_numerical = ttk.Combobox(
                    dialog4, values=[u'', u''])
                dialog4.entry_numerical.current(0)
                dialog4.entry_numerical.place(x=200, y=100)

                btn_cancel = ttk.Button(
                    dialog4, text='Закрыть', command=dialog4.destroy)
                btn_cancel.place(x=300, y=170)

                dialog4.btn_ok = ttk.Button(
                    dialog4, text='Начать анализ', command=analyze4)
                dialog4.btn_ok.place(x=200, y=170)
                dialog4.btn_ok.bind('<Button-1>', lambda event: dialog4.view.records(dialog4.entry_quality1.get(),
                                                                                     dialog4.entry_numerical.get()))

                dialog4.grab_set()  # перехват всех событий, происходящих в приложении
                dialog4.focus_set()  # захват и удержание фокуса
                dialog4.mainloop()
            elif (choosen_analysis == 'Диаграмма Бокса-Вискера'):
                dialog5 = Tk()
                dialog5.title('Параметры Диаграммы Бокса-Вискера')
                dialog5.geometry('400x220+400+300')
                dialog5.resizable(False, False)

                label_quality1 = tk.Label(dialog5, text='Качественный столбец')
                label_quality1.place(x=50, y=50)
                label_numerical = tk.Label(dialog5, text='Численный столбец')
                label_numerical.place(x=50, y=100)
                dialog5.entry_quality1 = ttk.Combobox(dialog5, values=[
                                                      u'Название', u'Город', u'Регион', u'Контакты', u'Дополнительная информация'])
                dialog5.entry_quality1.current(0)
                dialog5.entry_quality1.place(x=200, y=50)
                dialog5.entry_numerical = ttk.Combobox(
                    dialog5, values=[u'', u''])
                dialog5.entry_numerical.current(0)
                dialog5.entry_numerical.place(x=200, y=100)

                btn_cancel = ttk.Button(
                    dialog5, text='Закрыть', command=dialog5.destroy)
                btn_cancel.place(x=300, y=170)

                dialog5.btn_ok = ttk.Button(
                    dialog5, text='Начать анализ', command=analyze5)
                dialog5.btn_ok.place(x=200, y=170)
                dialog5.btn_ok.bind('<Button-1>', lambda event: dialog5.view.records(dialog5.entry_quality1.get(),
                                                                                     dialog5.entry_numerical.get()))

                dialog5.grab_set()  # перехват всех событий, происходящих в приложении
                dialog5.focus_set()  # захват и удержание фокуса
                dialog5.mainloop()
            elif (choosen_analysis == 'Диаграмма рассеивания'):
                dialog6 = Tk()
                dialog6.title('Параметры диаграммы рассеивания')
                dialog6.geometry('400x220+400+300')
                dialog6.resizable(False, False)

                label_quality1 = tk.Label(dialog6, text='Качественный столбец')
                label_quality1.place(x=50, y=50)
                label_numerical1 = tk.Label(
                    dialog6, text='Численный столбец 1')
                label_numerical1.place(x=50, y=80)
                label_numerical2 = tk.Label(
                    dialog6, text='Численный столбец 2')
                label_numerical2.place(x=50, y=110)
                dialog6.entry_quality1 = ttk.Combobox(dialog6, values=[
                                                      u'Название', u'Город', u'Регион', u'Контакты', u'Дополнительная информация'])
                dialog6.entry_quality1.current(0)
                dialog6.entry_quality1.place(x=200, y=50)
                dialog6.entry_numerical1 = ttk.Combobox(
                    dialog6, values=[u'', u''])
                dialog6.entry_numerical1.current(0)
                dialog6.entry_numerical1.place(x=200, y=80)
                dialog6.entry_numerical2 = ttk.Combobox(
                    dialog6, values=[u'', u''])
                dialog6.entry_numerical2.current(0)
                dialog6.entry_numerical2.place(x=200, y=110)

                btn_cancel = ttk.Button(
                    dialog6, text='Закрыть', command=dialog6.destroy)
                btn_cancel.place(x=300, y=170)

                dialog6.btn_ok = ttk.Button(
                    dialog6, text='Начать анализ', command=analyze6)
                dialog6.btn_ok.place(x=200, y=170)
                dialog6.btn_ok.bind('<Button-1>', lambda event: dialog6.view.records(dialog6.entry_quality1.get(),
                                                                                     dialog6.entry_numerical1.get(),
                                                                                     dialog6.entry_numerical2.get()))

                dialog6.grab_set()  # перехват всех событий, происходящих в приложении
                dialog6.focus_set()  # захват и удержание фокуса
                dialog6.mainloop()

        toolbar = tk.Frame(bd=10)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        editing_group = tk.LabelFrame(toolbar, text='Таблица')
        editing_group.pack(side=tk.LEFT, padx=70, pady=0)
        btn_open_dialog = tk.Button(
            editing_group, text='Добавить строку', command=self.open_dialog)
        btn_open_dialog.pack(side=tk.TOP, padx=10, pady=10)
        button_edit = tk.Button(editing_group, text="Изменить",
                                command=editing)
        button_edit.pack(side=tk.TOP, padx=10, pady=10)
        button_delete = tk.Button(editing_group, text="Удалить",
                                  command=deleting)
        button_delete.pack(side=tk.BOTTOM, padx=10, pady=10)
        button_delete = tk.Button(editing_group, text="Экспорт",
                                  command=export)
        button_delete.pack(side=tk.BOTTOM, padx=10, pady=10)
        analysis_group = tk.LabelFrame(toolbar, text='Метод анализа')
        analysis_group.pack(side=tk.LEFT, padx=70, pady=0)
        combobox_2 = ttk.Combobox(analysis_group,
                                  values=["Базовая статистика",
                                          "Сводная таблица",
                                          "Столбчатая диаграмма",
                                          "Гистограмма",
                                          "Диаграмма Бокса-Вискера",
                                          "Диаграмма рассеивания"])
        combobox_2.pack(side=tk.TOP, padx=30, pady=20)
        combobox_2.current(0)
        button_method = tk.Button(analysis_group, text="Выбрать",
                                  command=get_analysis)
        button_method.pack(side=tk.TOP, padx=30, pady=20)
        button_delete = tk.Button(analysis_group, text="Экспорт",
                                  command=export)
        button_delete.pack(side=tk.BOTTOM, padx=30, pady=20)
        filtr_group = tk.LabelFrame(toolbar, text='Фильтры')
        filtr_group.pack(side=tk.LEFT, padx=70, pady=0)
        combobox_3 = ttk.Combobox(filtr_group,
                                  values=["Номер сотрудника",
                                          "ФИО",
                                          "Номер телефона",
                                          "Город"])
        combobox_3.pack(side=tk.TOP, padx=30, pady=20)
        combobox_3.current(0)
        button_method2 = tk.Button(filtr_group, text="Отфильтровать",
                                   command=get_filtr)
        button_method2.pack(side=tk.TOP, padx=30, pady=20)

        self.tree = ttk.Treeview(self, columns=(
            'ID', 'Full_Name', "Phone_Number", "City"), height=100, show='headings')
        self.tree.column('ID', width=230, anchor=tk.CENTER)
        self.tree.column('Full_Name', width=230, anchor=tk.CENTER)
        self.tree.column("Phone_Number", width=230, anchor=tk.CENTER)
        self.tree.column("City", width=230, anchor=tk.CENTER)

        self.tree.heading('ID', text='Номер сотрудника')
        self.tree.heading('Full_Name', text='ФИО')
        self.tree.heading("Phone_Number", text="Номер телефона")
        self.tree.heading("City", text="Город")

        self.tree.pack()

    def record(self, ID, Full_Name, Phone_Number, City):
        self.db.insert_data(ID, Full_Name, Phone_Number, City)
        self.view_records()

    def view_records(self):
        self.db.c.execute('''SELECT * FROM database''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row)
         for row in self.db.c.fetchall()]

    def open_dialog(self):
        Child()


class Child(tk.Toplevel):

    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title("Добавить строку")
        self.geometry('300x400')
        self.resizable(False, False)

        label_ID = tk.Label(self, text='Номер сотрудника')
        label_ID.place(x=30, y=50)

        label_Full_Name = tk.Label(self, text='ФИО')
        label_Full_Name.place(x=30, y=100)

        label_Phone_Number = tk.Label(self, text="Номер телефона")
        label_Phone_Number.place(x=30, y=150)

        label_City = tk.Label(self, text="Город")
        label_City.place(x=30, y=200)

        self.entry_ID = ttk.Entry(self)
        self.entry_ID.place(x=150, y=50)

        self.entry_Full_Name = ttk.Entry(self)
        self.entry_Full_Name.place(x=150, y=100)

        self.entry_Phone_Number = ttk.Entry(self)
        self.entry_Phone_Number.place(x=150, y=150)

        self.entry_City = ttk.Entry(self)
        self.entry_City.place(x=150, y=200)

        # добавить u
        #self.combobox = ttk.Combobox(self, values=["LOLO", "DADADA"])
        # self.combobox.current(0)
        #self.combobox.place(x=100, y=20)

        btn_close = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_close.place(x=30, y=350)

        btn_add = ttk.Button(self, text="Добавить")
        btn_add.place(x=150, y=350)
        btn_add.bind('<Button-1>', lambda event: self.view.record(self.entry_ID.get(),
                                                                  self.entry_Full_Name.get(),
                                                                  self.entry_Phone_Number.get(),
                                                                  self.entry_City.get()))

        # Не даёт перейти в другое окно
        self.grab_set()
        self.focus_set()


class DB:

    def __init__(self):

        self.conn = sqlite3.connect("database.pickle")
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS database(ID integer primary key,Full_Name text,Phone_Number text,City text)''')
        self.conn.commit()

    def insert_data(self, ID, Full_Name, Phone_Number, City):
        self.c.execute(
            '''INSERT INTO database(ID,Full_Name,Phone_Number,City) VALUES (?,?,?,?)''',
            (ID, Full_Name, Phone_Number, City))
        self.conn.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.mainloop()

    

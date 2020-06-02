from tkinter import Tk, ttk, messagebox
import tkinter as tk

#pylint: disable=C0103

class Child_Analysis(tk.Toplevel):

    def __init__(self,root,app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        choosen_analysis = fg_cb_filter.get()
        if (choosen_analysis == "Базовая статистика"):
            dialog1 = Tk()
            dialog1.title('Параметры базовой статистики')
            dialog1.geometry('300x300+400+300')
            dialog1.resizable(False, False)
            dialog1.title = ttk.Checkbutton(
                dialog1, text='Номер сотрудника')
            dialog1.title.place(x=50, y=30)
            dialog1.city = ttk.Checkbutton(dialog1, text='ФИО')
            dialog1.city.place(x=50, y=60)
            dialog1.region = ttk.Checkbutton(dialog1, text='Телефон')
            dialog1.region.place(x=50, y=90)
            dialog1.contacts = ttk.Checkbutton(dialog1, text='Город')
            dialog1.contacts.place(x=50, y=120)
            dialog1.numerical1 = ttk.Checkbutton(dialog1, text='Пустая1')
            dialog1.numerical1.place(x=50, y=150)
            dialog1.numerical2 = ttk.Checkbutton(dialog1, text='Пустая2')
            dialog1.numerical2.place(x=50, y=180)

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
            dialog2.entry_quality1 = ttk.Combobox(
                dialog2, values=[u'ФИО', u'Город'])
            dialog2.entry_quality1.current(0)
            dialog2.entry_quality1.place(x=200, y=50)
            dialog2.entry_quality2 = ttk.Combobox(
                dialog2, values=[u'ФИО', u'Город'])
            dialog2.entry_quality2.current(0)
            dialog2.entry_quality2.place(x=200, y=80)

            dialog2.entry_numerical = ttk.Combobox(
                dialog2, values=[u'Номер сотрудника', u'Телефон'])
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
            dialog3.entry_quality1 = ttk.Combobox(
                dialog3, values=[u'ФИО', u'Город'])
            dialog3.entry_quality1.current(0)
            dialog3.entry_quality1.place(x=200, y=50)
            dialog3.entry_quality2 = ttk.Combobox(
                dialog3, values=[u'ФИО', u'Город'])
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
            dialog4.entry_quality1 = ttk.Combobox(
                dialog4, values=[u'ФИО', u'Город'])
            dialog4.entry_quality1.current(0)
            dialog4.entry_quality1.place(x=200, y=50)
            dialog4.entry_numerical = ttk.Combobox(
                dialog4, values=[u'Номер сотрудника', u'Телефон'])
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
            dialog5.entry_quality1 = ttk.Combobox(
                dialog5, values=[u'ФИО', u'Город'])
            dialog5.entry_quality1.current(0)
            dialog5.entry_quality1.place(x=200, y=50)
            dialog5.entry_numerical = ttk.Combobox(
                dialog5, values=[u'Номер сотрудника', u'Телефон'])
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
            dialog6.entry_quality1 = ttk.Combobox(
                dialog6, values=[u'ФИО', u'Город'])
            dialog6.entry_quality1.current(0)
            dialog6.entry_quality1.place(x=200, y=50)
            dialog6.entry_numerical1 = ttk.Combobox(
                dialog6, values=[u'Номер сотрудника', u'Телефон'])
            dialog6.entry_numerical1.current(0)
            dialog6.entry_numerical1.place(x=200, y=80)
            dialog6.entry_numerical2 = ttk.Combobox(
                dialog6, values=[u'Номер сотрудника', u'Телефон'])
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

if __name__ == "__main__":
    pass
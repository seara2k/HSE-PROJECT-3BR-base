from tkinter import Tk, ttk, messagebox
import tkinter as tk

#pylint: disable=C0103

class child_histogram(tk.Toplevel):

    def __init__(self, root, app):
        super().__init__(root)
        self.init_GUI()
        self.view = app

    def init_GUI(self):
        self.title("Параметры гистограммы")
        self.geometry('340x160')
        self.resizable(False, False)

        # Фрейм окна
        summary_table_group = tk.LabelFrame(self, text='Параметры гистограммы')
        summary_table_group.pack(fill=tk.BOTH, expand=1, padx=5, pady=5)

        # Надписи и лейблы с их фреймами
        kach_col_group=tk.Frame(summary_table_group)
        kach_col_group.pack(side=tk.TOP, fill=tk.X)

        lbl_kach_col = tk.Label(kach_col_group, text="Качественный столбец")
        lbl_kach_col.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)

        cb_kach_col = ttk.Combobox(kach_col_group, values=["ФИО","Город"])
        cb_kach_col.pack(side=tk.RIGHT, padx=5, pady=5)
        cb_kach_col.current(0)

        numeral_group=tk.Frame(summary_table_group)
        numeral_group.pack(side=tk.TOP, fill=tk.X)

        lbl_numeral = tk.Label(numeral_group, text="Численный столбец")
        lbl_numeral.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X)

        cb_numeral = ttk.Combobox(numeral_group, values=["Номер сотрудника","Телефон"])
        cb_numeral.pack(side=tk.RIGHT, padx=5, pady=5)
        cb_numeral.current(0)

        btn_start = ttk.Button(summary_table_group, text='Начать анализ', command=self.histogram_analyze)
        btn_start.pack(side=tk.TOP, padx=5, pady=5, fill=tk.X)
        #btn_start.bind('<Button-1>', lambda event: dialog2.view.records(dialog2.entry_quality1.get(),
        #                                                                     dialog2.entry_quality1.get(),
        #                                                                    dialog2.entry_numerical.get()))


        # Не даёт перейти в другое окно
        self.grab_set()
        self.focus_set()

    def histogram_analyze(self):
        pass

if __name__ == "__main__":
    pass

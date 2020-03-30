import tkinter as tk
from tkinter import ttk
import sqlite3


class Main(tk.Frame):

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):

        toolbar = tk.Frame(bd=70)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        btn_open_dialog = tk.Button(toolbar, text='Добавить строку', command=self.open_dialog,
                                    bg='#d7d8e0', bd=15, compound=tk.TOP)
        btn_open_dialog.pack(side=tk.LEFT)

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

        btn_clear = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_clear.place(x=30, y=350)

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

    root.title("POLUAKOV ZAEBAL")
    root.geometry("1000x600")
    root.resizable(False, False)
    root.mainloop()

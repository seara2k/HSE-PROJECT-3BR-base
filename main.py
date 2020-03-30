import tkinter as tk
from tkinter import ttk
import sqlite3


class Main(tk.Frame):

    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):

        toolbar = tk.Frame(bd=70)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        btn_open_dialog = tk.Button(toolbar, text='Добавить строку', command=self.open_dialog,
                                    bg='#d7d8e0', bd=15, compound=tk.TOP)
        btn_open_dialog.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=(
            'ID', 'Full Name', "Phone Number", "City"), height=100, show='headings')
        self.tree.column('ID', width=230, anchor=tk.CENTER)
        self.tree.column('Full Name', width=230, anchor=tk.CENTER)
        self.tree.column("Phone Number", width=230, anchor=tk.CENTER)
        self.tree.column("City", width=230, anchor=tk.CENTER)

        self.tree.heading('ID', text='Номер сотрудника')
        self.tree.heading('Full Name', text='ФИО')
        self.tree.heading("Phone Number", text="Номер телефона")
        self.tree.heading("City", text="Город")

        self.tree.pack()

    def open_dialog(self):
        Child()


class Child(tk.Toplevel):

    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title("Добавить строку")
        self.geometry('300x400')
        self.resizable(False, False)

        label_ID = tk.Label(self, text='ID')
        label_ID.place(x=30, y=50)

        label_Full_Name = tk.Label(self, text='Full Name')
        label_Full_Name.place(x=30, y=100)

        label_Phone_Number = tk.Label(self, text="Phone Number")
        label_Phone_Number.place(x=30, y=150)

        label_City = tk.Label(self, text="City")
        label_City.place(x=30, y=200)


        self.ID = ttk.Entry(self)
        self.ID.place(x=150, y=50)

        self.Full_Name = ttk.Entry(self)
        self.Full_Name.place(x=150, y=100)

        self.Phone_Number = ttk.Entry(self)
        self.Phone_Number.place(x=150, y=150)

        self.City = ttk.Entry(self)
        self.City.place(x=150, y=200)

		# добавить u
        #self.combobox = ttk.Combobox(self, values=["LOLO", "DADADA"])
        #self.combobox.current(0)
        #self.combobox.place(x=100, y=20)

        btn_clear = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_clear.place(x=300, y=80)

        btn_add = ttk.Button(self, text="Добавить")
        btn_add.place(x=330, y=50)
        btn_add.bind('<Button-1>')

        # Не даёт перейти в другое окно
        self.grab_set()
        self.focus_set()


class DB:

    def __init__(self):

        self.conn = sqlite3.connect("jostko.db")
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXIST jostko("ID" integer primary key,"Full Name" text,"Phone Number" text,"City" text)''')
        self.conn.commit()





if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("POLUAKOV ZAEBAL")
    root.geometry("1000x600")
    root.resizable(False, False)
    root.mainloop()

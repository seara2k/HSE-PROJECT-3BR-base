import tkinter as tk
from tkinter import ttk


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
            'Номер сотрудника', 'ФИО', "Номер телефона", "Город"), height=70, show='headings')

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
        # Не даёт перейти в другое окно
        self.grab_set()
        self.focus_set()


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("POLUAKOV XUESOS")
    root.geometry("1000x600")
    root.resizable(False, False)
    root.mainloop()

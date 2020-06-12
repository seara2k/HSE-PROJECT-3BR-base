import tkinter as tk
from tkinter import ttk
from . import child_add as child_add
from . import child_base_stats as child_base_stats
from . import child_summary_table as child_summary_table
from . import child_bar_chart as child_bar_chart
from . import child_histogram as child_histogram
from . import child_box_visk as child_box_visk
from . import child_dispersion as child_dispersion
from . import child_about_program as child_about_program


class main_gui:

    def change(self):
        child_add.child_add(self, "change")

    def open_add(self):
        child_add.child_add(self, "add")

    def open_base_stats_analysis(self):
        child_base_stats.child_base_stats(self)

    def open_summary_table_analysis(self):
        child_summary_table.child_summary_table(self)

    def open_bar_chart_analysis(self):
        child_bar_chart.child_bar_chart(self)

    def open_histogram_analysis(self):
        child_histogram.child_histogram(self)

    def open_box_visk_analysis(self):
        child_box_visk.child_box_visk(self)

    def open_dispersion_analysis(self):
        child_dispersion.child_dispersion(self)

    def open_about_program(self):
        child_about_program.child_about_program(self)

    def widgets(self):
        """
        Конструктор меню сверху слева главного окна
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """
        mainmenu = tk.Menu(self)

        filemenu = tk.Menu(mainmenu, tearoff=0)
        filemenu.add_command(label="Новый", command=self.new)
        filemenu.add_command(label="Открыть", command=self.open)
        filemenu.add_command(label="Сохранить", command=self.save)
        filemenu.add_command(label="Сохранить как",
                             command=self.save_to_pickle)
        filemenu.add_separator()
        filemenu.add_command(label="Импорт из excel",
                             command=self.import_from_excel)
        filemenu.add_command(label="Экспорт в excel",
                             command=self.export_to_excel)

        helpmenu = tk.Menu(mainmenu, tearoff=0)
        helpmenu.add_command(label="Помощь", command=self.get_help)
        helpmenu.add_command(label="О программе",
                             command=self.open_about_program)

        mainmenu.add_cascade(label="Файл", menu=filemenu)
        mainmenu.add_cascade(label="Справка", menu=helpmenu)
        self.config(menu=mainmenu)

    def init_GUI(self):
        """
        Конструктор интерфейса главного окна
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """
        # design and mats
        ttk.Style().configure("TNotebook.Tab", padding=('50', '5'))
        style = ttk.Style()
        style.layout("Tab",
                     [('Notebook.tab', {'sticky': 'nswe', 'children':
                                        [('Notebook.padding', {'side': 'top', 'sticky': 'nswe', 'children':
                                                               #[('Notebook.focus', {'side': 'top', 'sticky': 'nswe', 'children':
                                                               [('Notebook.label', {
                                                                 'side': 'top', 'sticky': ''})],
                                                               #})],
                                                               })],
                                        })]
                     )

        # Верхняя часть программы
        toolbar = tk.Frame(bd=10)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        # Фрейм добавки
        editing_group = tk.LabelFrame(toolbar, text='Таблица')
        editing_group.pack(side=tk.LEFT, padx=0, pady=0,
                           anchor=tk.N, fill=tk.Y)

        eg_btn_add = ttk.Button(
            editing_group, text='Добавить строку', width=30, command=self.open_add)
        eg_btn_add.pack(side=tk.TOP, padx=5, pady=5, fill=tk.X, expand=1)

        self.eg_btn_edit = ttk.Button(
            editing_group, text="Изменить", command=self.change)
        self.eg_btn_edit.pack(side=tk.LEFT, padx=5,
                              pady=5, fill=tk.X, expand=1)
        self.eg_btn_edit.config(state="disabled")

        eg_btn_delete = ttk.Button(
            editing_group, text="Удалить", command=self.delete)
        eg_btn_delete.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=1)

        # Фрейм анализов
        analysis_group = tk.LabelFrame(toolbar, text='Метод анализа')
        analysis_group.pack(side=tk.LEFT, padx=10, pady=0,
                            anchor=tk.N, fill=tk.Y)

        self.ag_cb_analys = ttk.Combobox(analysis_group,
                                         values=["Базовая статистика",
                                                 "Сводная таблица",
                                                 "Столбчатая диаграмма",
                                                 "Гистограмма",
                                                 "Диаграмма Бокса-Вискера",
                                                 "Диаграмма рассеивания"], width=25)
        self.ag_cb_analys.pack(side=tk.TOP, padx=5, pady=5)
        self.ag_cb_analys.current(0)

        ag_btn_choose = ttk.Button(
            analysis_group, text="Выбрать", command=self.choose_analysis_function)
        ag_btn_choose.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=1)

        # Фрейм фильтров
        filtr_group = tk.LabelFrame(toolbar, text='Фильтры')
        filtr_group.pack(side=tk.LEFT, padx=0, pady=0, anchor=tk.N, fill=tk.Y)

        self.fg_cb_filter = ttk.Combobox(filtr_group,
                                         values=["Номер сотрудника",
                                                 "ФИО",
                                                 "Номер телефона",
                                                 "Город"])
        self.fg_cb_filter.pack(side=tk.TOP, padx=5, pady=5)
        self.fg_cb_filter.configure(state="disabled")
        self.fg_cb_filter.current(0)

        self.fg_btn_filtr = ttk.Button(
            filtr_group, text="Рефреш таблицы", command=self.refresh_from_database)
        self.fg_btn_filtr.pack(side=tk.TOP, padx=5,
                               pady=5, fill=tk.X, expand=1)

        # Фрейм таблицы и табов
        bottom_frame = tk.Frame(bd=10)
        self.tab_parent = ttk.Notebook(bottom_frame)
        tab_all = ttk.Frame(self.tab_parent, padding=10)
        tab_1 = ttk.Frame(self.tab_parent, padding=10)
        tab_2 = ttk.Frame(self.tab_parent, padding=10)
        tab_3 = ttk.Frame(self.tab_parent, padding=10)
        self.tab_parent.add(tab_all, text="Полная таблица")
        self.tab_parent.add(tab_1, text="Сотрудник")
        self.tab_parent.add(tab_2, text="Часы")
        self.tab_parent.add(tab_3, text="Работы")
        self.tab_parent.pack()
        bottom_frame.pack()
        self.tab_parent.bind("<<NotebookTabChanged>>", self.deselect_rows)

        # Таблицы и скролл бары к ним
        self.tree_names = ["tree_all", "tree_1", "tree_2", "tree_3"]
        self.tree_all_columns = ["ID", "Full_Name", "City",
                                 "Phone_Number", "Speciality", "Time", "Pays_An_Hour"]
        self.tree_all = ttk.Treeview(
            tab_all, columns=self.tree_all_columns, height=20, show="headings")

        self.tree_all.column('ID', width=135, anchor=tk.CENTER)
        self.tree_all.column('Full_Name', width=135, anchor=tk.CENTER)
        self.tree_all.column('City', width=135, anchor=tk.CENTER)
        self.tree_all.column("Phone_Number", width=135, anchor=tk.CENTER)
        self.tree_all.column("Speciality", width=135, anchor=tk.CENTER)
        self.tree_all.column("Time", width=135, anchor=tk.CENTER)
        self.tree_all.column("Pays_An_Hour", width=135, anchor=tk.CENTER)

        self.tree_all.heading("ID", text="Номер сотрудника", command=lambda:
                              self.sort(self.tree_all, "ID", False, "tree_all"))
        self.tree_all.heading("Full_Name", text='ФИО', command=lambda:
                              self.sort(self.tree_all, "Full_Name", False, "tree_all"))
        self.tree_all.heading("City", text="Город", command=lambda:
                              self.sort(self.tree_all, "City", False, "tree_all"))
        self.tree_all.heading("Phone_Number", text="Номер телефона", command=lambda:
                              self.sort(self.tree_all, "Phone_Number", False, "tree_all"))
        self.tree_all.heading("Speciality", text="Специальность", command=lambda:
                              self.sort(self.tree_all, "Speciality", False, "tree_all"))
        self.tree_all.heading("Time", text="Часы", command=lambda:
                              self.sort(self.tree_all, "Time", False, "tree_all"))
        self.tree_all.heading("Pays_An_Hour", text="Зарплата в час", command=lambda:
                              self.sort(self.tree_all, "Pays_An_Hour", False, "tree_all"))

        tree_scrollbar_vertical_all = tk.Scrollbar(
            tab_all, orient="vertical", command=self.tree_all.yview)
        tree_scrollbar_vertical_all.pack(side="right", fill="y")
        tree_scrollbar_horizontal_all = tk.Scrollbar(
            tab_all, orient="horizontal", command=self.tree_all.xview)
        tree_scrollbar_horizontal_all.pack(side="bottom", fill="x")

        self.tree_all.pack()
        self.tree_all.bind("<<TreeviewSelect>>", self.edit_button_check)

        self.tree_1_columns = ['ID', 'Full_Name', "Phone_Number"]
        self.tree_1 = ttk.Treeview(
            tab_1, columns=self.tree_1_columns, height=20, show="headings")

        self.tree_1.column('ID', width=315, anchor=tk.CENTER)
        self.tree_1.column('Full_Name', width=315, anchor=tk.CENTER)
        self.tree_1.column("Phone_Number", width=315, anchor=tk.CENTER)

        self.tree_1.heading("ID", text="Номер сотрудника", command=lambda:
                            self.sort(self.tree_1, "ID", False, "tree_1"))
        self.tree_1.heading("Full_Name", text='ФИО', command=lambda:
                            self.sort(self.tree_1, "Full_Name", False, "tree_1"))
        self.tree_1.heading("Phone_Number", text="Номер телефона", command=lambda:
                            self.sort(self.tree_1, "Phone_Number", False, "tree_1"))

        tree_scrollbar_vertical_1 = tk.Scrollbar(
            tab_1, orient="vertical", command=self.tree_1.yview)
        tree_scrollbar_vertical_1.pack(side="right", fill="y")

        tree_scrollbar_horizontal_1 = tk.Scrollbar(
            tab_1, orient="horizontal", command=self.tree_1.xview)
        tree_scrollbar_horizontal_1.pack(side="bottom", fill="x")

        self.tree_1.pack()
        self.tree_1.bind("<<TreeviewSelect>>", self.edit_button_check)

        self.tree_2_columns = ["ID", "Speciality", "Time"]
        self.tree_2 = ttk.Treeview(
            tab_2, columns=self.tree_2_columns, height=20, show="headings")

        self.tree_2.column("ID", width=315, anchor=tk.CENTER)
        self.tree_2.column("Speciality", width=315, anchor=tk.CENTER)
        self.tree_2.column("Time", width=315, anchor=tk.CENTER)

        self.tree_2.heading("ID", text='Номер сотрудника', command=lambda:
                            self.sort(self.tree_2, "ID", False, "tree_2"))
        self.tree_2.heading("Speciality", text="Специальность", command=lambda:
                            self.sort(self.tree_2, "Speciality", False, "tree_2"))
        self.tree_2.heading("Time", text="Часы", command=lambda:
                            self.sort(self.tree_2, "Time", False, "tree_2"))

        tree_scrollbar_vertical_2 = tk.Scrollbar(
            tab_2, orient="vertical", command=self.tree_2.yview)
        tree_scrollbar_vertical_2.pack(side="right", fill="y")

        tree_scrollbar_horizontal_2 = tk.Scrollbar(
            tab_2, orient="horizontal", command=self.tree_2.xview)
        tree_scrollbar_horizontal_2.pack(side="bottom", fill="x")

        self.tree_2.pack()
        self.tree_2.bind("<<TreeviewSelect>>", self.edit_button_check)

        self.tree_3_columns = ["City", "Speciality", "Pays_An_Hour"]
        self.tree_3 = ttk.Treeview(
            tab_3, columns=self.tree_3_columns, height=20, show="headings")
        self.tree_3.column("City", width=315, anchor=tk.CENTER)
        self.tree_3.column("Speciality", width=315, anchor=tk.CENTER)
        self.tree_3.column("Pays_An_Hour", width=315, anchor=tk.CENTER)

        self.tree_3.heading("City", text="Город", command=lambda:
                            self.sort(self.tree_3, "City", False, "tree_3"))
        self.tree_3.heading("Speciality", text="Специальность", command=lambda:
                            self.sort(self.tree_3, "Speciality", False, "tree_3"))
        self.tree_3.heading("Pays_An_Hour", text="Зарплата в час", command=lambda:
                            self.sort(self.tree_3, "Pays_An_Hour", False, "tree_3"))

        tree_scrollbar_vertical_3 = tk.Scrollbar(
            tab_3, orient="vertical", command=self.tree_3.yview)
        tree_scrollbar_vertical_3.pack(side="right", fill="y")

        tree_scrollbar_horizontal_3 = tk.Scrollbar(
            tab_3, orient="horizontal", command=self.tree_3.xview)
        tree_scrollbar_horizontal_3.pack(side="bottom", fill="x")

        self.tree_3.pack()
        self.tree_3.bind("<<TreeviewSelect>>", self.edit_button_check)

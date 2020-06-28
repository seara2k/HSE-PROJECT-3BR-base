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
        """
        Вызывает окно изменения строки
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """
        child_add.child_add(self, "change")

    def open_add(self):
        """
        Вызывает окно добавления строки
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """
        child_add.child_add(self, "add")

    def open_base_stats_analysis(self):
        """
        Вызывает окно базовой статистики
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Чихватова А.А.
        """
        child_base_stats.child_base_stats(self)

    def open_summary_table_analysis(self):
        """
        Вызывает окно сводной таблицы
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Чихватова А.А.
        """
        child_summary_table.child_summary_table(self)

    def open_bar_chart_analysis(self):
        """
        Вызывает окно стобчатой диаграммы
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Чихватова А.А.
        """
        child_bar_chart.child_bar_chart(self)

    def open_histogram_analysis(self):
        """
        Вызывает окно гистограммы
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Чихватова А.А.
        """
        child_histogram.child_histogram(self)

    def open_box_visk_analysis(self):
        """
        Вызывает окно диаграммы Бокса-Вискера
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Чихватова А.А.
        """
        child_box_visk.child_box_visk(self)

    def open_dispersion_analysis(self):
        """
        Вызывает окно диаграммы рассеивания
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Чихватова А.А.
        """
        child_dispersion.child_dispersion(self)

    def open_about_program(self):
        """
        Вызывает окно "О программе"
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """
        child_about_program.child_about_program(self)

    def open_filter(self):
        """
        Вызывает окно выбора фильтров
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Литвинов В.С.
        """
        child_add.child_add(self, "filter")

    def widgets(self):
        """
        Конструктор меню сверху слева главного окна
        ----------
        Параметры: -
        ----------
        Возвращает: -
        ----------
        Автор: Чихватова А.А.
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
                             command=lambda: self.export_to_excel(False))

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
        Автор: Чихватова А.А.
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

        self.eg_btn_add = ttk.Button(
            editing_group, text='Добавить строку', width=30, command=self.open_add)
        self.eg_btn_add.pack(side=tk.TOP, padx=5, pady=5, fill=tk.X, expand=1)

        self.eg_btn_edit = ttk.Button(
            editing_group, text="Изменить", command=self.change)
        self.eg_btn_edit.pack(side=tk.LEFT, padx=5,
                              pady=5, fill=tk.X, expand=1)
        self.eg_btn_edit.config(state="disabled")

        self.eg_btn_delete = ttk.Button(
            editing_group, text="Удалить", command=self.delete)
        self.eg_btn_delete.pack(side=tk.LEFT, padx=5,
                                pady=5, fill=tk.X, expand=1)

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

        ag_btn_choose = ttk.Button(analysis_group, text="Выбрать", command=self.choose_analysis_function)
        ag_btn_choose.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=1)

        # Фрейм фильтров
        filtr_group = tk.LabelFrame(toolbar, text='Фильтры')
        filtr_group.pack(side=tk.LEFT, padx=0, pady=0, anchor=tk.N, fill=tk.Y)

        self.fg_btn_filtr = ttk.Button(
            filtr_group, text="Выбрать фильтрацию", command=self.open_filter)
        self.fg_btn_filtr.pack(side=tk.TOP, padx=5,
                               pady=5, fill=tk.X, expand=1)

        self.fg_btn_refresh = ttk.Button(
            filtr_group, text="Очистить фильтрацию", command=lambda: self.refresh_from_database(self.database))
        self.fg_btn_refresh.pack(side=tk.TOP, padx=5,
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
        self.tree_all_columns = ["id", "full_name", "city",
                                 "phone_number", "speciality", "time", "pays_an_hour"]
        self.tree_all = ttk.Treeview(
            tab_all, columns=self.tree_all_columns, height=20, show="headings")

        self.tree_all.column('id', width=135, anchor=tk.CENTER)
        self.tree_all.column('full_name', width=135, anchor=tk.CENTER)
        self.tree_all.column('city', width=135, anchor=tk.CENTER)
        self.tree_all.column("phone_number", width=135, anchor=tk.CENTER)
        self.tree_all.column("speciality", width=135, anchor=tk.CENTER)
        self.tree_all.column("time", width=135, anchor=tk.CENTER)
        self.tree_all.column("pays_an_hour", width=135, anchor=tk.CENTER)

        self.tree_all.heading("id", text="Номер сотрудника", command=lambda:
                              self.sort(self.tree_all, "id", False, "tree_all"))
        self.tree_all.heading("full_name", text='ФИО', command=lambda:
                              self.sort(self.tree_all, "full_name", False, "tree_all"))
        self.tree_all.heading("city", text="Город", command=lambda:
                              self.sort(self.tree_all, "city", False, "tree_all"))
        self.tree_all.heading("phone_number", text="Номер телефона", command=lambda:
                              self.sort(self.tree_all, "phone_number", False, "tree_all"))
        self.tree_all.heading("speciality", text="Специальность", command=lambda:
                              self.sort(self.tree_all, "speciality", False, "tree_all"))
        self.tree_all.heading("time", text="Часы", command=lambda:
                              self.sort(self.tree_all, "time", False, "tree_all"))
        self.tree_all.heading("pays_an_hour", text="Зарплата в час", command=lambda:
                              self.sort(self.tree_all, "pays_an_hour", False, "tree_all"))

        tree_scrollbar_vertical_all = tk.Scrollbar(
            tab_all, orient="vertical", command=self.tree_all.yview)
        tree_scrollbar_vertical_all.pack(side="right", fill="y")
        tree_scrollbar_horizontal_all = tk.Scrollbar(
            tab_all, orient="horizontal", command=self.tree_all.xview)
        tree_scrollbar_horizontal_all.pack(side="bottom", fill="x")

        self.tree_all.pack()

        self.tree_1_columns = ['id', 'full_name', "city", "phone_number"]
        self.tree_1 = ttk.Treeview(
            tab_1, columns=self.tree_1_columns, height=20, show="headings")

        self.tree_1.column('id', width=236, anchor=tk.CENTER)
        self.tree_1.column('full_name', width=236, anchor=tk.CENTER)
        self.tree_1.column("city", width=236, anchor=tk.CENTER)
        self.tree_1.column("phone_number", width=236, anchor=tk.CENTER)

        self.tree_1.heading("id", text="Номер сотрудника", command=lambda:
                            self.sort(self.tree_1, "id", False, "tree_1"))
        self.tree_1.heading("full_name", text='ФИО', command=lambda:
                            self.sort(self.tree_1, "full_name", False, "tree_1"))
        self.tree_1.heading("city", text="Город", command=lambda:
                            self.sort(self.tree_1, "city", False, "tree_1"))
        self.tree_1.heading("phone_number", text="Номер телефона", command=lambda:
                            self.sort(self.tree_1, "phone_number", False, "tree_1"))

        tree_scrollbar_vertical_1 = tk.Scrollbar(
            tab_1, orient="vertical", command=self.tree_1.yview)
        tree_scrollbar_vertical_1.pack(side="right", fill="y")

        tree_scrollbar_horizontal_1 = tk.Scrollbar(
            tab_1, orient="horizontal", command=self.tree_1.xview)
        tree_scrollbar_horizontal_1.pack(side="bottom", fill="x")

        self.tree_1.pack()
        self.tree_1.bind("<<TreeviewSelect>>", self.edit_button_check)

        self.tree_2_columns = ["id", "speciality", "time"]
        self.tree_2 = ttk.Treeview(
            tab_2, columns=self.tree_2_columns, height=20, show="headings")

        self.tree_2.column("id", width=315, anchor=tk.CENTER)
        self.tree_2.column("speciality", width=315, anchor=tk.CENTER)
        self.tree_2.column("time", width=315, anchor=tk.CENTER)

        self.tree_2.heading("id", text='Номер сотрудника', command=lambda:
                            self.sort(self.tree_2, "id", False, "tree_2"))
        self.tree_2.heading("speciality", text="Специальность", command=lambda:
                            self.sort(self.tree_2, "speciality", False, "tree_2"))
        self.tree_2.heading("time", text="Часы", command=lambda:
                            self.sort(self.tree_2, "time", False, "tree_2"))

        tree_scrollbar_vertical_2 = tk.Scrollbar(
            tab_2, orient="vertical", command=self.tree_2.yview)
        tree_scrollbar_vertical_2.pack(side="right", fill="y")

        tree_scrollbar_horizontal_2 = tk.Scrollbar(
            tab_2, orient="horizontal", command=self.tree_2.xview)
        tree_scrollbar_horizontal_2.pack(side="bottom", fill="x")

        self.tree_2.pack()
        self.tree_2.bind("<<TreeviewSelect>>", self.edit_button_check)

        self.tree_3_columns = ["city", "speciality", "pays_an_hour"]
        self.tree_3 = ttk.Treeview(
            tab_3, columns=self.tree_3_columns, height=20, show="headings")
        self.tree_3.column("city", width=315, anchor=tk.CENTER)
        self.tree_3.column("speciality", width=315, anchor=tk.CENTER)
        self.tree_3.column("pays_an_hour", width=315, anchor=tk.CENTER)

        self.tree_3.heading("city", text="Город", command=lambda:
                            self.sort(self.tree_3, "city", False, "tree_3"))
        self.tree_3.heading("speciality", text="Специальность", command=lambda:
                            self.sort(self.tree_3, "speciality", False, "tree_3"))
        self.tree_3.heading("pays_an_hour", text="Зарплата в час", command=lambda:
                            self.sort(self.tree_3, "pays_an_hour", False, "tree_3"))

        tree_scrollbar_vertical_3 = tk.Scrollbar(
            tab_3, orient="vertical", command=self.tree_3.yview)
        tree_scrollbar_vertical_3.pack(side="right", fill="y")

        tree_scrollbar_horizontal_3 = tk.Scrollbar(
            tab_3, orient="horizontal", command=self.tree_3.xview)
        tree_scrollbar_horizontal_3.pack(side="bottom", fill="x")

        self.tree_3.pack()
        self.tree_3.bind("<<TreeviewSelect>>", self.edit_button_check)
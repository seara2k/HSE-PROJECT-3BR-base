import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Сводная Таблица
def summary(df, attr1_name, attr2_name, num_name):
    """
    Создание датафрейма для сводной таблицы
    ----------
    Параметры:
        df - Исходный датафрейм
        attr1_name - название качественного столбца 1
        attr2_name - название качественного столбца 2
        num_name - название численного столбца
    ----------
    Возвращает: -
    ----------
    Автор: Чихватова. А.А.
    """
    return pd.pivot_table(df, index=attr1_name, columns=attr2_name,
                          values=num_name, aggfunc='mean')


# Столбчатая Диаграмма
def bar_chart(kach_st_1, kach_st_2, name1, name2):
    """
    Построение столбчатой диаграммы
    ----------
    Параметры:
            kach_st_1 - качественный столбец 1
            kach_st_2 - качетсвенный столбец 2
            name1 - название качественного столбца 1
            name2 - название качественного столбца 2
    ----------
    Возвращает: -
    ----------
    Автор: Чихватова А.А.
    """
    position = np.arange(len(kach_st_1))
    for i in range(len(kach_st_1)):
        kach_st_1[i] = kach_st_1[i].replace(' ', '\n')

    fig, ax = plt.subplots()
    ax.set_title(f' Столбчатая диаграмма зависимости {name2.lower()} от {name1.lower()}')
    ax.set_xlabel(name1)
    ax.set_ylabel(name2)
    ax.bar(position, kach_st_2,  color=np.random.rand(7, 3))

    ax.set_xticks(position)
    fig.savefig('Graphics/bar_chart.png')

    labels = ax.set_xticklabels(kach_st_1)

    fig.set_figwidth(10)
    fig.set_figheight(6)

    plt.show()


# Гистограмма
def histogram(kach, kol, name_kach, name_kol):
    """
    Построение столбчатой диаграммы
    ----------
    Параметры:
            kach - качественный столбец
            kol - количественный столбец
            name_kach - название качественного столбца
            name_kol - название количественного столбца
    ----------
    Возвращает: -
    ----------
    Автор: Чихватова А.А.
    """
    d = {'kol': kol, 'kach': kach}
    df = pd.DataFrame(d)
    df_agg = df.groupby(kach)
    vals = [df['kol'].values.tolist() for i, df in df_agg]
    plt.figure(figsize=(16, 9), dpi=80)
    colors = [plt.cm.Spectral(i/float(len(vals) + 1)) for i in range(len(vals))]
    if len(vals) != 0:
        n, bins, patches = plt.hist(vals, stacked=True, density=False, edgecolor='black', color=colors[:(len(vals))])
    else:
        n, bins, patches = plt.hist(vals, stacked=True, density=False, edgecolor='black')
    plt.legend({group: col for group, col in zip(np.unique(df['kach']).tolist(), colors[:len(vals)])})
    plt.title(f"Гистограмма распределения частоты {name_kach} по {name_kol}", fontsize=22)
    plt.xlabel(name_kol)
    plt.ylabel("Частота")
    plt.savefig('Graphics/histogram.png')
    plt.show()


# Диаграмма Бокса-Вискера
def box_plot(kach_st, kol_st, name1, name2):
    """
    Построение диаграммы Бокса-Вискера
    ----------
    Параметры:
            kach_st - качественный столбец
            kol_st - численный столбец
    ----------
    Возвращает: -
    ----------
    Автор: Чихватова А.А.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title(f'Диаграмма Бокса-Вискера зависимости {name2.lower()} от {name1.lower()}')
    ax.set_xlabel(name1)
    ax.set_ylabel(name2)
    ax.boxplot(kol_st,
               patch_artist=True,
               medianprops={'color': "#297083"},
               boxprops={'color': "#539caf", 'facecolor': "#539caf"},
               whiskerprops={'color': "#539caf"},
               capprops={'color': "#539caf"})
    ax.set_xticklabels(kach_st)
    fig.savefig('Graphics/boxplot.png')
    plt.show()


# Диаграмма Рассеивания
def scatter(kach_st, kol_st_1, kol_st_2, name1, name2, name3):
    """
    Построение диаграммы рассеяния
    ----------
    Параметры:
            kach_st - качественный столбец
            kol_st_1 - численный столбец 1
            kol_st_2 - численный столбец 2
            name1 - название качественного столбца
            name2 - название количественного столбца 1
            name3 - название количественного столбца 2
    ----------
    Возвращает: -
    ----------
    Автор: Чихватова А.А.
    """
    data = {'Name': kach_st,
            'Hours': kol_st_1,
            'Salary': kol_st_2}
    midwest = pd.DataFrame(data)

    categories = np.unique(midwest['Name'])
    colors = [plt.cm.Spectral(i / float(len(categories) + 1)) for i in range(len(categories))]
    plt.figure(figsize=(16, 10), dpi=80, facecolor='w', edgecolor='k')
    for i, Name in enumerate(categories):
        plt.scatter('Hours', 'Salary',
                    data=midwest.loc[midwest.Name == Name, :],
                    s=20, c=np.array([colors[i]]), label=str(Name))

    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.title(f' Рассеяние {name1.lower()} по {name2.lower()} и {name3.lower()}', fontsize=22)
    plt.xlabel(name2)
    plt.ylabel(name3)
    if len(categories) != 0:
        plt.legend(fontsize=12)
    plt.savefig('Graphics/scatter.png')
    plt.show()

def amount_of_elements(var):
    return len(var)


# Уникальных элементов
def unique_elements(var):
    return(len(set(var)))


# Самый частый элемент
def most_frequent(var):
    var_set = set(var)
    count = 0
    most_frequent_element = None
    for i in var_set:
        element = var.count(i)
        if element > count:
            count = element
            most_frequent_element = i
    return most_frequent_element


# Повторения самого частого элемента
def most_frequent_count(var):
    var_set = set(var)
    count = 0
    for i in var_set:
        element = var.count(i)
        if element > count:
            count = element
    return count


#  Среднее
def average(var):
    average = 0
    try:
        for i in var:
            average += i
        return average / len(var)
    except TypeError:
        return '-'


#  Среднеквадратическое отклонение
def standard_deviation(var):
    try:
        return np.std(var)
    except TypeError:
        return '-'


# Максимальный элемент
def maximum(var):
    try:
        maxi = float(var[0])
        for i in var:
            if i > maxi:
                maxi = i
        return maxi
    except ValueError:
        return '-'


# Минимальный элемент
def minimum(var):
    try:
        mini = float(var[0])
        for i in var:
            if i < mini:
                mini = i
        return mini
    except ValueError:
        return '-'








base_stats_rows = {"Количество элементов":amount_of_elements, "Уникальные элементы":unique_elements,
                   "Самый частый элемент":most_frequent, "Количество повторений":most_frequent_count,
                   "Среднее значение":average, "Среднеквадратическое отклонение":standard_deviation,
                   "Максимальный элемент":maximum, "Минимальный элемент":minimum}


print(base_stats_rows.items())
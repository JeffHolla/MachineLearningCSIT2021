import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as panda


# Task_1_22
# Задание 1.
def main():
    panda.set_option('display.max_rows', 50)
    panda.set_option('display.max_columns', None)

    df = panda.read_csv("googleplaystore - redacted.csv", delimiter=';')  # DataFrame

    print("Количество приложений: ", len(df))
    df.drop_duplicates(subset='App', inplace=True)
    df = df[df['Android Ver'] != np.nan]
    df = df[df['Android Ver'] != 'NaN']
    # print(df.dtypes)

    print("Количество приложений: ", len(df))
    # # print(df.sample(7))
    #

    # Подготовим и обработаем данные
    # Преобразуем все размеры приложений к Kb
    # Преобразуем все цены из $ в просто цифры
    # Уберём из колонки Installs знаки '+' и ',' для того, чтобы сделать тип исчисляемым
    # Удаляем из значений +
    df['Installs'] = df['Installs'].apply(lambda x: x.replace('+', '') if '+' in str(x) else x)
    # Удаляем из значений ,
    df['Installs'] = df['Installs'].apply(lambda x: x.replace(',', '') if ',' in str(x) else x)
    # Приводим к типу int
    df['Installs'] = df['Installs'].apply(lambda x: int(x))

    # Преобразуем в Kb
    # Если размер варьируется от устройства к устройству, то ставим NaN
    df['Size'] = df['Size'].apply(
        lambda x: str(x).replace('Varies with device', 'NaN') if 'Varies with device' in str(x) else x)
    df['Size'] = df['Size'].apply(lambda x: str(x).replace('M', '') if 'M' in str(x) else x)
    df['Size'] = df['Size'].apply(lambda x: str(x).replace(',', '') if 'M' in str(x) else x)
    df['Size'] = df['Size'].apply(lambda x: float(str(x).replace('k', '')) / 1000 if 'k' in str(x) else x)

    # Преобразуем в тип float
    df['Size'] = df['Size'].apply(lambda x: float(x))
    df['Installs'] = df['Installs'].apply(lambda x: float(x))
    df['Reviews'] = df['Reviews'].apply(lambda x: int(x))

    # Убираем знак доллара из колонки Price
    df['Price'] = df['Price'].apply(lambda x: str(x).replace('$', '') if '$' in str(x) else str(x))
    df['Price'] = df['Price'].apply(lambda x: float(x))
    # print(df.sample(70)["Installs"])

    # print(df.dtypes)

    # Task 2
    # Посчитать статистические показатели:
    # медиана,
    # мода,
    # средняя,
    # минимум,
    # максимум.

    test = panda.read_csv("test.csv", delimiter=';')  # DataFrame
    # print(test)
    print()

    # # Median
    # # Среднее значение из всех значений
    # print("Median: ")
    # print(df.median())
    # print()
    #
    # # Mode
    # # Мода — значение во множестве наблюдений, которое всртречается наиболее часто.
    # print("Mode: ")
    # print(df.mode(numeric_only=True))
    # print()
    #
    # # Average (mean)
    # # Среднее арифметическое
    # print("Average(mean): ")
    # print(df.mean())
    # print()
    #
    # # Min
    # # Минимальное значение
    # print("Min: ")
    # print(df.min(numeric_only=True))
    # print()
    #
    # # Max
    # # Максимальное значение
    # print("Max: ")
    # print(df.max(numeric_only=True))

    # Task 3
    # Создать новый столбец, в котором разместить
    # разницу между максимумом и текущим значением для некоторого числового параметра.
    # Создадим колонку с названием Task_3, в которую положим результат задания.
    # df["Task_3"] = df['Rating'].max() - df['Rating']
    # print("Готовые данные")
    # print(df['Task_3'].head(n=15))
    # print("Изначальные данные")
    # print(df['Rating'].head(n=15))
    # print("Максимум из изначальных данных: ", df['Rating'].max())

    # Task 4
    # Разбить данные на несколько блоков
    # (не менее 3, приблизительно равных по размеру) по некоторому критерию (критерий определить самостоятельно).
    stars_1 = df.loc[df["Rating"] < 2]
    # stars_2 = df.query("Rating >= 2 and Rating < 3")  # Альт способ выбирать данные
    stars_2 = df.loc[df["Rating"] >= 2].loc[df["Rating"] < 3]
    stars_3 = df.loc[df["Rating"] >= 3].loc[df["Rating"] < 4]
    stars_4 = df.loc[df["Rating"] >= 4].loc[df["Rating"] < 5]
    stars_5 = df.loc[df["Rating"] == 5]

    # print(sorted(stars_4["Rating"].unique()))
    # print(stars_2)

    # Task 5
    # Привести круговую диаграмму для проделанного разбиения.
    labels = ["Одна звезда", "Две звезды", "Три звезды", "Четыре звезды", "Пять звезды"]
    values = [len(stars_1) / len(df) * 100,
              len(stars_2) / len(df) * 100,
              len(stars_3) / len(df) * 100,
              len(stars_4) / len(df) * 100,
              len(stars_5) / len(df) * 100]

    # fig, ax = plt.subplots()
    # ax.pie(values, labels=labels, autopct='%1.1f%%', shadow=True)
    # ax.axis("equal")  # Соотношение длины и ширины одинаковые
    # ax.legend(loc='upper left', bbox_to_anchor=(0.87, 0.18))  # Легенда диаграммы
    #
    # plt.show()

    # Task 6
    # В зависимости от особенностей набора данных для каждого блока
    # построить график (гистограмму, ...).
    # # stars_1
    # values = stars_1["Category"].value_counts().to_dict()
    # two_dicts = divideDictValuesBy2(values)
    # hbarplot(two_dicts[0].keys(), two_dicts[0].values(), y_label="Категория", x_label="Количество приложений",
    #         title="Rating 2>x>=1 - Part 1")
    # hbarplot(two_dicts[1].keys(), two_dicts[1].values(), y_label="Категория", x_label="Количество приложений",
    #         title="Rating 2>x>=1 - Part 2")

    # # stars_2
    # values = stars_2["Category"].value_counts().to_dict()
    # two_dicts = divideDictValuesBy2(values)
    # hbarplot(two_dicts[0].keys(), two_dicts[0].values(), y_label="Категория", x_label="Количество приложений",
    #         title="Rating 3>x>=2 - Part 1")
    # hbarplot(two_dicts[1].keys(), two_dicts[1].values(), y_label="Категория", x_label="Количество приложений",
    #         title="Rating 3>x>=2 - Part 2")

    # # stars_3
    # values = stars_3["Category"].value_counts().to_dict()
    # two_dicts = divideDictValuesBy2(values)
    # hbarplot(two_dicts[0].keys(), two_dicts[0].values(), y_label="Категория", x_label="Количество приложений",
    #         title="Rating 4>x>=3 - Part 1")
    # hbarplot(two_dicts[1].keys(), two_dicts[1].values(), y_label="Категория", x_label="Количество приложений",
    #         title="Rating 4>x>=3 - Part 2")
    #
    # # stars_4
    # values = stars_4["Category"].value_counts().to_dict()
    # two_dicts = divideDictValuesBy2(values)
    # hbarplot(two_dicts[0].keys(), two_dicts[0].values(), y_label="Категория", x_label="Количество приложений",
    #         title="Rating 5>x>=4 - Part 1")
    # hbarplot(two_dicts[1].keys(), two_dicts[1].values(), y_label="Категория", x_label="Количество приложений",
    #         title="Rating 5>x>=4 - Part 2")
    #
    # # stars_5
    # values = stars_5["Category"].value_counts().to_dict()
    # two_dicts = divideDictValuesBy2(values)
    # hbarplot(two_dicts[0].keys(), two_dicts[0].values(), y_label="Категория", x_label="Количество приложений",
    #         title="Rating 5 - Part 1")
    # hbarplot(two_dicts[1].keys(), two_dicts[1].values(), y_label="Категория", x_label="Количество приложений",
    #         title="Rating 5 - Part 2")

    #plt.show()


    # Task 7.
    # Сгруппировать данные (GroupBy) по некоторому признаку и сохранить результаты в новые таблицы.
    # Для каждой новой таблицы провести сортировку по сложному ключу, состоящему из
    # нескольких признаков. Для каждой таблицы своя сортировка.

    # Сгруппируем по жанру Education
    educationGenre = df.groupby('Genres').get_group('Education')
    # print(educationGenre)

    # Сгруппируем по жанру Puzzle
    puzzleGenre = df.groupby('Genres').get_group('Puzzle')
    # print(puzzleGenre)

    # # Отсортируем жанр education по сложному ключу
    # educationGenreSort = educationGenre.sort_values(by=['Rating', 'Size', 'Genres'])
    # print(educationGenreSort)
    #
    # # Отсортируем жанр puzzle по сложному ключу
    # puzzleGenreSort = puzzleGenre.sort_values(by=['Installs', 'Rating', 'Reviews'])
    # print(puzzleGenreSort)


    # Task 7.
    # Для вариантов № 1, 2, 4, 13, 20, 22, 23: отобразить распределение некоторого
    # параметра по дням недели (в каждой группе), по месяцам (суммарно).
    # Параметр - количество вышедших приложений определённого жанра в день

    panda.options.mode.chained_assignment = None  # Для отключения предупреждения о работе с копией

    puzzleGenre["Release"] = panda.to_datetime(puzzleGenre["Release"])
    # print(puzzleGenre["Release"])

    days_1 = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    puzzleGenre['DayOfWeek'] = puzzleGenre["Release"].dt.weekday.apply(lambda x: x+1)
    puzzleGenre['DayOfWeekName'] = puzzleGenre["Release"].dt.weekday.apply(lambda x: x+1).apply(lambda x: days_1[x])
    print(puzzleGenre)
    print(puzzleGenre.dtypes)

    days_dict = {}
    for item in sorted(puzzleGenre['DayOfWeek'].unique()):
        # print(item)
        day_name = item
        # print(puzzleGenre.query("DayOfWeek == @day_name"))
        # days_dict[days_1[item]] = puzzleGenre.query("DayOfWeek == @day_name")["DayOfWeek"].value_counts()
        # days_dict = puzzleGenre.query("DayOfWeek == @day_name")["DayOfWeekName"].value_counts().to_dict()
        days_dict[days_1[item]] = puzzleGenre.query("DayOfWeek == @day_name")["DayOfWeekName"].value_counts().item()
    #    print(days_dict)



    # print(dict_tmp)
    # alt_dict = {'Monday': 19, 'Tuesday': 17, 'Wednesday': 11, 'Thursday': 29, 'Friday': 19, 'Saturday': 11, 'Sunday': 13}
    # s = panda.Series(dict_tmp)
    # print("Dict = ", s)
    # s.plot(figsize=(15, 5))
    #
    # plt.show()

    puzzleGenre['Month'] = puzzleGenre["Release"].dt.month
    print(puzzleGenre['Month'])
    months = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август', 9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
    month_dict = {}
    for item in sorted(puzzleGenre['Month'].unique()):
        # print(item)
        month = item
        # print(puzzleGenre.query("Month == @month"))
        month_dict[months[item]] = sum(puzzleGenre.query("Month == @month")["Release"].value_counts())
        print(month_dict)

    print(month_dict)
    month_plot = panda.Series(month_dict)
    print("Dict = ", month_plot)
    month_plot.plot(figsize=(15, 5))

    plt.show()


    # Способ python
    # print(test.mean()["Температура"])
    # count_ = 0
    # for item in test["Температура"]:
    #     if item - test.mean()["Температура"] > 10:
    #         count_ += 1
    #
    # print("Процент равен :", count_ / 100 * 10)\

    # Способ pandas
    # aver_temp = test.mean()["Температура"]  # Переменная для средней температуры
    # # print("Test = ", test.query("Температура - @aver_temp > 10"))
    # print("Процент равен :",
    #       test.query("Температура - @aver_temp > 10")["Город"].count() / 100 * test["Температура"].count())


# def barplot(x_data, y_data, y_label='', x_label='', title=''):
#     _, ax_ = plt.subplots()
#     ax_.barh(x_data, y_data, color="blue", align="edge")
#     ax_.set_ylabel(x_label)
#     ax_.set_xlabel(y_label)
#     ax_.set_title(title)
#     # _.set_figwidth(18)

def hbarplot(x_data, y_data, y_label="Категория", x_label='', title=''):
    fig, ax = plt.subplots(figsize=(15, 5))
    y_pos = np.arange(len(x_data))
    tick_label_ = np.arange(len(x_data))
    ax.barh(y_pos, y_data, align='center', tick_label=tick_label_)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(x_data)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)

    for i, v in enumerate(y_data):
        plt.text(v, i, " "+str(v), color='blue', va='center', fontweight='bold')


def divideDictValuesBy2(values):
    first_half_dict = {}
    second_half_dict = {}
    counter = 0
    for items in values.items():
        if counter % 2 == 0:
            first_half_dict[items[0]] = items[1]
            # print('0 : ', first_half_dict)
        else:
            second_half_dict[items[0]] = items[1]
            # print('1 : ', second_half_dict)
        counter += 1

    list_of_two_dict = [first_half_dict, second_half_dict]

    return list_of_two_dict


if __name__ == "__main__":
    main()

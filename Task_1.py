import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as panda


# 1. Общая статистика (количество, минимальный, максимальный, среднее, медиана, мода, среднеквадратическое отклонение).
# 2. Статистика количества сдававших и оценок по видам школ (СОШ, гимназия, лицей и т.д.), гистограмма.
# 3. Статистика количества сдававших и оценок по районам, гистограмма.
# 4. 10 лучших школ (не учитывать школы, из которых участвовало менее 10 учеников).
# 5. 10 худших школ.
# 6. Проверка гипотезы: зависимость результатов от удалённости от областного центра.
# 7.* Проверка гипотезы: зависимость результатов от размера населённого пункта, в котором расположено образовательное учреждение (по численности населения).
# В качестве ответа отправьте ссылку на ноутбук (предварительно открыв доступ) или сам ноутбук — файл с расширением ipynb.

# Задание 1.
def main():
    panda.set_option('display.max_rows', 50)
    panda.set_option('display.max_columns', None)

    df = panda.read_csv("OGE_2019_Results_And_Analize.csv", delimiter=';')  # DataFrame

    print(df.dtypes)

    # print(df)
    print()

    # Task 1:
    # Общая статистика:

    # # Количество
    # print("Общее количество записей: ", len(df))
    # print()
    #
    # # Минимальное значение
    # print("Min: ")
    # print(df["Первичный балл"].min())
    # print()
    #
    # # Max
    # # Максимальное значение
    # print("Max: ")
    # print(df["Первичный балл"].max())
    # print()
    #
    # # Average (mean)
    # # Среднее арифметическое
    # print("Average(mean): ")
    # print(df["Первичный балл"].mean())
    # print()
    #
    # # Среднее значение из всех значений
    # print("Median: ")
    # print(df["Первичный балл"].median())
    # print()
    #
    # # Mode
    # # Мода — значение во множестве наблюдений, которое всртречается наиболее часто.
    # print("Mode: ")
    # print(df["Первичный балл"].mode())
    # print()
    #
    # # Среднеквадратическое отклонение
    # print("Среднеквадратическое отклонение: ")
    # print(df["Первичный балл"].std())
    # print()

    # 2. Статистика количества сдававших и оценок по видам школ (СОШ, гимназия, лицей и т.д.), гистограмма.
    # labels = ["Одна звезда", "Две звезды", "Три звезды", "Четыре звезды", "Пять звезды"]
    # values = [len(stars_1) / len(df) * 100,
    #           len(stars_2) / len(df) * 100,
    #           len(stars_3) / len(df) * 100,
    #           len(stars_4) / len(df) * 100,
    #           len(stars_5) / len(df) * 100]

    labels = [*df["Вид ОО"].unique()]

    passed = df.loc[df["Оцека по 5"] >= 3]
    notPassed = df.loc[df["Оцека по 5"] < 3]

    print(passed["Вид ОО"].unique())
    # print(passed[df["Вид ОО"] == "Лицей"])
    # print(notPassed)

    print(len(passed.loc[passed["Вид ОО"] == "Лицей"]))
    print(len(passed.loc[passed["Вид ОО"] == "Вечерняя (сменная) общеобразовательная школа"]))
    print(len(passed.loc[passed["Вид ОО"] == "Кадетская школа-интернат"]))

    index = ['СОШ', 'Гимназия', 'Лицей', 'ООШ', 'Лицей-интернат', 'СОШи', 'СОШ с углуб.',
             'Вечерняя ОШ', 'Кадетская школа-интернат']
    values = [len(passed.loc[passed["Вид ОО"] == _iter]) for _iter in passed["Вид ОО"].unique()]

    plt.title('Количество сдавших по отношению к ОО (оценки 3, 4, 5)')
    plt.bar(index, values)

    for x, y in zip(index, values):
        plt.text(x, y + 0.05, '%d' % y, ha='center', va='bottom')

    plt.show()

    # fig, ax = plt.subplots()
    # ax.pie(values, labels=labels, autopct='%1.1f%%', shadow=True)
    # ax.axis("equal")  # Соотношение длины и ширины одинаковые
    # ax.legend(loc='upper left', bbox_to_anchor=(0.87, 0.18))  # Легенда диаграммы
    #
    plt.show()


if __name__ == "__main__":
    main()

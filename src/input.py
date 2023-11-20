import csv
import locale
import enum

import sys, getopt

locale.setlocale(locale.LC_ALL, '')


class TableIndices(enum.IntEnum):
    headers = 0
    data = 1
    labels = 2


def load_single_arg_deps(path: str):
    """Возвращает таблицу функций одной переменной в следующем формате:

    Первый индекс - столбец

    Второй индекс - часть столбца (см. TableIndices)

    Третий - элементы столбца
    """
    with open(path, encoding="utf-8-sig") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        headers = next(csv_reader)
        labels = next(csv_reader)
        table = list(zip(headers, map(lambda column: list(map(locale.atof, column)), zip(*csv_reader)), labels))
        return table


def input_parameters():
    argumentList = sys.argv[1:]
    # Options
    options = "x:y:t:"

    # Long options
    long_options = ["2D", "title="]

    x_label = ""
    y_label = ""
    title = ""
    is_2d = False
    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)

        # checking each argument
        for currentArgument, currentValue in arguments:

            if currentArgument == "-x":
                x_label = currentValue

            elif currentArgument == "-y":
                y_label = currentValue

            elif currentArgument in ("-t", "--title"):
                title = currentValue

            elif currentArgument == "--2D":
                is_2d = True

        return x_label, y_label, title, is_2d

    except getopt.error as err:
        # output error, and return with an error code
        print(str(err))




import csv
import locale
import enum

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

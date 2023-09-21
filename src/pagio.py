import csv
import locale

locale.setlocale(locale.LC_ALL, '')


def load(path: str) -> list[tuple[str, list[float]]]:
    """Возвращает таблицу в следующем формате:

    Первый индекс - столбец

    Второй индекс - 0 для заголовка столбца, 1 для данных

    Третий - элементы столбца
    """
    with open(path, encoding="utf-8-sig") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        header = next(csv_reader)
        table = list(zip(header, map(lambda column: list(map(locale.atof, column)), zip(*csv_reader))))
        return table

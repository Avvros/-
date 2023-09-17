import locale
import csv

locale.setlocale(locale.LC_ALL, '')

def load(path: str):
    with open(path, encoding="utf-8-sig") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        header = next(csv_reader)
        table = list(zip(header, map(lambda column: list(map(locale.atof, column)), zip(*csv_reader))))
        return table
        # print(" | ".join(header))
        # for row in csv_reader:
        #     try:
        #         print(*map(locale.atof, row))
        #     except ValueError as ve:
        #         print(ve)


print(load("st_atm.csv"))
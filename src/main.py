import numpy as np
import locale
import csv
import enum
import approx

locale.setlocale(locale.LC_ALL, '')


class StandardAtmosphereParameters(enum.Enum):
    geom_height = 0
    geop_height = 1
    temperature_K = 2
    temperature_C = 3
    pressure_Pa = 4
    pressure_mmHg = 5
    density = 6
    gravity_acceleration = 7


def load(path: str):
    with open(path, encoding="utf-8-sig") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        header = next(csv_reader)
        table = list(zip(header, map(lambda column: list(map(locale.atof, column)), zip(*csv_reader))))
        return table


st_atm = load("st_atm.csv")
base_index = StandardAtmosphereParameters.geom_height.value
with np.printoptions(precision=5, suppress=True):
    print(approx.polyfill(st_atm[base_index][1], st_atm[StandardAtmosphereParameters.density.value][1], 2))
#print(st_atm[base_index][1])
#print(st_atm[StandardAtmosphereParameters.density.value][1])

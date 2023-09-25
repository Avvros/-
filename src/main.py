import matplotlib.pyplot as plt
import numpy as np
import enum
import approx
from pagio import *
from itertools import takewhile

# Размеры сетки графиков
dim_x = 2
dim_y = 2


# Описание содержания параметров стандартной атмосферы
class StandardAtmosphereParameters(enum.IntEnum):
    geom_height = 0
    geop_height = 1
    temperature_K = 2
    temperature_C = 3
    pressure_Pa = 4
    pressure_mmHg = 5
    density = 6
    gravity_acceleration = 7


SAP = StandardAtmosphereParameters


# Загрузка таблицы параметров стандартной атмосферы
st_atm = load_single_arg_deps("st_atm.csv")

# Аргумент функций - геометрическая высота (столбец 0)
argument_index = 0

# A
st_atm_iter = iter(st_atm)
next(st_atm_iter)
height_funcs = [approx.polyfill(st_atm[argument_index][TableIndices.data], column[TableIndices.data], 2) for column in st_atm_iter]
# print(height_funcs)

# Верхняя граница высоты при построении графиков
top = 10001

# Набор высот для точек графика
x = np.linspace(0, top, 100)

# Создание окна с графиками в виде сетки dim_x на dim_y размера 10 на 10
# получение контейнера графиков (Figure) и представлений каждого графика (Axes)
fig, axs = plt.subplots(dim_x, dim_y, figsize=(10, 10))
for i, val in enumerate([SAP.gravity_acceleration, SAP.density, SAP.pressure_Pa, SAP.temperature_K]):
    ax = axs[i // dim_x, i % dim_x]
    ax.plot(x, approx.polyval(height_funcs[val - 1], x))
    ax.set_xlabel(st_atm[argument_index][TableIndices.labels])
    ax.set_ylabel(st_atm[val][TableIndices.labels])  # Add a y-label to the axes.
    ax.set_title(st_atm[val][TableIndices.headers])  # Add a title to the axes.
    ax.set_xticks(np.arange(0, top, 1000))
    plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
    ax.grid()

[fig.delaxes(ax) for ax in axs.flatten() if not ax.has_data()]

plt.tight_layout()
plt.show()

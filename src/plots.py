import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
import approx


def draw_plot(func, x_label, y_label, title):
    # Верхняя граница высоты при построении графиков
    top = 10001
    # Набор высот для точек графика
    x = np.linspace(0, top, 100)
    # Создание окна с графиками в виде сетки dim_x на dim_y размера 10 на 10
    # получение контейнера графиков (Figure) и представлений каждого графика (Axes)
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.plot(x, approx.polyval(func, x))
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)  # Add a y-label to the axes.
    ax.set_title(title)  # Add a title to the axes.
    #ax.set_xticks(np.arange(0, top, 1000))
    plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
    ax.grid()
    plt.tight_layout()
    plt.show()

def draw_arrow(ax, sp, ep, label):
    arr = mpatches.FancyArrowPatch(sp, ep, arrowstyle='->,head_width=.15', mutation_scale=20)
    ax.add_patch(arr)
    ax.annotate(label, (.5, .5), xycoords=arr, ha='center', va='bottom')

def draw_time_matrix(sv, sH, dV, dH, vm, hm, vhm):
    divisor = 1000
    sv /= divisor
    sH /= divisor
    dV /= divisor
    dH /= divisor
    fig, ax = plt.subplots()
    for i in range(len(vm)):
        for j in range(len(vm[i])):
            draw_arrow(ax, (sv + dV * j, sH + dH * i), (sv + dV * (j + 1), sH + dH * i), vm[i][j])
    #draw_arrow(ax, (1.25, 1.5), (1.75, 1.5))
    #ax.set(xlim=(1, 2), ylim=(1, 2))
    plt.show()

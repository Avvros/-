import numpy as np
from matplotlib import pyplot as plt
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
    ax.set_xticks(np.arange(0, top, 1000))
    plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
    ax.grid()
    plt.tight_layout()
    plt.show()

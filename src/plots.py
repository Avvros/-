import numpy as np

from pagio import TableIndices
import matplotlib as plt
import approx


def draw_plots(funcs: tuple[str, list[float], str], x, dim_x, dim_y):
    pass

# def draw_plot(poly, x):
#     #x = np.linspace(0, table[xi][TableIndices.data.value][-1], 100)
#
#     # Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
#     fig, ax = plt.subplots(dimX, dimY)
#     ax.plot(x, approx.polyval(poly, x))  # Plot some data on the axes.
#     # ax.plot(x, x, label='linear')
#     ax.set_xlabel(table[base_index][labels_position])  # Add an x-label to the axes.
#     ax.set_ylabel(table[StandardAtmParamsIdx.density.value][labels_position])  # Add a y-label to the axes.
#     ax.set_title(table[StandardAtmParamsIdx.density.value][headers_position])  # Add a title to the axes.
#     # ax.legend()  # Add a legend.
#     plt.grid()
#     plt.show()
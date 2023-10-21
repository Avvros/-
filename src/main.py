from approx import polyfill
from locale import atof
from input import input_parameters
from plots import draw_plot
import numpy as np

x_label, y_label, title = input_parameters()
x_data = list(map(atof, input().split()))
y_data = list(map(atof, input().split()))

func = polyfill(x_data, y_data, 2)

with np.printoptions(precision=6, suppress=True):
    print(func)

draw_plot(func, x_label, y_label, title)
import matplotlib.pyplot as plt
import numpy as np
import enum
import approx
import pagio


class StandardAtmParamsIdx(enum.Enum):
    geom_height = 0
    geop_height = 1
    temperature_K = 2
    temperature_C = 3
    pressure_Pa = 4
    pressure_mmHg = 5
    density = 6
    gravity_acceleration = 7


st_atm = pagio.load("st_atm.csv")
print(st_atm)
base_index = StandardAtmParamsIdx.geom_height.value
density_data = st_atm[StandardAtmParamsIdx.density.value]
density_poly = approx.polyfill(st_atm[base_index][1], density_data[1], 2)
with np.printoptions(precision=5, suppress=True):
    print(density_poly)
    print(approx.polyfill(st_atm[base_index][1], st_atm[StandardAtmParamsIdx.gravity_acceleration.value][1], 2))
    print(approx.polyfill(st_atm[base_index][1], st_atm[StandardAtmParamsIdx.pressure_Pa.value][1], 2))

x = np.linspace(0, st_atm[base_index][1][-1], 100)  # Sample data.
#x = np.linspace(0, 2, 100)

# Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
fig, ax = plt.subplots()
ax.plot(x, approx.polyval(density_poly, x), label='Density')  # Plot some data on the axes.
#ax.plot(x, x, label='linear')
ax.set_xlabel('Геометрическая высота h, м')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Density")  # Add a title to the axes.
#ax.legend()  # Add a legend.
plt.grid()
plt.show()




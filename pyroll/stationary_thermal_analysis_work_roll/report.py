import numpy as np
import matplotlib.pyplot as plt

from pyroll.report import hookimpl
from pyroll.core import Unit
from pyroll.core import RollPass



from .stationary_heat_analysis import StationaryHeatAnalysis

@hookimpl(specname="unit_plot")
def roll_temperature_field_plot(unit: Unit):
    if isinstance(unit, RollPass):
        fig: plt.Figure = plt.figure()
        ax: plt.Axes = fig.subplots(subplot_kw={"projection": "polar"})

        ax.set_theta_zero_location("S")
        ax.set_theta_direction(1)

        heat_analysis = StationaryHeatAnalysis(unit.roll)
        polar_angles = heat_analysis.polar_angles


        for i, radius in enumerate(heat_analysis.normed_radial_coordinates):
            angles = np.array(list(polar_angles))
            temp = np.array(list(unit.roll.temperature_field[i, :]), dtype=np.float64)

            ax.plot(angles, temp, label=f"Radius:{radius * unit.roll.min_radius}")

        angle = np.deg2rad(67.5)

        ax.legend(
            loc="lower left", bbox_to_anchor=(0.5 + np.cos(angle) / 2, 0.5 + np.sin(angle) / 2)
        )

        return fig
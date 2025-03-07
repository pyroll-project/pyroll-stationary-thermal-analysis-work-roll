from typing import List

from pyroll.core import Roll
from pyroll.core.hooks import Hook

Roll.peclet_number = Hook[float]()
"""Peclet number of the roll."""

Roll.cooling_sections = Hook[List[List[float, float]]]()
"""Cooling sections of the roll."""

Roll.coolant_heat_transfer_coefficient = Hook[float]()
"""Heat Transfer coefficient of the coolant."""

Roll.free_surface_heat_transfer_coefficient = Hook[float]()
"""Heat Transfer coefficient of the coolant."""

@Roll.peclet_number
def peclet_number(self: Roll):
    return (self.rotational_frequency * self.min_radius ** 2) / self.heat_transfer_coefficient


@Roll.coolant_heat_transfer_coefficient
def default_water(self: Roll):
    return 15000


@Roll.free_surface_heat_transfer_coefficient
def default_air(self: Roll):
    return 15
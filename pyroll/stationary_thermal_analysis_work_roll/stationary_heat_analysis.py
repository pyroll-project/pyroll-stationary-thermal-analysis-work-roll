from typing import List

import numpy as np
import mpmath as mp
import pyroll.core as pr

from scipy.interpolate import interp1d

mp.mp.dps = 50

class StationaryHeatAnalysis:
    def __init__(self, roll: pr.RollPass.Roll):
        self.roll = roll
        self.roll_pass = self.roll.roll_pass
        self.number_of_number_of_fourier_terms = 141
        self.angular_discretization = 360
        self.radial_discretization = 2
        self.reference_temperature = 1 + 273.15
        self.polar_angles = mp.linspace(0, 2 * np.pi, self.angular_discretization, endpoint=True)
        self.fourier_orders = mp.linspace((-self.number_of_number_of_fourier_terms + 1) / 2,
                                          (self.number_of_number_of_fourier_terms + 1) / 2,
                                          self.number_of_number_of_fourier_terms,
                                          endpoint=False)
        self.radial_coordinates = mp.linspace(0.998 * self.roll.min_radius, self.roll.min_radius, self.radial_discretization)
        self.normed_radial_coordinates = [radial_coordinate / self.roll.min_radius for radial_coordinate in self.radial_coordinates]
        self.normed_cooling_array = mp.zeros(self.angular_discretization, 1)
        self.normed_heating_array = mp.zeros(self.angular_discretization, 1)


    def create_diagonal_matrix(self):
        pass

    def create_hermitian_matrix(self):
        pass

    def complex_fourier_analysis(self):
        pass

    def temperature_fourier_analysis(self):
        pass

    def set_normed_cooling_values(self, angle: float):

        for cooling_section_angles in self.roll.cooling_sections:
            self.normed_cooling_array[cooling_section_angles[0] : cooling_section_angles[1]] = self.roll.min_radius * self.roll.coolant_heat_transfer_coefficient / self.roll.thermal_conductivity

        for i in range(self.normed_cooling_array.rows):
            if self.normed_cooling_array[i] == 0:
                self.normed_cooling_array[i] = self.roll.free_surface_heat_transfer_coefficient





    def set_normed_heating_values(self, angle: float):





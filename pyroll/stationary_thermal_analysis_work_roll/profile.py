from pyroll.core import RollPass, Hook


RollPass.heat_flux = Hook[float]
"""Heat Flux inside the RollPass from Profile to the Roll."""

@RollPass.Profile.heat_flux
def heat_flux(self: RollPass):
    mean_temperature = (self.in_profile.temperature + self.out_profile.temperature) / 2

    return self.roll.contact_heat_transfer_coefficient * (mean_temperature - self.roll.temperature) * self.duration


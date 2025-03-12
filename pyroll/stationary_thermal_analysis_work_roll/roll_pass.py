from pyroll.core import SymmetricRollPass, Hook, root_hooks


SymmetricRollPass.heat_flux = Hook[float]()
"""Heat Flux inside the RollPass from Profile to the Roll."""

@SymmetricRollPass.heat_flux
def heat_flux(self: SymmetricRollPass):
    mean_temperature = (self.in_profile.temperature + self.out_profile.temperature) / 2

    return self.roll.heat_transfer_coefficient * (mean_temperature - self.roll.temperature)


root_hooks.append(SymmetricRollPass.heat_flux)

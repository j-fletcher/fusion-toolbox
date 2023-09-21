import ChargedParticle
import Field
import scipy.constants as constants
import numpy as np

initialPosition = [0, 0, 0]
initialVelocity = [0, 0, 0]
charge = constants.elementary_charge
mass = constants.proton_mass

Bx, By, Bz = np.meshgrid(np.linspace(0, 1, num=10), np.linspace(1, 2, num=10), np.linspace(2, 3, num=10))

particle = ChargedParticle(initialPosition, initialVelocity, charge, mass)

ti, tf, dt = 0, 10, 1
r = []

while ti <= tf:
    particle.updateVelocity(dt, field)
    particle.updatePosition()
    r.append(particle.getPosition) # could be replaced by a plot...
    ti += dt
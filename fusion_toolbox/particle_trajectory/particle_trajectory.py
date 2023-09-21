import ChargedParticle
import Field
import scipy.constants as constants
import numpy as np

initialPosition = [0, 0, 0]
initialVelocity = [0, 0, 0]
charge = constants.elementary_charge
mass = constants.proton_mass

x=np.linspace(0,1,10)
y=np.linspace(1,2,10)
z=np.linspace(2,3,10)
Bx, By, Bz = np.meshgrid(x, y, z)
Bfield=Field(x,y,z,Bx,By,Bz)

particle = ChargedParticle(initialPosition, initialVelocity, charge, mass)

ti, tf, dt = 0, 10, 1
r = []

while ti <= tf:
    particle.updateVelocity(dt, Bfield.interpolateField(particle.getPosition()))
    particle.updatePosition()
    r.append(particle.getPosition) # could be replaced by a plot...
    ti += dt
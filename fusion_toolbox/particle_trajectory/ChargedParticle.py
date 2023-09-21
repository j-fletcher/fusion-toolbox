import numpy as np

from scipy.integrate import quad
from scipy.interpolate import LinearNDInterpolator

class ChargedParticle():
    def __init__(self, initialPosition, initialVelocity, charge, mass):
        self.position = {
            'x': initialPosition[0],
            'y': initialPosition[1],
            'z': initialPosition[2]
        }
        self.velocity = {
            'x': initialVelocity[0],
            'x': initialVelocity[1],
            'x': initialVelocity[2]
        }
        self.qm = charge/mass
        
    def updatePosition(self, dt):
        self.position['x'] += dt * self.velocity.x
        self.position['y'] += dt * self.velocity.y
        self.position['z'] += dt * self.velocity.z

    def updateVelocity(self, dt, field):
        
        # interpolate B field at particle position
        Bx, By, Bz = self.interpolateBField(field)

        self.velocity['x'] = quad(self.qm * (self.velocity.y*Bz - self.velocity.z*By, 0, dt))
        self.velocity['y'] = quad(self.qm * (self.velocity.z*Bx - self.velocity.x*Bz, 0, dt))
        self.velocity['z'] = quad(self.qm * (self.velocity.x*By - self.velocity.y*Bx, 0, dt))

    def getPosition(self):
        return self.position
    
    def getVelocity(self):
        return self.velocity

    def interpolateBField(field):
        
        rx, ry, rz = np.meshgrid(field.x, field.y, field.z)
        r = np.column_stack((rx.flatten(), ry.flatten(), rz.flatten()))

        field = np.random.rand(10, 10, 10)
        B = np.meshgrid(field.Bx, field.By, field.Bz)
        smoothB = 

        return interpolatedBx, interpolatedBy, interpolatedBz
        
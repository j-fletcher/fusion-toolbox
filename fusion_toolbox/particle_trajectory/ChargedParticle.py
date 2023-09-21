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
            'y': initialVelocity[1],
            'z': initialVelocity[2]
        }
        self.qm = charge/mass
        
    def updatePosition(self, dt):
        self.position['x'] += dt * self.velocity['x']
        self.position['y'] += dt * self.velocity['y']
        self.position['z'] += dt * self.velocity['z']

    def updateVelocity(self, dt, field):
        
        # interpolate B field at particle position
        Bx, By, Bz = self.interpolateBField(field)

        self.velocity['x'] = quad(self.qm * (self.velocity.y*Bz - self.velocity.z*By, 0, dt))
        self.velocity['y'] = quad(self.qm * (self.velocity.z*Bx - self.velocity.x*Bz, 0, dt))
        self.velocity['z'] = quad(self.qm * (self.velocity.x*By - self.velocity.y*Bx, 0, dt))

    def getPosition(self):
        return np.array([self.position['x'], self.position['y'], self.position['z']])
    
    def getVelocity(self):
        return np.array([self.velocity['x'], self.velocity['y'], self.velocity['z']])
        
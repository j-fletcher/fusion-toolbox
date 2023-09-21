from scipy.integrate import quad

class ChargedParticle():
    def __init__(self, initialPosition, initialVelocity, charge, mass):
        self.position = {
            'x': initialPosition[0],
            'y': initialPosition[1],
            'z': initialPosition[2]
        }
        self.velocity = {
            'vx': initialVelocity[0],
            'vx': initialVelocity[1],
            'vx': initialVelocity[2]
        }
        self.qm = charge/mass
        
    def updatePosition(self, dt):
        self.position['x'] += dt * self.velocity.x
        self.position['y'] += dt * self.velocity.y
        self.position['z'] += dt * self.velocity.z

    def updateVelocity(self, dt, field):
        self.velocity['x'] = quad(self.qm * (self.velocity.y*self.field.Bz - self.velocity.z*self.field.By, 0, dt)
        self.velocity['y'] = quad(self.qm * (self.velocity.z*self.field.Bx - self.velocity.x*self.field.Bz, 0, dt) 
        self.velocity['z'] = quad(self.qm * (self.velocity.x*self.field.By - self.velocity.y*self.field.Bx, 0, dt) 
    
    def getPosition(self):
        return self.position
    
    def getVelocity(self):
        return self.velocity
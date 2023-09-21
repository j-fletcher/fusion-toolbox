import numpy as np
from scipy.interpolate import RegularGridInterpolator

class Field:
    def __init__(self, x, y, z, fx, fy, fz):
        '''
        Field object that packages spatial grid and vector field together
        x: x linspace
        y: y linspace
        z: z linspace
        fx: x component of field over the grid
        fy: y component of field over the grid
        fz: z component of field over the grid
        '''
        self.x = x
        self.y = y
        self.z = z
        self.fx = fx
        self.fy = fy
        self.fz = fz

    def interpolateField(self, p):
        '''
        Return interpolated field vector at a point, p
        field: 3D vector field to interpolate 
        p: point in (x,y,z) space to interpolate to
        returns: field(p)
        '''
        mg = np.meshgrid(self.x, self.y, self.z, indexing='ij')
        fx_interp = RegularGridInterpolator((self.x, self.y, self.z), self.fx)
        fy_interp = RegularGridInterpolator((self.x, self.y, self.z), self.fy)
        fz_interp = RegularGridInterpolator((self.x, self.y, self.z), self.fz)

        return fx_interp(p), fy_interp(p), fz_interp(p)
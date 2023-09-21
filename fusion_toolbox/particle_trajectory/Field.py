import numpy as np


class Field:
    def __init__(self, x, y, z, fx, fy, fz):
        '''
        Field object that packages spatial grid and vector field together
        x: x meshgrid
        y: y meshgrid
        z: z meshgrid
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
        fx_interp = LinearNDInterpolator([], F)

        return interpolatedFx, interpolatedFy, interpolatedFz
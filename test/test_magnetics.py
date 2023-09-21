import numpy as np
import numpy.testing as npt
from math import pi

def generate_pf_coil_xyz(R, N = 100, z = 0): 
    thetas =  np.linspace(0, 2*pi, N)
    xyz = np.zeros((N,3))
    xyz[:,0] = R * np.cos(thetas)
    xyz[:,1] = R * np.sin(thetas)
    xyz[:,2] = z
    return xyz

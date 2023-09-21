import numpy as np
import scipy.constants as constants
import numpy.testing as npt
import pytest
@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0, 0], [4, 0, 0], 1], [4, 0, 0]),
        ([[0, 0, 0], [0, 4, 0], 1], [0, 4, 0]),
        ([[0, 0, 0], [0, 0, 4], 1], [0, 0, 4]),
    ]
)
def test_updatePosition(test, expected):
    """Tests that the position is updated correctly based on the particle velocity"""
    from fusion_toolbox.particle_trajectory.ChargedParticle import ChargedParticle
    particle = ChargedParticle(initialPosition=test[0], initialVelocity=test[1], charge=constants.elementary_charge, mass=constants.proton_mass)
    particle.updatePosition(test[2])
    npt.assert_array_equal(particle.getPosition(), np.array(expected))


@pytest.mark.parametrize(
    "test, expected",
    [
        ([0.5, 0, 0],[3, 0, 0]),
        ([.5,.5,.5],[4.5,0,0])
    ]
)
def test_fieldInterpolation(test, expected):
    '''Tests the field interpolation routine'''
    import fusion_toolbox.particle_trajectory.Field as F
    x=np.linspace(0,1,2)
    y=np.linspace(0,1,2)
    z=np.linspace(0,1,2)
    Bx=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
    By=np.zeros((2,2,2))
    Bz=np.zeros((2,2,2))
    B = F.Field(x, y, z, Bx, By, Bz)
    interpB = B.interpolateField(test)
    npt.assert_equal(interpB, expected)
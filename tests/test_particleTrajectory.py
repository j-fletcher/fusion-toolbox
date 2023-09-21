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

from dataclasses import dataclass
from typing import Union, Callable


def from_h5(filename, mat_names: list = None):
    pass


def make_dict():
    pass


def make_openmc_material():
    pass


@dataclass
class Material:
    name: str
    composition: str
    density: Union[float, Callable]
    thermal_conductivity: Union[float, Callable] = None
    thermal_expansion_coefficient: Union[float, Callable] = None
    melting_temperature: float = None
    yield_strength: float = None

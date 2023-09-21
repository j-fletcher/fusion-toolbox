from dataclasses import dataclass
from typing import Union, Callable
from dataserve import DataContainer


def make_openmc_material():
    pass


@dataclass
class Material:
    """Material object that has all the material properties wanted
    """
    name: str
    composition: str
    density: Union[float, Callable]
    thermal_conductivity: Union[float, Callable] = None
    thermal_expansion_coefficient: Union[float, Callable] = None
    melting_temperature: float = None
    yield_strength: float = None

    def save_to(self, filename: str):
        """Add the material to the material_database file

        Args:
            filename (str): name of the material_database file
        """

        try:
            dc = DataContainer(load_fn=filename)
        except FileNotFoundError:
            dc = DataContainer()
            dc.trials = []

        dc.trials.append(self)
        dc.save('material_database.pkl')

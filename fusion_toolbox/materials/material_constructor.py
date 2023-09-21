from dataclasses import dataclass, fields
from typing import Union, Callable
from dataserve import DataContainer
from QueryAPI import WolframAPI


_material_to_wolfram = {
    'density': 'density',
    'thermal_capacity': 'specific heat',
    'thermal_conductivity': 'thermal conductivity',
    'thermal_expansion_coefficient': 'coefficienty of thermal expansion',
    'melting_temperature': 'melting temperature',
}


@dataclass
class Material:
    """Material object that has all the material properties wanted
    """
    name: str
    composition: str
    density: Union[float, Callable] = None
    thermal_capacity: Union[float, Callable] = None
    thermal_conductivity: Union[float, Callable] = None
    thermal_expansion_coefficient: Union[float, Callable] = None
    melting_temperature: float = None

    def save_to(self, filename: str = "material_database.pkl"):
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
        dc.save(filename)

    def find_property(self, key, wolfram_name=None):

        api = WolframAPI(key)

        for el in self.__dict__.keys():
            if self.__dict__[el] is None:
                ans = float(
                    api.query(self.name, _material_to_wolfram[el]).split()[0])
                self.__setattr__(el, ans)

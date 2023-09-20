from abc import ABC, abstractclassmethod

class Material(ABC):

    def __init__(self):
        pass


    @property
    def composition(self):
        pass

    @property
    def density(self):
        pass

    @property
    def thermal_expansion_coefficient(self):
        pass

    @property
    def melting_temperature(self):
        pass

    @property
    def thermal_conductivity(self):
        pass

    @property
    def yield_strenght(self):
        pass
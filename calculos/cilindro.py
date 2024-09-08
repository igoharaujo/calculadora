import math
from interfaces.formas import VolumeInterface

class VolumeCilindro(VolumeInterface):
    def __init__(self, raio: float, altura: float) -> None:
        self.raio = raio
        self.altura = altura

    def volume(self) -> float:
        return math.pi * (self.raio ** 2) * self.altura

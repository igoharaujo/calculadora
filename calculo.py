from typing import Type
from interfaces.formas import FormasInterface, VolumeInterface

class Calculadora:
    def __init__(self) -> None:
        pass

    def medir_margem(self, forma: Type[FormasInterface]) -> float:
        return forma.margem()

    def medir_area(self, forma: Type[FormasInterface]) -> float:
        return forma.area()

    def medir_volume(self, forma: Type[VolumeInterface]) -> float:
        return forma.volume()

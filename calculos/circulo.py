import math
from interfaces.formas import FormasInterface

class AreaCirculo(FormasInterface):
    def __init__(self, raio: float) -> None:
        self.raio = raio

    def margem(self) -> float:
        return 2 * math.pi * self.raio
    
    def area(self) -> float:
        return math.pi * math.pow(self.raio, 2)

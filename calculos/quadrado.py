import math
from interfaces.formas import FormasInterface

class AreaQuadrado(FormasInterface):
    def __init__(self, lado: float) -> None:
        self.lado = lado

    def margem(self) -> float:
        return self.lado * 4
    
    def area(self) -> float:
        return math.pow(self.lado, 2)

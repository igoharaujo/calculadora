import math
from interfaces.formas import FormasInterface

class AreaRetangulo(FormasInterface):
    def __init__(self, largura: float, comprimento: float) -> None:
        self.largura = largura
        self.comprimento = comprimento

    def margem(self) -> float:
        return 2 * (self.largura + self.comprimento)
    
    def area(self) -> float:
        return self.largura * self.comprimento

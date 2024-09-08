from interfaces.formas import VolumeInterface

class VolumeParalelepipedo(VolumeInterface):
    def __init__(self, comprimento: float, largura: float, altura: float) -> None:
        self.comprimento = comprimento
        self.largura = largura
        self.altura = altura

    def volume(self) -> float:
        return self.comprimento * self.largura * self.altura

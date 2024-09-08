from interfaces.formas import VolumeInterface

class VolumeCubo(VolumeInterface):
    def __init__(self, lado: float) -> None:
        self.lado = lado

    def volume(self) -> float:
        return self.lado ** 3

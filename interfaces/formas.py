from abc import ABC, abstractmethod

class FormasInterface(ABC):
    @abstractmethod
    def margem(self) -> float:
        pass

    @abstractmethod
    def area(self) -> float:
        pass

class VolumeInterface(ABC):
    @abstractmethod
    def volume(self) -> float:
        pass

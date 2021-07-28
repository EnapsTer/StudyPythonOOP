from abc import ABC, abstractmethod


class AMateria(ABC):

    def __init__(self, materia_type: str):
        self._type = materia_type

    @abstractmethod
    def materia_type(self):
        return self._type

    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def use(self, target):
        pass

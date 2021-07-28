from abc import ABC, abstractmethod
from AMateria import AMateria


class ICharacter(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def equip(self, materia: AMateria):
        pass

    @abstractmethod
    def unequip(self, index: int):
        pass

    @abstractmethod
    def use(self, index: int, target):
        pass

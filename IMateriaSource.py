from AMateria import AMateria
from abc import ABC, abstractmethod


class IMateriaSource(ABC):

    @abstractmethod
    def learn_materia(self, materia: AMateria):
        pass

    @abstractmethod
    def create_materia(self, type_: str):
        pass

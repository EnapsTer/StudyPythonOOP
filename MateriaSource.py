from AMateria import AMateria
from IMateriaSource import IMateriaSource
from copy import deepcopy


class MateriaSource(IMateriaSource):

    _materias_count = 4

    def __init__(self):
       self._materias = dict()

    def learn_materia(self, materia: AMateria):
        if len(self._materias) <= MateriaSource._materias_count:
            self._materias[materia.materia_type] = materia

    def create_materia(self, type_: str):
        return deepcopy(self._materias.get(type_))

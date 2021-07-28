from AMateria import AMateria
from ICharacter import ICharacter


class Ice(AMateria):

    def __init__(self):
        super().__init__('ice')

    @property
    def materia_type(self):
        return self._type

    def clone(self):
        return Ice()

    def use(self, character: ICharacter):
        print(f"* shoots an ice bolt at {character.name} *")

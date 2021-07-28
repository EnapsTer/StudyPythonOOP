from AMateria import AMateria
from ICharacter import ICharacter


class Cure(AMateria):

    def __init__(self):
        super().__init__('cure')

    @property
    def materia_type(self):
        return self._type

    def clone(self):
        return Cure()

    def use(self, character: ICharacter):
        print(f"* heals {character.name}'s wounds *")

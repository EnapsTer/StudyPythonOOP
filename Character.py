from ICharacter import ICharacter
from AMateria import AMateria


class Character(ICharacter):

    _inventory_size = 4

    def __init__(self, name: str):
        self._name = name
        self._inventory = [None for _ in range(Character._inventory_size)]

    @property
    def name(self) -> str:
        return self._name

    def equip(self, materia: AMateria) -> None:
        for index, item in enumerate(self._inventory):
            if not item:
                self._inventory[index] = materia
                break
        else:
            print('Full inventory')

    @classmethod
    def check_inventory_index(cls, index: int):
        if index < 0 or index > cls._inventory_size:
            raise ValueError

    def unequip(self, index: int):
        Character.check_inventory_index(index)

        self._inventory[index] = None

    def use(self, index: int, target) -> None:
        Character.check_inventory_index(index)

        if self._inventory[index]:
            self._inventory[index].use(target)

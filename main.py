from MateriaSource import MateriaSource
from Character import Character
from Ice import Ice
from Cure import Cure


def main():
    source = MateriaSource()
    source.learn_materia(Ice())
    source.learn_materia(Cure())
    character = Character('Stas')
    character.equip(source.create_materia('ice'))
    character.equip(source.create_materia('cure'))
    bob = Character('bob')
    character.use(0, bob)
    character.use(1, bob)


if __name__ == '__main__':
    main()

from antagonistfinder import Place
from abc import ABC


class SuperHero(ABC):

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = Place()

    def find(self, place):
        self.finder.get_antagonist(place)

    def attack(self):
        Weapons.fire_a_gun(self)


class News(ABC):

    def create_news(self,place):
        self.name = 'name'
        place_name = getattr(place, 'name', 'place')
        print(f'{self.name} saved the {place_name}!')


class Weapons():
    def fire_a_gun(self):
        print('PIU PIU')

    def incinerate_with_lasers(self):
        print('Wzzzuuuup!')

    def roundhouse_kick(self):
        print('Bump')

    def ultimate(self):
        if self.name == 'Clark Kent':
            self.incinerate_with_lasers()


class Superman(SuperHero):

    def __init__(self):
        super(Superman, self).__init__('Superman', True)

    def attack(self):
        Weapons.roundhouse_kick(self)

    def ultimate(self):
        if self.name == 'Superman':
            Weapons.incinerate_with_lasers(self)



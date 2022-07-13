from places import Kostroma, Tokyo
from abc import ABC, abstractmethod


class AntagonistFinder(ABC):
    @abstractmethod
    def get_antagonist(self, place):
        if isinstance(place):
            place.get_enomy
        elif isinstance(place):
            place.get_enomy


class Place(AntagonistFinder):
    def get_antagonist(self, place):
        if isinstance(place, Kostroma):
            place.get_orcs()

    def get_antagonist(self, place):
        if isinstance(place, Tokyo):
            place.get_godzilla()

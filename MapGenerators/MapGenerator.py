from abc import ABC, abstractmethod
from MapGenerators.Map import Map


# Map gen class
class MapGenerator(ABC):

    # Returns a Map object
    @abstractmethod
    def generate(self):
        return Map()

from os import name
from aquarium_package.models import AlgueORM


class Herbivore:
    
    name: str
    pv: int

    def eat(self, algue: AlgueORM):
        """
        Args:
            algue (AlgueORM): seaweed will be eaten
        """
        self.pv += 3
        algue.pv -= 2
        print(f"{self.name} a mangé {algue.name}")
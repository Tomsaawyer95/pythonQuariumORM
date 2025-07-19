from aquarium_package.models import FishORM

class Carnivore():
    """
    Carnivore
    """
    name: str
    pv: int
    def eat(self, fish : FishORM):
        """
        Args:
            fish (FIshORM): fish will be eaten
        """
        self.pv += 5
        fish.pv -= 4
        print(f"{self.name} a mangé {fish.name}")
        
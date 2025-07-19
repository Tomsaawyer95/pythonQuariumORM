from aquarium_package.models import FishORM

class Carnivore():
    
    def manger(self, fish : FishORM):
        self.pv += 5
        fish.pv -= 4
        print(f"{self.name} a mangé {fish.name}")
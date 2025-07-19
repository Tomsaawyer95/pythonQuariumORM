from aquarium_package.models import AlgueORM

class Herbivore():

    def manger(self, algue : AlgueORM):
        self.pv += 3
        algue.pv -= 2
        print(f"{self.name} a mangé {algue.name}")



from aquarium_package.models import fish, FishParentORM
from aquarium_package.utils import Session

def creer_lien(child,parent1,parent2,session):
    lien = FishParentORM(child,parent1,parent2)
    session.add(lien)

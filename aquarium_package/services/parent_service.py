from aquarium_package.models import fish, parent
from aquarium_package.utils import Session

def creer_lien(child,parent1,parent2,session):
    lien = parent(child,parent1,parent2,session)
    session.add(lien)

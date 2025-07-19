import random

from aquarium_package.models import Type, Sexe, FishORM
from aquarium_package.models.fishs import Carpe,Thon,PoissonClown,Sole,Merou,Bar

def create_fish_type(
                        type_fish : Type = None,
                        sexe : Sexe | None = None,
                        age : int = 0,
                        pv : int = 10,
                        name : str | None = None,
                        fish_aquarium_id : int | None = None,
                        id : int | None = None,
                        is_alive : bool = True):
    
    """permet de creer un type de poisson a partir des informations
    
    Args:
        type_fish (Type): Type de poisson.
        sexe (Sexe, optional): Sexe du poisson. Par défaut None.
        age (int, optional): Âge du poisson. Par défaut 0.
        pv (int, optional): Points de vie restants du poisson. Par défaut 20.
        name (str, optional): Nom du poisson à créer. Par défaut une chaîne vide.
        aquarium_id (int,optional) : donne l'aquarium auquel le poisson est assigné

    Raises:
        ValueError: erreur renvoyer si le type de poisson n'est pas dans la liste

    Returns:
        list[Fish]: Liste de poissons (instances de Carpe, Thon, etc.)
    """
    if type_fish is None:
        type_fish = random.choice(list(Type))

    match(type_fish):
        case Type.CARPE:
            return Carpe(id = id,sexe = sexe,age = age, pv = pv, name=name,fish_aquarium_id=fish_aquarium_id)
        case Type.THON:
            return Thon(id = id,sexe = sexe,age = age, pv = pv, name=name,fish_aquarium_id=fish_aquarium_id)
        case Type.POISSON_CLOWN:
            return PoissonClown(id = id,sexe = sexe,age = age, pv = pv, name=name,fish_aquarium_id=fish_aquarium_id)
        case Type.BAR:
            return Bar(id = id,sexe = sexe,age = age, pv = pv, name=name,fish_aquarium_id=fish_aquarium_id)
        case Type.SOLE:
            return Sole(id = id,sexe = sexe,age = age, pv = pv, name=name,fish_aquarium_id=fish_aquarium_id)
        case Type.MEROU:
            return Merou(id = id,sexe = sexe,age = age, pv = pv, name=name,fish_aquarium_id=fish_aquarium_id)
        case _:
            raise ValueError(f"Type de poisson inconnu : {type_fish}")


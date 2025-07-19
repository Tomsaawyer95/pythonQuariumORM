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
        type_fish (Type : Enum): Type of fish from Enum Type
        sexe (Sexe, optional): Sexe of fish from Enum Sexe. Defaults to None.
        age (int, optional): Age of fish. Defaults to 0.
        pv (int, optional): PV of fish. Defaults to 10.
        name (str, optional): Name of fish . Defaults to None
        aquarium_id (int,optional) : give the assignation of aquarium to the fish. Defaults to None.

    Raises:
        ValueError: return error if type_fish isn't in the Enum Type of fish

    Returns:
        Fish : instance of under-class fish:
            - Carpe
            - Thon
            - PoissonClown
            - Sole
            - Merou
            - PoissonClown
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


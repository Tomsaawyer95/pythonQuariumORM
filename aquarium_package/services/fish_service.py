import random

from aquarium_package.ecosystem.aquarium import Aquarium
from aquarium_package.models import FishORM, AlgueORM, FishParentORM
from aquarium_package.models.behaviors import Herbivore, Carnivore
from aquarium_package.factories import create_fish_type


def handle_fishs_eating(
        fish: FishORM,
        alive_fishs: list[FishORM],
        alive_algues: list[AlgueORM]
):
    if isinstance(fish, Herbivore) and alive_algues:
        proie = random.choice(alive_algues)
    elif isinstance(fish, Carnivore):
        proie = random.choice(alive_fishs)
    else:
        proie = None

    if proie and proie.is_alive and type(proie) != type(fish):  # type: ignore
        fish.eat(proie)
        if proie.pv <= 0:
            proie.isDead()
    else:
        if proie:
            print(f"{fish.name} a essayer de manger a {proie.name} mais a échoué")
            pass
        else:
            print(f"{fish.name} n'a rien trouvé a manger")
            pass


def handle_fishs_reproduction(
        aquarium: Aquarium, fish: FishORM, alive_fishs: list[FishORM]
):
    proie = random.choice(alive_fishs)
    if not (fish is proie) and proie.is_alive and type(proie) == type(fish):  # type: ignore

        # Definir une chance de reussite :
        if fish.reproduce(proie) and random.random() > 0.90:
            new_fish = create_fish_type(
                type_fish=fish.type_fish_enum, fish_aquarium_id=aquarium.id
            )
            aquarium.management_session.add_to_session(new_fish)
            aquarium.management_session.flush_to_session(new_fish)
            aquarium.management_session.add_to_session(
                FishParentORM(new_fish, fish, proie)
            )
            print(
                f"{fish.name} s'est reproduit avec {proie.name} et a donnée {new_fish.name}"
            )
            aquarium.add_fish(new_fish)

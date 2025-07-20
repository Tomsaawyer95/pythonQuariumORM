import random
import math


import typer
from dotenv import load_dotenv

from aquarium_package.utils.psql_data_manager_orm import Base, engine

from aquarium_package.models.behaviors import (
    Herbivore,
    Carnivore,
    HermaphroditeAgeMixin,
    HermaphroditeOpportunisteMixin,
)
from aquarium_package.models import FishParentORM
from aquarium_package.factories import create_fish_type

# from aquarium_package.utils import json_data_manager
from aquarium_package.ecosystem import Aquarium
from aquarium_package.services import load_aquarium, save_aquarium_to_db,handle_fishs_eating, handle_fishs_reproduction


Base.metadata.create_all(engine, checkfirst=True)

MENU = """
choix 1 : telecharger un aquarium
choix 2 : creer un nouvelle aquarium
"""

MENU_AQUARIUM_OK = """
choix 1 : ajouter un poisson
choix 2 : ajouter une algue
choix 3 : passer un tour
choix 4 : sauvegarder l'aquarium
choix 5 : Quitter
"""
ERREUR = "Le choix entrée n'est pas dans la liste"


def print_form(s, v=15):
    print(f"\n{'-'* v} {s} {'-'* v}")


def do_step(aquarium: Aquarium):
    """
    Performs a simulation step for the given aquarium.
    This function advances the state of the aquarium by:
    1. Aging all alive algae and handling their duplication.
    2. Aging all alive fish.
    3. Shuffling the list of alive fish to randomize interactions.
    4. For each alive fish:
        - If its health points (pv) are between 1 and 5, it attempts to eat.
        - If the fish is alive, it attempts to reproduce.
    Args:
        aquarium (Aquarium): The aquarium instance to update.
    Returns:
        None
    """
    for algue in aquarium.get_alive_algues():
        algue.viellir()
        aquarium.handle_algue_duplication(algue)

    for fish in aquarium.get_alive_fishs():
        fish.viellir()

    alive_fishs = aquarium.get_alive_fishs()
    random.shuffle(alive_fishs)
    alive_algues = aquarium.get_alive_algues()

    for fish in alive_fishs:
        if 0 < fish.pv <= 5:
            handle_fishs_eating(fish,alive_fishs,alive_algues)
        elif fish.is_alive:
            handle_fishs_reproduction(aquarium,fish, alive_fishs)
            

if __name__ == "__main__":
    load_dotenv()

    print_form("Debut du traitement")

    current_aquarium = Aquarium(-1)

    def main():
        while True:
            print_form("Menu principal")
            print(MENU)
            choix = typer.prompt("Votre choix")
            match choix:
                case "1":
                    print_form("choix 1")
                    choix_aquarium = typer.prompt("veuillez choisir un numéro aquarium")
                    # try:
                    current_aquarium = load_aquarium(int(choix_aquarium))
                    break
                    # except ValueError:
                    #    print("La valeur choisie n'est pas correcte")
                case "2":
                    print_form("choix 2")

        while True:
            print(MENU_AQUARIUM_OK)
            choix = typer.prompt("Votre choix")
            match choix:
                case "1":
                    print_form("choix 2")
                    current_aquarium.add_fish()
                case "2":
                    print_form("choix 3")
                    current_aquarium.add_algue()
                case "3":
                    do_step(current_aquarium)
                case "4":
                    print_form("choix 4")
                    saved = typer.confirm("Voulez vous enregistrer")
                    if saved and current_aquarium.id != -1:
                        # current_aquarium.save_to_json()
                        save_aquarium_to_db(current_aquarium)
                        break
                case "5":
                    print_form("choix 5")
                    quit = typer.confirm("Voulez vous quitter sans sauvegarder")
                    if quit:
                        break
                case _:
                    print(print_form(ERREUR, 3))
            # current_aquarium.afficher_df()

    # data_manager.load_list_algues_from_json('part_algue-00005.json')
    # add_ten_to_aquarium(aquarium)
    # aquarium.save()

    typer.run(main)

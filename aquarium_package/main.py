import random
import math


import typer
from dotenv import load_dotenv

from aquarium_package.utils.psql_data_manager_orm import Base, engine

from aquarium_package.models.behaviors import (Herbivore,Carnivore,HermaphroditeAgeMixin,
                                               HermaphroditeOpportunisteMixin)
from aquarium_package.models import FishParentORM
from aquarium_package.factories import create_fish_type,create_algue
#from aquarium_package.utils import json_data_manager
from aquarium_package.ecosystem import Aquarium
from aquarium_package.services import load_aquarium

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

def print_form(s,v = 15):
    print(f"\n{'-'* v} {s} {'-'* v}")


def do_step(aquarium: Aquarium):

    for algue in aquarium.get_alive_algues():
        algue.viellir()
        #Verification que l'algue n'est pas morte de viellesse
        if  algue.age >= 11:
            algue.isDead()
        #Duplication de l'algue si Pv >= 10 avec la moitier des points de vie
        elif algue.pv >= 10:
            new_pv = math.floor(algue.pv/2)
            algue.pv = new_pv
            new_algue = create_algue(pv=new_pv, algue_aquarium_id=aquarium.id)

            aquarium.management_session.add_to_session(new_algue)
            aquarium.management_session.flush_to_session(new_algue)
            new_algue.name = f"Algue-{new_algue.id}"
            aquarium.algues_list.append(new_algue)

    for fish in aquarium.get_alive_fishs():
        fish.viellir()
        if fish.pv <= 0 or fish.age >= 20:
            fish.isDead()
        elif isinstance(fish, HermaphroditeAgeMixin) and fish.age == 15:
            fish.changed_sexe()

    alive_fishs = aquarium.get_alive_fishs()
    random.shuffle(alive_fishs)
    alive_algues = aquarium.get_alive_algues()


    for fish in alive_fishs:
        # Traitement pour que les poissons encore vivant mangent selon leur régime alimentaire si ils respectent
        # la condition de point de vie
        if 0 < fish.pv <= 5:
            if isinstance(fish, Herbivore) and alive_algues:
                proie = random.choice(alive_algues)
            elif isinstance(fish, Carnivore):
                proie = random.choice(alive_fishs)
            else:
                proie = None

            if proie and proie.is_alive and type(proie) != type(fish):
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
        # Traitement pour les poissons encore vivant se reproduisent si ils n'ont pas tenté de eat
        elif fish.is_alive:
            proie = random.choice(alive_fishs)
            if not(fish is proie) and proie.is_alive and type(proie) == type(fish):

                # Definir une chance de reussite :
                if fish.reproduce(proie) and random.random() > 0.90:
                    new_fish = create_fish_type(
                        type_fish=fish.type_fish_enum,
                        fish_aquarium_id=aquarium.id
                    )
                    aquarium.management_session.add_to_session(new_fish)
                    aquarium.management_session.flush_to_session(new_fish)
                    aquarium.management_session.add_to_session(FishParentORM(new_fish,fish,proie))
                    print(f"{fish.name} s'est reproduit avec {proie.name} et a donnée {new_fish.name}")
                    aquarium.add_fish(new_fish)

    #aquarium.afficher_df()


if __name__ == "__main__":
    load_dotenv()

    print_form('Debut du traitement')

    current_aquarium = Aquarium(-1)
    def main():
        while(True):
            print_form("Menu principal")
            print(MENU)
            choix = typer.prompt('Votre choix')
            match choix :
                case '1':
                    print_form("choix 1")
                    choix_aquarium = typer.prompt('veuillez choisir un numéro aquarium')
                    #try:
                    current_aquarium = load_aquarium(int(choix_aquarium))
                    break
                    #except ValueError:
                    #    print("La valeur choisie n'est pas correcte")
                case '2':
                    print_form("choix 2")
                
        while(True):
            print(MENU_AQUARIUM_OK)
            choix = typer.prompt('Votre choix')
            match choix :
                    case '1':
                        print_form('choix 2')
                        current_aquarium.add_fish()
                    case '2':
                        print_form('choix 3')
                        current_aquarium.add_algue()
                    case '3':
                        do_step(current_aquarium)
                    case '4':
                        print_form('choix 4')
                        saved = typer.confirm("Voulez vous enregistrer")
                        if saved and current_aquarium.id != -1:
                            #current_aquarium.save_to_json()
                            current_aquarium.save_to_db()
                            break
                    case '5':
                        print_form('choix 5')
                        quit = typer.confirm("Voulez vous quitter sans sauvegarder")
                        if quit :
                            break
                    case _ :
                        print(print_form(ERREUR, 3))
            #current_aquarium.afficher_df()


#data_manager.load_list_algues_from_json('part_algue-00005.json')
#add_ten_to_aquarium(aquarium)
#aquarium.save()

    typer.run(main)





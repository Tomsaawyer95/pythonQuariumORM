import random
import pandas as pd

from aquarium_package.models import FishORM, AlgueORM, Type
from aquarium_package.factories import algues_factory, fishs_factory, create_fish_type
from aquarium_package.manager import AquariumSessionManger
from sqlalchemy.inspection import inspect
from aquarium_package.utils import convert_to_df, Session

class Aquarium():

    _instances = {}

    def __new__(cls, id, *args, **kwargs):
        if id in cls._instances:
            return cls._instances[id]  # 🚨 Si déjà créé → on le renvoie
        instance = super().__new__(cls)  # 🧱 Sinon on crée une nouvelle instance
        cls._instances[id] = instance  # 🗃 On l’enregistre dans le cache
        return instance

    def __init__(self, id : int|None = None):
        if hasattr(self, '_initialized') and self._initialized:  # type: ignore
            return  # ✅ Si déjà initialisé → on saute l'init      
        self.fishs_list : list[FishORM] = []
        self.algues_list : list[AlgueORM] = []
        if id:
            self.id = id
        else :
            self.id = 1
        self.management_session = AquariumSessionManger()

    def save_to_db(self):
        """Sauvegarde l'aquarium dans la base postgresSql."""
        self.management_session.save_session()

    def add_fish(self, fish: FishORM | None = None):
        if fish is None:
            fish = fishs_factory.create_fish_type(
                aquarium_id=self.id
            )
        elif fish.type_fish is None:
            fish = fishs_factory.create_fish_type(
                aquarium_id=self.id,
                age=fish.age,
                name=fish.name,
                pv=fish.pv,
                sexe=fish.sexe,
                id=fish.id
            )
        self.management_session.add_to_session(fish)
        self.fishs_list.append(fish)

    def add_algue(self,age=0, pv=10):
        algue = algues_factory.create_algue(algue_aquarium_id = self.id, pv=pv, age=age)
        self.management_session.add_to_session(algue)
        self.management_session.flush_to_session(algue)
        algue.name = f"Algue-{algue.id}"
        self.algues_list.append(algue)
        return algue

    def get_alive_fishs(self):
        return [fish for fish in self.fishs_list if fish.is_alive]

    def get_alive_algues(self):
        return [algue for algue in self.algues_list if algue.is_alive]

    def afficher_df(self):
        print("*-------------------------------------*")
        print("*-------------------------------------*")
        df_algue, df_fish = convert_to_df(self)
        print(df_algue)
        print("*-------------------------------------*")
        print(df_fish)








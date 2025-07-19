import random

from faker import Faker
from sqlalchemy import Column, Integer, String, Boolean
from aquarium_package.utils.psql_data_manager_orm import Base
from aquarium_package.models.enums import Type, Sexe

faker = Faker()

class FishORM(Base):
    __tablename__ = 'fishs'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    type_fish = Column(String,nullable=False)
    sexe = Column(String)
    age = Column(Integer)
    pv = Column(Integer)
    fish_aquarium_id = Column(Integer)
    is_alive = Column(Boolean)

    __mapper_args__ = {
        "polymorphic_on": type_fish,
        "polymorphic_identity": "BASE"
    }

    def __init__(self,
                 id: int | None = None,
                 type_fish: Type | None = None,
                 sexe: Sexe | None = None,
                 age: int = 0,
                 pv: int = 20,
                 name: str | None = None,
                 fish_aquarium_id: int | None = 0,
                 is_alive: bool = True):
        self.id = id
        # Initialisation propre des attributs Enum → String
        self.sexe = sexe.name if isinstance(sexe, Sexe) else (sexe or random.choice(list(Sexe)).name)
        self.type_fish = type_fish.name if type_fish else self.__class__.type_fish.name

        self.age = age
        self.pv = pv
        self.fish_aquarium_id = fish_aquarium_id
        self.is_alive = is_alive

        self.name = name or (faker.name_male() if self.sexe == "MALE" else faker.name_female())

    @property
    def sexe_enum(self):
        return Sexe[self.sexe]

    @sexe_enum.setter
    def sexe_enum(self, value: Sexe):
        self.sexe = value.name

    @property
    def type_fish_enum(self):
        return Type[self.type_fish]

    @type_fish_enum.setter
    def type_fish_enum(self, value: Type):
        self.type_fish = value.name

    def isDead(self):
        self.is_alive = False

    def viellir(self):
        self.pv -= 1
        self.age += 1

    def reproduce(self, other_fish):
        raise NotImplementedError("Chaque type de poisson doit implémenter sa méthode reproduce.")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'type_fish': self.type_fish,
            'sexe': self.sexe,
            'age': self.age,
            'pv': self.pv,
            'fish_aquarium_id': self.fish_aquarium_id,
            'is_alive': self.is_alive
        }
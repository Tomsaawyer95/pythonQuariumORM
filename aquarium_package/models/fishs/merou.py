from aquarium_package.models import FishORM, Type
from aquarium_package.models.behaviors import Carnivore,HermaphroditeAgeMixin

class Merou(Carnivore, HermaphroditeAgeMixin, FishORM):
    type_fish_default = Type.MEROU.name

    __mapper_args__ = {
        "polymorphic_identity": "MEROU"
    }

    def __init__(self, **kwargs):
        kwargs['type_fish'] = Type.MEROU
        super().__init__(**kwargs)
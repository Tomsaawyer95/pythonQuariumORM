from aquarium_package.models import FishORM, Type
from aquarium_package.models.behaviors import Herbivore,HermaphroditeAgeMixin

class Bar(Herbivore, HermaphroditeAgeMixin, FishORM):
    type_fish_default = Type.BAR.name

    __mapper_args__ = {
        "polymorphic_identity": "BAR"
    }

    def __init__(self, **kwargs):
        kwargs['type_fish'] = Type.BAR
        super().__init__(**kwargs)
    
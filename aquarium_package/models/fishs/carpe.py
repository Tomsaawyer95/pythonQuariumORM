from aquarium_package.models import FishORM, Type
from aquarium_package.models.behaviors import Herbivore,MonoSexeMixin

class Carpe(Herbivore, MonoSexeMixin, FishORM):
    type_fish_default = Type.CARPE.name

    __mapper_args__ = {
        "polymorphic_identity": "CARPE"
    }

    def __init__(self, **kwargs):
        kwargs['type_fish'] = Type.CARPE
        super().__init__(**kwargs)
    
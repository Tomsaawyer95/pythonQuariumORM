from aquarium_package.models import FishORM, Type
from aquarium_package.models.behaviors import Carnivore, MonoSexeMixin

class Thon(Carnivore, MonoSexeMixin, FishORM):
    type_fish_default = Type.THON.name

    __mapper_args__ = {
        "polymorphic_identity": "THON"
    }

    def __init__(self, **kwargs):
        kwargs['type_fish'] = Type.THON
        super().__init__(**kwargs)
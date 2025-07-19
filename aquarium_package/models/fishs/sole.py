from aquarium_package.models.behaviors.HermaphroditeOpportunisteMixin import HermaphroditeOpportunisteMixin
from aquarium_package.models import FishORM, Type
from aquarium_package.models.behaviors import Herbivore

class Sole(Herbivore, HermaphroditeOpportunisteMixin, FishORM):
    type_fish_default = Type.SOLE.name

    __mapper_args__ = {
        "polymorphic_identity": "SOLE"
    }

    def __init__(self, **kwargs):
        kwargs['type_fish'] = Type.SOLE
        super().__init__(**kwargs)
    
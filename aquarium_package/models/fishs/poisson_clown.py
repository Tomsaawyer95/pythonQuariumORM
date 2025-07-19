from aquarium_package.models import FishORM, Type
from aquarium_package.models.behaviors import Carnivore,HermaphroditeOpportunisteMixin

class PoissonClown(Carnivore, HermaphroditeOpportunisteMixin, FishORM):
    type_fish_default = Type.POISSON_CLOWN.name

    __mapper_args__ = {
        "polymorphic_identity": "POISSON_CLOWN"
    }

    def __init__(self, **kwargs):
        kwargs['type_fish'] = Type.POISSON_CLOWN
        super().__init__(**kwargs)
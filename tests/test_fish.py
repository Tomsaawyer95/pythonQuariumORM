import pytest
from aquarium_package.models import FishORM, Sexe
from aquarium_package.models.fishs import Carpe, PoissonClown, Merou, Sole, Bar, Thon


def test_is_dead():
    Fish = FishORM(name="Nemo", age=2, pv=10)
    Fish.isDead()
    assert Fish.is_alive is False, "Le poisson devrait être marqué comme mort"


def test_viellir_incremente_age_et_diminue_pv():
    fish = FishORM(name="Nemo", age=2, pv=10)
    fish.viellir()
    assert fish.age == 3, "L'âge devrait être incrémenté de 1"
    assert fish.pv == 9, "Les points de vie devraient diminuer de 1"


def test_viellir_meurt_si_pv_inferieur_zero():
    fish = FishORM(name="Nemo", age=2, pv=1)
    fish.viellir()
    assert (
        fish.is_alive is False
    ), "Le poisson devrait être mort si les points de vie sont à 0 ou moins"


def test_viellir_meurt_si_age_depasse_20():
    fish = FishORM(name="Nemo", age=19, pv=10)
    fish.viellir()
    assert (
        fish.is_alive is False
    ), "Le poisson devrait être mort si l'âge est supérieur ou égal à 20"


@pytest.mark.parametrize("FishClass", [Bar, Merou])
def test_viellir_hermaphrodite_age_change_sexe(FishClass):
    fish = Bar(name="Nemo", age=14, pv=10, sexe=Sexe.MALE)
    fish.viellir()
    assert (
        fish.sexe == Sexe.FEMALE.name
    ), "Le sexe du poisson hermaphrodite devrait changer en féminin"


@pytest.mark.parametrize("FishClass", [Carpe, Thon, Merou, Bar])
def test_reproduce_creates_new_fish_HermaphroditeAge_and_MonoSexe_OK(FishClass):
    fish1 = FishClass(name="Fihs1", age=2, pv=10, sexe=Sexe.FEMALE)
    fish2 = FishClass(name="Fish2", age=3, pv=8, sexe=Sexe.MALE)
    is_born = fish1.reproduce(fish2)

    assert (
        is_born is True
    ), "La reproduction devrait être réussie pour les poissons hermaphrodites ou mono-sexe de sexe différent"


@pytest.mark.parametrize("FishClass", [Carpe, Thon, Merou, Bar])
def test_reproduce_creates_new_fish_HermaphroditeAge_and_MonoSexe_KO(FishClass):
    fish1 = FishClass(name="Fihs1", age=2, pv=10, sexe=Sexe.MALE)
    fish2 = FishClass(name="Fish2", age=3, pv=8, sexe=Sexe.MALE)
    is_born = fish1.reproduce(fish2)
    assert (
        is_born is False
    ), "La reproduction devrait un echec pour les poissons hermaphrodites ou mono-sexe de meme différent"


@pytest.mark.parametrize(
    "FishClass",
    [
        PoissonClown,
        Sole,
    ],
)
def test_reproduce_creates_new_fish_HermaphroditeOpportuniste_sexe_different(FishClass):
    fish1 = FishClass(name="Fihs1", age=2, pv=10, sexe=Sexe.FEMALE)
    fish2 = FishClass(name="Fish2", age=3, pv=8, sexe=Sexe.MALE)
    is_born = fish1.reproduce(fish2)

    assert (
        is_born is True
    ), "La reproduction devrait être réussie pour les poissons hermaphrodites ou mono-sexe de sexe différent"
    assert fish1.sexe == "FEMALE", "Le poisson 1 devrait rester de sexe féminin"


@pytest.mark.parametrize("FishClass", [PoissonClown, Sole])
def test_reproduce_creates_new_fish_HermaphroditeOpportuniste_meme_different(FishClass):
    fish1 = FishClass(name="Fihs1", age=2, pv=10, sexe=Sexe.MALE)
    fish2 = FishClass(name="Fish2", age=3, pv=8, sexe=Sexe.MALE)
    is_born = fish1.reproduce(fish2)
    assert (
        is_born is True
    ), "La reproduction devrait être réussie pour les poissons hermaphrodites ou mono-sexe de sexe différent"
    assert (
        fish1.sexe == "FEMALE"
    ), "Le poisson1 devrait changer de sexe et passer à féminin"

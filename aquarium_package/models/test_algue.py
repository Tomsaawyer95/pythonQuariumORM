import pytest
from aquarium_package.models import AlgueORM


def test_is_dead():
    algue = AlgueORM(age=3, pv=10)
    algue.isDead()
    assert algue.is_alive is False, "L'algue devrait être marqué comme morte"


def test_viellir_incremente_age_et_increse_pv():
    algue = AlgueORM(age=3, pv=10)
    algue.viellir()
    assert algue.age == 3, "L'âge devrait être incrémenté de 1"
    assert algue.pv == 9, "Les points de vie devraient diminuer de 1"


def test_viellir_and_dead_by_pv():
    algue = AlgueORM(age=3, pv=1)
    algue.viellir()
    assert algue.age == 4, "L'âge devrait être incrémenté de 1"
    assert (
        algue.pv == 0
    ), "Les points de vie devraient être égaux à 0 après vieillissement"
    assert (
        algue.is_alive == False
    ), "L'algue devrait être morte après avoir atteint 0 PV"


def test_viellir_and_die_by_age():
    algue = AlgueORM(age=19, pv=6)
    algue.viellir()
    assert algue.age == 20, "L'âge devrait être incrémenté de 1"
    assert (
        algue.pv == 0
    ), "Les points de vie devraient être égaux à 0 après vieillissement"
    assert (
        algue.is_alive == False
    ), "L'algue devrait être morte après avoir atteint 20 ans"

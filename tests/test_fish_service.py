import pytest
import random
from aquarium_package.factories import create_fish_type
from aquarium_package.services.fish_service import handle_fishs_eating, handle_fishs_reproduction
from aquarium_package.models import FishORM, AlgueORM, FishParentORM
from aquarium_package.models.behaviors import Herbivore, Carnivore
from aquarium_package.ecosystem.aquarium import Aquarium

class DummyHerbivore(FishORM, Herbivore):
    def __init__(self, name="Herb", pv=10):
        self.name = name
        self.pv = pv
        self.is_alive = True
        self.type_fish = "HERBIVORE"
    @property
    def type_fish_enum(self):
        return None
    def eat(self, proie):
        proie.pv -= 5
    def reproduce(self, other_fish):
        return True  # Simulate successful reproduction
    def isDead(self):
        self.is_alive = False

class DummyCarnivore(FishORM, Carnivore):
    def __init__(self, name="Carn", pv=10):
        self.name = name
        self.pv = pv
        self.is_alive = True
        self.type_fish = "CARNIVORE"
    @property
    def type_fish_enum(self):
        return None
    def eat(self, proie):
        proie.pv -= 5
    def reproduce(self, other_fish):
        return True
    def isDead(self):
        self.is_alive = False

class DummyAlgue(AlgueORM):
    def __init__(self, name="Alg", pv=10):
        self.name = name
        self.pv = pv
        self.is_alive = True
    def isDead(self):
        self.is_alive = False

class DummySession:
    def __init__(self):
        self.added = []
        self.flushed = []
    def add_to_session(self, obj):
        self.added.append(obj)
    def flush_to_session(self, obj):
        self.flushed.append(obj)

class DummyAquarium(Aquarium):
    def __init__(self):
        self.id = 1
        self.management_session = DummySession()
        self.fishs = []
    def add_fish(self, fish):
        self.fishs.append(fish)

def test_handle_fishs_eating_herbivore_eats_algue(monkeypatch):
    fish = DummyHerbivore()
    algue = DummyAlgue()
    alive_fishs = [DummyHerbivore()]
    alive_algues = [algue]

    monkeypatch.setattr(random, "choice", lambda x: x[0])
    handle_fishs_eating(fish, alive_fishs, alive_algues)
    assert algue.pv == 5

def test_handle_fishs_eating_carnivore_eats_fish(monkeypatch):
    fish = DummyCarnivore()
    prey = DummyHerbivore()
    alive_fishs = [prey]
    alive_algues = []

    monkeypatch.setattr(random, "choice", lambda x: x[0])
    handle_fishs_eating(fish, alive_fishs, alive_algues)
    assert prey.pv == 5

def test_handle_fishs_eating_no_proie(monkeypatch, capsys):
    fish = DummyHerbivore()
    alive_fishs = []
    alive_algues = []

    handle_fishs_eating(fish, alive_fishs, alive_algues)
    captured = capsys.readouterr()
    assert "n'a rien trouvé a manger" in captured.out

def test_handle_fishs_eating_wrong_type(monkeypatch, capsys):
    fish = DummyHerbivore()
    algue = DummyHerbivore()  # Not an algue, so type mismatch
    alive_fishs = []
    alive_algues: list[DummyHerbivore] = [algue]

    monkeypatch.setattr(random, "choice", lambda x: x[0])
    handle_fishs_eating(fish, alive_fishs, alive_algues)
    captured = capsys.readouterr()
    assert "a essayer de manger" in captured.out

def test_handle_fishs_reproduction_success(monkeypatch):
    aquarium = DummyAquarium()
    fish = DummyHerbivore(name="Parent1")
    mate = DummyHerbivore(name="Parent2")
    alive_fishs = [mate]

    # Patch random.choice to always pick mate, random.random to always succeed
    monkeypatch.setattr(random, "choice", lambda x: x[0])
    monkeypatch.setattr(random, "random", lambda: 0.95)

    # Patch create_fish_type to return a DummyHerbivore
    monkeypatch.setattr("aquarium_package.services.fish_service.create_fish_type", lambda **kwargs: DummyHerbivore(name="Baby"))

    handle_fishs_reproduction(aquarium, fish, alive_fishs)
    assert any(f.name == "Baby" for f in aquarium.fishs)
    assert len(aquarium.fishs) == 1  # Only the baby fish should be added
    assert any(isinstance(obj, DummyHerbivore) and obj.name == "Baby" for obj in aquarium.management_session.added)

def test_handle_fishs_reproduction_failure_not_same_type(monkeypatch):
    aquarium = DummyAquarium()
    fish = DummyHerbivore(name="Parent1")
    mate = DummyCarnivore(name="Parent2")
    alive_fishs = [mate]

    # Patch random.choice to always pick mate, random.random to always fail
    monkeypatch.setattr(random, "choice", lambda x: x[0])
    monkeypatch.setattr(random, "random", lambda: 0.95)

    handle_fishs_reproduction(aquarium, fish, alive_fishs)
    assert len(aquarium.fishs) == 0
    assert not any(f.name == "Baby" for f in aquarium.fishs)

def test_handle_fishs_reproduction_failure_not_same_fish(monkeypatch):
    aquarium = DummyAquarium()
    fish = DummyHerbivore(name="Parent1")
    mate = fish
    alive_fishs = [mate]

    # Patch random.choice to always pick mate, random.random to always fail
    monkeypatch.setattr(random, "choice", lambda x: x[0])
    monkeypatch.setattr(random, "random", lambda: 0.95)

    handle_fishs_reproduction(aquarium, fish, alive_fishs)
    assert len(aquarium.fishs) == 0
    assert not any(f.name == "Baby" for f in aquarium.fishs)
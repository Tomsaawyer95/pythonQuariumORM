from enum import Enum

class Sexe(Enum):
    """liste des sexe des poissons

    Args:
        Enum (str): Sexe du poisson
    """
    MALE = 'Male'
    FEMALE = 'Female'

class Type(Enum):
    """Donne la liste type de poissons

    Args:
        Enum (str): Type de poisson
    """
    POISSON_CLOWN = 'PoissonClown'
    CARPE = 'Carpe'
    BAR = 'Bar'
    SOLE = 'Sole'
    THON = 'Thon'
    MEROU ='Merou'

from aquarium_package.models import AlgueORM

def create_algue(   pv : int = 10,
                    age : int = 0,
                    id : int | None = None, 
                    algue_aquarium_id : int | None = None,
                    name : str | None = None
                    ):
    """    Crée une instance d'Algue avec les paramètres fournis. """
    return AlgueORM(pv=pv, id=id,age=age, algue_aquarium_id=algue_aquarium_id, name=name)
    
    
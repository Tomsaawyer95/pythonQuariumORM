from aquarium_package.ecosystem import Aquarium
from aquarium_package.models import FishORM, AlgueORM
from sqlalchemy.orm import Session

def save_aquarium_to_db(aquarium: Aquarium):
    """
    Saves the current state of the given Aquarium instance to the database.

    This function triggers the save operation on the aquarium's management session,
    persisting any changes made to the aquarium.

    Args:
        aquarium (Aquarium): The Aquarium instance whose state should be saved.
    """
    aquarium.management_session.save_session()

def load_aquarium(id: int) -> Aquarium:
    """
    Loads an Aquarium instance by its ID, including its living fish and algae.
    Args:
        id (int): The unique identifier of the aquarium to load.
    Returns:
        Aquarium: An Aquarium object populated with its living fish and algae.
    Notes:
        - Only fish and algae marked as alive are included in the returned Aquarium.
        - The function assumes that the Aquarium class and ORM models (FishORM, AlgueORM) are properly defined.
    """


    aquarium = Aquarium(id)
    session = aquarium.management_session.session
    aquarium.fishs_list = session.query(FishORM).filter_by(fish_aquarium_id=id,is_alive=True).all()
    aquarium.algues_list = session.query(AlgueORM).filter_by(algue_aquarium_id=id,is_alive=True).all()
    return aquarium

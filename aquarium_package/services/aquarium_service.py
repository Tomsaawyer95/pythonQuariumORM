from aquarium_package.ecosystem import Aquarium
from aquarium_package.models import FishORM, AlgueORM
from sqlalchemy.orm import Session

def save_aquarium_to_db(aquarium: Aquarium):
    aquarium.management_session.save_session()

def load_aquarium(id: int) -> Aquarium:
    aquarium = Aquarium(id)
    session = aquarium.management_session.session
    aquarium.fishs_list = session.query(FishORM).filter_by(fish_aquarium_id=id).all()
    aquarium.algues_list = session.query(AlgueORM).filter_by(algue_aquarium_id=id).all()
    return aquarium

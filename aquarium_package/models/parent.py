from sqlalchemy import Column, Integer, ForeignKey, String

from aquarium_package.utils.psql_data_manager_orm import Base


class FishParentORM(Base):
    __tablename__ = 'fish_parents'
    id = Column(Integer, primary_key=True)
    child_id = Column(Integer, ForeignKey('fishs.id'))
    parent1_id = Column(Integer, ForeignKey('fishs.id'))
    parent2_id = Column(Integer, ForeignKey('fishs.id'))

    def __init__(self,child,parent1,parent2):
        self.child_id=child.id
        self.parent1_id = parent1.id
        self.parent2_id = parent2.id



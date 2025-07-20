from sqlalchemy import Column, Integer, ForeignKey, String

from aquarium_package.utils.psql_data_manager_orm import Base


class FishParentORM(Base):
    """
    ORM model representing the parentage relationship of a fish.
    Attributes:
        id (int): Primary key for the parentage record.
        child_id (int): Foreign key referencing the child fish's ID.
        parent1_id (int): Foreign key referencing the first parent's fish ID.
        parent2_id (int): Foreign key referencing the second parent's fish ID.
    Args:
        child: An instance of the Fish ORM model representing the child fish.
        parent1: An instance of the Fish ORM model representing the first parent fish.
        parent2: An instance of the Fish ORM model representing the second parent fish.
    The FishParentORM class is used to store and manage the relationship between a child fish and its two parents in the database.
    """
    __tablename__ = 'fish_parents'
    id = Column(Integer, primary_key=True)
    child_id = Column(Integer, ForeignKey('fishs.id'))
    parent1_id = Column(Integer, ForeignKey('fishs.id'))
    parent2_id = Column(Integer, ForeignKey('fishs.id'))

    def __init__(self,child,parent1,parent2):
        self.child_id=child.id
        self.parent1_id = parent1.id
        self.parent2_id = parent2.id



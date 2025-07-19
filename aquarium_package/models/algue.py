from pathlib import Path

from sqlalchemy import Integer, Column, String, DateTime, Boolean, ForeignKey

from aquarium_package.utils.psql_data_manager_orm import Base

class AlgueORM(Base):
    __tablename__ = 'algues'

    id = Column(Integer, primary_key=True)
    pv = Column(Integer)
    name = Column(String)
    age = Column(Integer)
    algue_aquarium_id = Column(Integer)
    is_alive = Column(Boolean)
    
    def __init__(   self,
                    id: int | None = None,
                    pv : int = 10,
                    algue_aquarium_id : int | None = None,
                    name : str | None = None,
                    age : int = 0,
                    is_alive : bool = True):
        
        self.pv = pv
        self.algue_aquarium_id = algue_aquarium_id
        self.age = age
        self.id = id
        self.is_alive = is_alive
        self.algue_name = name
    

    def viellir(self):
        self.pv += 1
        self.age += 1

    def isDead(self):
        self.is_alive = False
    
    def to_dict(self):
        return {'id' : self.id , 'name' : self.name, 'pv' : self.pv, 'algue_aquarium_id' : self.aquarium_id, 'age' : self.age, 'is_alive' : self.is_alive}


if __name__ == "__main__":
    algue = AlgueORM(2)
    print(algue.name, algue.pv)

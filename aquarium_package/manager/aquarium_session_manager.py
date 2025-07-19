from aquarium_package.utils import Session

class AquariumSessionManger:
    """
    AquariumSessionManger
    """
    def __init__(self):
        self.session = Session()

    def add_to_session(self,object):
        self.session.add(object)

    def add_all_to_session(self,list_of_objects):
        self.session.add_all(list_of_objects)

    def flush_to_session(self,object):
        self.session.flush([object])

    def save_session(self):
        self.session.commit()
        self.session.close()


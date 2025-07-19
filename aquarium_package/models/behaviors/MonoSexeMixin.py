

class MonoSexeMixin():
    def reproduce(self,fish):
        """
             Args:
                fish (FishORM): fish with which he reproduces
            Returns:
                bool : True
        """
        if fish.sexe != self.sexe:
            return True
        else:
            return False
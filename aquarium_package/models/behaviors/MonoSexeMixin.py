

class MonoSexeMixin():
    def reproduce(self,fish):
        if fish.sexe != self.sexe:
            return True
        else:
            return False
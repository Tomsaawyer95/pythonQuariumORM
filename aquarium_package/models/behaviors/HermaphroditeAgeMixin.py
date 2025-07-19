from aquarium_package.models.enums import Sexe

class HermaphroditeAgeMixin():
    def reproduce(self,fish):
        if fish.sexe != self.sexe:
            return True
        else :
            return False


    def changed_sexe(self):
        if self.sexe == Sexe.MALE:
            self.sexe = Sexe.FEMALE
        elif self.sexe == Sexe.FEMALE:
            self.sexe = Sexe.MALE
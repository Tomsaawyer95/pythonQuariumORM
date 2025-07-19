from aquarium_package.models.enums import Sexe

class HermaphroditeOpportunisteMixin():
    def reproduce(self,fish ):
        if fish.sexe == self.sexe:
            self.changed_sexe()
        return True

    def changed_sexe(self):
        if self.sexe == Sexe.MALE:
            self.sexe = Sexe.FEMALE
        elif self.sexe == Sexe.FEMALE:
            self.sexe = Sexe.MALE

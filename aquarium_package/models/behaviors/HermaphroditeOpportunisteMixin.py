from aquarium_package.models.enums import Sexe


class HermaphroditeOpportunisteMixin:
    def reproduce(self, fish):
        """
         Args:
            fish (FishORM): fish with which he reproduces
        Returns:
            bool : True
        """
        if fish.sexe == self.sexe:
            self.changed_sexe()
        return True

    def changed_sexe(self):
        """
        Changes the sexe of the fish
        Returns:
            Sexe of fish
        """
        if self.sexe == Sexe.MALE.name:
            self.sexe = Sexe.FEMALE.name
        elif self.sexe == Sexe.FEMALE.name:
            self.sexe = Sexe.MALE.name

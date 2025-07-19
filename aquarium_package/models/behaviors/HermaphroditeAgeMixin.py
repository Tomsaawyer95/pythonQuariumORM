from aquarium_package.models.enums import Sexe

class HermaphroditeAgeMixin():
    def reproduce(self,fish):
        """
        Args:
            fish (FishORM): fish with which he reproduces
        Returns:
            bool :
                - True if the fish was reproduced successfully
                - False if the fish was not reproduced
                Conditionning by the sexe of the two fishes
        """
        if fish.sexe != self.sexe:
            return True
        else :
            return False

    def changed_sexe(self):
        """
            Changes the sexe of the fish
            Returns:
                Sexe of fish
        """
        if self.sexe == Sexe.MALE:
            self.sexe = Sexe.FEMALE
        elif self.sexe == Sexe.FEMALE:
            self.sexe = Sexe.MALE
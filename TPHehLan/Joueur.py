from Personne import Personne
from Tournoi import Tournoi

class Joueur(Personne):
    def __init__(self, nom, prenom, participeTournoi):
        super().__init__(nom, prenom)
        self.__participeTournoi = participeTournoi
    
    @property
    def participeTournoi(self):
        return self.__participeTournoi

    @participeTournoi.setter
    def participeTournoi(self, participeTournoi):
        self.__participeTournoi = participeTournoi
    
    def choisirTournoi(T : Tournoi):
        pass

    def inscriptionTournoi(T : Tournoi):
        pass

    
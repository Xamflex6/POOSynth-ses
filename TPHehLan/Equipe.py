from Joueur import Joueur
from Tournoi import Tournoi

class Equipe:
    def __init__(self, nomEquipe, compositionEquipe : Joueur):
        self.__nomEquipe = nomEquipe
        self.__compositionEquipe = compositionEquipe

    @property
    def nomEquipe(self):
        return self.__nomEquipe

    @nomEquipe.setter
    def nomEquipe(self, nomEquipe):
        self.__nomEquipe = nomEquipe
    
    @property
    def compositionEquipe(self):
        return self.__compositionEquipe

    @compositionEquipe.setter
    def compositionEquipe(self, compositionEquipe):
        self.__compositionEquipe = compositionEquipe
    
    def inscriptionEquipe(T : Tournoi):
        pass

    
    

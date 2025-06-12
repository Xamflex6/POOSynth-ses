from Organisateur import Organisateur

class Tournoi:
    def __init__(self, nom, equipes, round, jeu):
        self.__nom = nom 
        self.__equipes = equipes
        self.__round = round 
        self.__jeu = jeu
    
    @property
    def nom(self):
        return self.__nom
    
    @nom.setter
    def nom(self, nom):
        self.__nom = nom
    
    @property
    def equipes(self):
        return self.__equipes
    
    @equipes.setter
    def equipes(self, equipes):
        self.__equipes = equipes
    
    @property
    def round(self):
        return self.__round
    
    @round.setter
    def round(self, round):
        self.__round = round
    
    @property
    def jeu(self):
        return self.__jeu
    
    @jeu.setter
    def jeu(self, jeu):
        self.__jeu = jeu
    
    def lancerTournoi(self):
        pass

    def creerTournoi(O : Organisateur):
        pass

    def configTournoi(O: Organisateur):
        pass
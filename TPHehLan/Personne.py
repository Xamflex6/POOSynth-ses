from abc import ABC, abstractmethod

class Personne(ABC):
    def __init__(self, nom, prenom):
        self._nom = nom
        self._prenom = prenom
    
    @property
    def nom(self):
        return self._nom
    
    @nom.setter
    def nom(self, nom):
        self._nom = nom
    
    @property
    def prenom(self):
        return self._prenom
    
    @prenom.setter
    def prenom(self, prenom):
        self._prenom = prenom
    
    def sePresenter(self):
        pass
